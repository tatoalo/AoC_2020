def read_input(f):
    with open(f, 'r') as file:
        input_lines = [line.strip() for line in file]

    return input_lines


def extrapolate_data(d):
    valid = 0
    for item in d:
        split_item = item.split(' ')

        lowerB, upperB = split_item[0].split('-')
        lowerB = int(lowerB)
        upperB = int(upperB)
        target = split_item[1].split(':')[0]
        psw = split_item[2]

        # print(f"min = {lowerB}, max = {upperB}")
        # print(f"target = {target}")
        # print(f"password = {psw}")

        count = psw.count(target)
        # print(f"Found {count}")
        if lowerB <= count <= upperB:
            valid += 1

    return valid


def main():
    DEBUG = False
    if DEBUG:
        data = read_input("testData")
    else:
        data = read_input("data2")

    print(f"Valid passwords: {extrapolate_data(data)}")


if __name__ == "__main__":
    main()
