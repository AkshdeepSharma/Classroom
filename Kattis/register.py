def main():
    operations = 0
    registers = [1, 2, 4, 6, 10, 12, 16, 18]
    to_multiply_by = [1, 2, 6, 30, 210, 2310, 30030, 510510]
    input_registers = list(map(int, input().split()))
    for i in range(len(registers)):
        operations += (registers[i] - input_registers[i]) * to_multiply_by[i]
    print(operations)


if __name__ == '__main__':
    main()
