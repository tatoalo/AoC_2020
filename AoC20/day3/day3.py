def read_input(f):
    with open(f, 'r') as file:
        input_lines = [line.strip() for line in file]

    return input_lines


def handle_data(debug, positional_orders):

    if debug:
        d = read_input("testData")
    else:
        d = read_input("data3")

    trees_encountered = []
    # positional_orders = [["R 1", "D 1"], ["R 3", "D 1"], ["R 5", "D 1"], ["R 7", "D 1"], ["R 1", "D 2"]]
    print(f"Map of {len(d)} elements")

    for orders in positional_orders:
        current_pos = 0
        inside_trees = 0
        val = [int(s) for s in orders[0].split() if s.isdigit()][0]
        val_set = [int(s) for s in orders[1].split() if s.isdigit()][0]

        for p in range(0, len(d)-1, val_set):
            # val = [int(s) for s in orders[0].split() if s.isdigit()][0]
            # val_set = [int(s) for s in orders[1].split() if s.isdigit()][0]
            current_path = list(d[p])
            forward_path = list(d[p + val_set])

            current_pos = (current_pos + val) % len(current_path)

            if forward_path[current_pos] == '#':
                forward_path[current_pos] = 'X'
                inside_trees += 1
            else:
                forward_path[current_pos] = 'O'

            d[p+val_set] = ''.join(forward_path)

        trees_encountered.append(inside_trees)

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

    encountered = [handle_data(DEBUG, [["R 1", "D 1"]]),
                   handle_data(DEBUG, [["R 3", "D 1"]]),
                   handle_data(DEBUG, [["R 5", "D 1"]]),
                   handle_data(DEBUG, [["R 7", "D 1"]]),
                   handle_data(DEBUG, [["R 1", "D 2"]])]

    print(f"Encountered trees: {encountered}")
    res = 1
    for _ in encountered:
        res *= _[0]

    print(f"Multiplication encountered trees: {res}")


if __name__ == "__main__":
    main()
