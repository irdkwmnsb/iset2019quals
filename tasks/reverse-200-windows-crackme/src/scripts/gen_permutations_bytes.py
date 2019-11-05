from copy import copy
from random import shuffle, randint


def main():
    data = [randint(1, 255) for i in range(20)]
    super_data = copy(data)
    shuffle(super_data)
    # super_data = ''.join(super_data)
    print(data)
    print(super_data)
    result = []
    for key, value in enumerate(data):
        result.append('secretData[{}] = encryptedData[{}];'.format(key, super_data.index(value)))

    shuffle(result)
    for i in result:
        print(i)


if __name__ == '__main__':
    main()
