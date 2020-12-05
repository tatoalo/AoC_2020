def read_input(f):
    with open(f, 'r') as file:
        input_lines = [line.strip() for line in file]

    return input_lines


def handle_data(d):
    trees_encountered = 0
    positional_orders = ["R 3", "D 1"]
    print(f"Map of {len(d)} elements")

    current_pos = 0
    for p in range(0, len(d)-1):
        val = [int(s) for s in positional_orders[0].split() if s.isdigit()][0]
        val_set = [int(s) for s in positional_orders[1].split() if s.isdigit()][0]

        current_path = list(d[p])
        forward_path = list(d[p + val_set])

        current_pos = (current_pos + val) % len(current_path)

        if forward_path[current_pos] == '#':
            forward_path[current_pos] = 'X'
            trees_encountered += 1
        else:
            forward_path[current_pos] = 'O'

        d[p+val_set] = ''.join(forward_path)

    print()
    for _ in d:
        print(_)

    return trees_encountered


def main():
    DEBUG = False
    if DEBUG:
        data = read_input("testData")
    else:
        data = read_input("data3")

    print(f"Encountered trees: {handle_data(data)}")


if __name__ == "__main__":
    main()
