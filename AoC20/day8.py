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

    return acc


def main():
    DEBUG = False
    if DEBUG:
        data = read_input("testData")
    else:
        data = read_input("data8")

    print(f"Before Infinite Loop, Accumulator: {execute_program(data)}")


if __name__ == "__main__":
    main()
