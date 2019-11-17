import random
import os
import pyminizip

if __name__ == "__main__":
    pwd = str(random.randint(1000,9999))
    print(pwd)
    pyminizip.compress("irc.txt", "", "enc.zip", pwd.encode(), 1)