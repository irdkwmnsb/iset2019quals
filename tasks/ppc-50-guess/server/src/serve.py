import asyncio
import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format="[%(asctime)s-%(name)21s-%(levelname)5s] %(message)s")

FLAG = "flag{sm4rt_gu3sses_j21yd7hkk2k}"


class GuesserServer(asyncio.Protocol):
    def __init__(self):
        self.loop = asyncio.get_running_loop()
        self.cur_time_limit = 60
        self.level = 0
        l = list(range(1, 256))
        random.shuffle(l)
        self.flag = l + [ord(i) for i in FLAG]

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        strpeer = "%s:%s" % peername
        self.logger = logging.getLogger(strpeer)
        self.logger.info("Opened %s", peername)
        self.transport = transport
        self.transport.write(b"Welcome to s01EGE-43662 (Ubuntu 19.04 (GNU/Linux 5.0.0-32-generic x86_64))\n")
        self.make_task()

    def make_task(self):
        self.tries = 8
        self.transport.write(("Task %s. Guess a number in range [1, 255]. Give a valid answer in %s seconds or %s tries\n>" % (
            self.level + 1, self.cur_time_limit, self.tries)
                              ).encode())
        self.logger.info("task_n=%s, t_l=%s, task=%s, tries=%s", self.level, self.cur_time_limit, self.flag[self.level], self.tries)
        if hasattr(self, "timeout_handle"):
            self.timeout_handle.cancel()
        self.timeout_handle = self.loop.call_later(
            self.cur_time_limit, self._timeout,
        )

    def check_answer(self, n):
        if self.tries == 0:
            self.logger.info("Is guessing")
            self.transport.write(b"Stop guessing.\n")
            self.transport.close()
            return
        self.tries -= 1
        if self.flag[self.level] > n:
            self.logger.info("Wrong, answer is higher, %s guesses remaining", self.tries)
            self.transport.write(b"Wrong. Take higher\n>")
        elif self.flag[self.level] < n:
            self.logger.info("Wrong, answer is lower, %s guesses remaining", self.tries)
            self.transport.write(b"Wrong. Take lower\n>")
        else:
            self.logger.info("Correct")
            self.transport.write(b"Correct.\n")
            self.level += 1
            if self.level == len(self.flag):
                self.transport.write(b"Good job! You already have your flag. Look for it.")
                self.transport.close()
            else:
                self.cur_time_limit = max(self.cur_time_limit / 2, 5)
                self.make_task()

    def data_received(self, data):
        self.logger.info("Received %s", data)
        data = data.decode().strip()
        if not data.isdigit():
            self.transport.write(b"That is not a number\n")
            return
        self.check_answer(int(data))

    def connection_lost(self, exc=None):
        if not self.transport.get_extra_info("open"):
            self.transport.write(b"Something went wrong.")
        self.logger.info("Connection lost")
        self.transport.close()

    def _timeout(self):
        self.logger.info("Timeout")
        self.transport.write(b"\rYou are too slow!")
        self.transport.close()


async def main(host, port):
    loop = asyncio.get_running_loop()
    server = await loop.create_server(GuesserServer, host, port)
    logging.info(f"Serving on {host}:{port}")
    print("serving")
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main('0.0.0.0', 33003))
