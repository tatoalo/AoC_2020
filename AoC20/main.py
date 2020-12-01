def read_input(f):
    with open(f, 'r') as file:
        input_lines = [line.strip() for line in file]

    final_data = []
    for i in input_lines:
        final_data.append(int(i))

    return final_data


def extrapolate_entries(d):
    entries = [None, None]
    goal = 2020
    filtered = list(filter(lambda x: x < goal + 1, d))
    filtered = sorted(filtered)

    for i in filtered:
        for k in filtered:
            filtered.reverse()
            if i + k == goal:
                entries[0] = i
                entries[1] = k

    if entries[0] is None:
        print("Entries not found!")
        return -1

    return entries


def extrapolate_three_entries(d):
    entries = [None, None, None]
    goal = 2020
    filtered = list(filter(lambda x: x < goal + 1, d))
    filtered = sorted(filtered)

    for i in filtered:
        for k in filtered:
            for j in filtered:
                if i + k + j == goal:
                    entries[0] = i
                    entries[1] = k
                    entries[2] = j

    if entries[0] is None:
        print("Entries not found!")
        return -1

    return entries


def main():
    DEBUG = False
    if DEBUG:
        data = read_input("testData")
    else:
        data = read_input("data1")
    entries = extrapolate_entries(data)
    if entries != -1:
        print(f"Found entries : {entries}")
        m1 = 1
        for _ in entries:
            m1 = m1 * _
        print(f"Multiplying them: {m1}")
        entries_tris = extrapolate_three_entries(data)
        print(f"Found entries : {entries_tris}")
        m2 = 1
        for _ in entries_tris:
            m2 = m2 * _
        print(f"Multiplying them: {m2}")
    else:
        print("*** Error ***")


if __name__ == "__main__":
    main()
