import re

def read_input(f):
    with open(f, 'r') as file:
        input_lines = [line.strip() for line in file]

    return input_lines


def extrapolate_bag_data_structure(data):

    bags_data_structure = {}

    for r in data:
        other_bags = []
        general_split = r.split(',')
        this_bag = general_split[0].split('contain')[0].replace(" bags", "").strip()
        # print(general_split)
        # print(f"This bag is: {this_bag}")
        for (num, bag) in enumerate(general_split):
            if num == 0:
                other_bags.append(bag.split('contain')[1])
            else:
                other_bags.append(bag)

        # print(f"Other bags: {other_bags}")
        bags_data_structure[this_bag] = other_bags

    return bags_data_structure


def shiny_gold_compliance(data):

    shiny_gold_compliant = 0

    for (k, v) in data.items():
        for other_bags in v:
            s = other_bags.split('bag')[0].strip()
            # print(s)
            value_bag_pair = re.split(r'\s+(?=\d)|(?<=\d)\s+', s)

            print(f"here: {value_bag_pair}")

            if len(value_bag_pair) != 1:
                for _ in data[value_bag_pair[1]]:
                    print(f"this: {_}")
                    if 'shiny gold' in _:
                        print(f"*** gold *** for {value_bag_pair[1]}")
                        shiny_gold_compliant += 1
                    else:
                        if 'bags' in _:
                            _ = _.replace(' bags.', '').strip()
                        else:
                            _ = _.replace(' bag.', '').strip()

                        if 'other' not in _:
                            taken = re.split(r'\s+(?=\d)|(?<=\d)\s+', _)[1]
                            print(f"{taken} for {s}")
                        else:
                            print(f"EMPTY for {s}")

                        # t = (re.split(r'\s+(?=\d)|(?<=\d)\s+', _.strip())[1]).strip('bag')
                        # print(t)
                # print(data[value_bag_pair[1]])
                # print()
        print(f"Finished with: {k}")
        print()

    return shiny_gold_compliant


def main():
    DEBUG = True
    if DEBUG:
        data = read_input("testData")
    else:
        data = read_input("data7")

    bags = extrapolate_bag_data_structure(data)
    shiny_compliant = shiny_gold_compliance(bags)
    print(f"Number of compliant shiny gold bags: {shiny_compliant}")





if __name__ == "__main__":
    main()
