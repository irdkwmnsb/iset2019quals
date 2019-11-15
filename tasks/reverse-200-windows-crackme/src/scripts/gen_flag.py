def main():
    gamma = reversed('ILOVEBEES')
    gamma_number = 216127633
    gamma_data = [ord(i) for i in gamma] + [i for i in gamma_number.to_bytes(4, 'little', signed=True)] + \
                 [241, 120, 227, 83, 188, 209, 124, 105, 173, 75, 96, 165, 34, 168, 156] + \
                 [186, 196, 27, 0, 1] * 3 + \
                 [i for i in gamma_number.to_bytes(4, 'little', signed=True)][::-1] + [ord(i) for i in reversed('OMTI')]

    print(gamma_data)
    flag = 'flag{y0u_4r3_0n3_573p_cl053r_70_h4ck_7h3_p3n7460n1}'
    flag_data = [ord(i) for i in flag]

    print(flag_data)
    print(len(flag))
    print(len(flag_data))
    print(len(gamma_data))
    result = [flag_data[i] ^ gamma_data[i] for i in range(len(flag_data))]
    print(chr(gamma_data[8] ^ result[8]))
    print(result)


if __name__ == '__main__':
    main()
