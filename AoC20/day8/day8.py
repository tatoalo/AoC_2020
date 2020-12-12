def read_input(f):
    with open(f, 'r') as file:
        input_lines = [line.strip() for line in file]

    return input_lines


def execute_program(data):
    acc = 0
    flagRepeated = False
    executed_instructions = []
    indices = [num for num, _ in enumerate(data)]
    pos = indices[0]

    opcode = data[pos]

    try:
        while not flagRepeated:

            if pos in executed_instructions:
                flagRepeated = True
            else:
                executed_instructions.append(pos)
                value = int(opcode.split(" ")[1])

                if 'acc' in opcode:
                    acc += value
                    pos += 1
                    opcode = data[pos]
                elif 'jmp' in opcode:
                    pos += value
                    opcode = data[pos]
                else:
                    if value == 0:
                        pos += 1
                    else:
                        pos += 1
                    opcode = data[pos]

    except IndexError as e:
        print("Program terminated correctly.")
        return -1, acc

    return 0, acc


def main():
    DEBUG = False
    if DEBUG:
        data = read_input("testData")
    else:
        data = read_input("data8")

    for i in range(len(data)):
        t = list(data)

        if t[i].split()[0] == 'nop':
            t[i] = 'jmp' + ' ' + t[i].split()[1]
        elif t[i].split()[0] == 'jmp':
            t[i] = 'nop' + ' ' + t[i].split()[1]
        code, acc = execute_program(t)
        if code == -1:
            print(acc)


if __name__ == "__main__":
    main()
