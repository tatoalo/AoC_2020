def read_input(f):
    with open(f, 'r') as file:
        input_lines = [line.strip() for line in file]

    return input_lines


def extrapolate_positive_responses(data):
    data.append("")
    positive_responses = []

    yes_response = []
    for d in data:
        if d not in yes_response and d != '':
            yes_response.append(d)
        elif d == '':
            # print(f"Found these positive responses: {yes_response}")
            positive_responses.append(yes_response)
            yes_response = []
            continue

    return positive_responses


def count_positive_responses(responses):
    pos = 0
    for r in responses:
        tmp_pos = []
        if len(r) == 1:
            # print(f"Adding {len(r[0])} for {r}")
            pos += len(r[0])
        else:
            for inner_single_partecipant in r:
                if len(inner_single_partecipant) != 1:
                    for inner_single_response in inner_single_partecipant:
                        if inner_single_response not in tmp_pos:
                            tmp_pos.append(inner_single_response)
                else:
                    if inner_single_partecipant not in tmp_pos:
                        tmp_pos.append(inner_single_partecipant)
            # print(f"Adding {len(tmp_pos)} for {tmp_pos}")
            pos += len(tmp_pos)
            tmp_pos = []

    return pos


# Part 2 policy enforcement
def count_positive_responses_everyone_policy(responses):
    pos = 0

    for group in responses:
        if len(group) == 1:
            # print(f"Adding {len(group[0])} for {group}")
            pos += len(group[0])
        else:
            common_responses = []
            for single_response in group:
                if len(single_response) == 1:
                    if len(common_responses) == 0:
                        common_responses.append(single_response)
                    elif single_response not in common_responses:
                        break

                else:
                    pos += corner_case(group)
                    break

    return pos


def corner_case(group):
    # print("***")
    # print(f"corner case for {group}")
    pos_found = 0
    all_responses = []
    target_quorum = len(group)

    for single_response in group:
        for inner in single_response:
            all_responses.append(inner)

    # Calculating occurrences
    occurrences = [[x, all_responses.count(x)] for x in set(all_responses)]
    for elem, val in occurrences:
        if val == target_quorum:
            # print(f"found {elem} with {val}")
            pos_found += 1

    # print("***")
    return pos_found


def main():
    DEBUG = False
    if DEBUG:
        data = read_input("testData")
    else:
        data = read_input("data6")

    positive_responses = extrapolate_positive_responses(data)
    print(f"Positive responses: {positive_responses}")
    print(f"Number of unique positive responses (OLD POLICY): {count_positive_responses(positive_responses)}")
    print(f"Number of unique positive responses (NEW POLICY): {count_positive_responses_everyone_policy(positive_responses)}")


if __name__ == "__main__":
    main()
