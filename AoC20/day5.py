def read_input(f):
    with open(f, 'r') as file:
        input_lines = [line.strip() for line in file]

    return input_lines


def retrieve_row(data):
    # t = data[0]
    rows = data[:7]
    chosen_row = []

    possible_values = [0, 128]
    index = 128
    for pos in rows:
        index = int(index / 2)
        if pos == 'F':
            possible_values = [possible_values[0], possible_values[0] + index - 1]
            # print(f"index: {index}, values: {possible_values}")
        else:
            possible_values = [possible_values[0] + index, possible_values[1]]
            # print(f"index: {index}, values: {possible_values}")

        if possible_values[0] == possible_values[1]:
            chosen_row = possible_values[0]

    # print(f"Chosen row: {chosen_row}")
    return chosen_row


def retrieve_column(data):
    # t = data[0]
    columns = data[7:]
    chosen_column = []

    possible_values = [0, 8]
    index = 8
    for pos in columns:
        index = int(index / 2)
        if pos == 'L':
            possible_values = [possible_values[0], possible_values[0] + index - 1]
            chosen_column = possible_values[1]
            # print(f"index: {index}, values: {possible_values}")
        else:
            possible_values = [possible_values[0] + index, possible_values[1]]
            chosen_column = possible_values[0]
            # print(f"index: {index}, values: {possible_values}")

        if possible_values[0] == possible_values[1]:
            chosen_column = possible_values[0]

    # print(f"Final possible values: {possible_values}")
    # print(f"Chosen column: {chosen_column}")
    return chosen_column


def retrieve_seat_ID(row, column):
    return row * 8 + column


def sanity_check(maxID, currentID):
    if maxID == 0:
        maxID = currentID
    elif currentID > maxID:
        maxID = currentID

    return maxID


def main():
    DEBUG = False
    if DEBUG:
        data = read_input("testData")
    else:
        data = read_input("data5")

    max_seat_ID = 0
    for d in data:
        row = retrieve_row(d)
        column = retrieve_column(d)
        seat_ID = retrieve_seat_ID(row, column)

        max_seat_ID = sanity_check(max_seat_ID, seat_ID)
        print(f"Row: {row}, Column: {column}, Seat ID: {seat_ID}")

    print(f"Largest ID: {max_seat_ID}")


if __name__ == "__main__":
    main()
