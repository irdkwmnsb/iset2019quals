from random import shuffle


def main():
    data = [241, 120, 227, 83, 188, 209, 124, 105, 173, 75, 96, 165, 34, 168, 156, 85, 214, 43, 204, 235]

    result = []
    for key, value in enumerate(data):
        result.append('data[{}] = {};'.format(key+13, value))

    shuffle(result)
    for i in result:
        print(i)


if __name__ == '__main__':
    main()
