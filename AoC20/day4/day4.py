import string


def read_input(f):
    with open(f, 'r') as file:
        input_lines = [line.strip() for line in file]

    return input_lines


class Passport:
    def __init__(self, byr=None, iyr=None, eyr=None, hgt=None,
                 hcl=None, ecl=None, pid=None, cid=None):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid
        self.valid = False

    def setGlobal(self, f, v):
        if 'ecl' in f:
            self.set_ecl(v)
        elif 'pid' in f:
            self.set_pid(v)
        elif 'eyr' in f:
            self.set_eyr(v)
        elif 'hcl' in f:
            self.set_hcl(v)
        elif 'byr' in f:
            self.set_byr(v)
        elif 'iyr' in f:
            self.set_iyr(v)
        elif 'hgt' in f:
            self.set_hgt(v)
        elif 'cid' in f:
            self.set_cid(v)

    def set_validity(self, validity):
        self.valid = validity

    def set_byr(self, v):
        self.byr = v

    def set_iyr(self, v):
        self.iyr = v

    def set_hgt(self, v):
        self.hgt = v

    def set_ecl(self, v):
        self.ecl = v

    def set_pid(self, v):
        self.pid = v

    def set_cid(self, v):
        self.cid = v

    def set_eyr(self, v):
        self.eyr = v

    def set_hcl(self, v):
        self.hcl = v


def manipulateData(data):
    passportsList = []
    tmp = ''
    # Adding empty string to the end for pattern recognition
    data.append('')

    for d in data:
        if d != '':
            if tmp != '':
                tmp = tmp + " " + d
            else:
                tmp = tmp + d
        else:
            passportsList.append([tmp])
            tmp = ''

    return passportsList


def populate_passports(data):
    passports = []

    for d in data:
        t = d[0].split(" ")
        finalL = []
        p1 = Passport()
        for _ in t:
            finalL.append(_.split(":"))
            for (field, value) in finalL:
                p1.setGlobal(field, value)
        passports.append(p1)

    return passports


def validate_passports(passports):
    valid = 0

    for p in passports:
        fields = vars(p)
        noneFields = 0
        invalidFields = 0
        for (k, v) in fields.items():
            if k == 'cid' or k == 'valid':
                continue
            elif v is None:
                noneFields += 1
            # Strictier second part validity policies
            else:
                if strict_policy_validation(field = k, value = v):
                    continue
                else:
                    invalidFields += 1
        if not noneFields and not invalidFields:
            p.set_validity(True)
            valid += 1

    return valid


def strict_policy_validation(field, value):
    validation = False

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if field == 'byr':
        digits = 0
        for _ in value:
            digits += 1
        if digits == 4 and 1920 <= int(value) <= 2002:
            validation = True

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    elif field == 'iyr':
        digits = 0
        for _ in value:
            digits += 1
        if digits == 4 and 2010 <= int(value) <= 2020:
            validation = True

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    elif field == 'eyr':
        digits = 0
        for _ in value:
            digits += 1
        if digits == 4 and 2020 <= int(value) <= 2030:
            validation = True

    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    elif field == 'hgt':
        digits = []
        height_measuring_system = []
        for _ in value:
            if _.isdigit():
                digits.append(_)
            else:
                height_measuring_system.append(_)

        if len(digits) != 0 and len(height_measuring_system) != 0:
            rebuiltValue = ''
            for _ in digits:
                rebuiltValue = rebuiltValue + "".join(_)

            # cm
            if height_measuring_system[0] == 'c':
                if 150 <= int(rebuiltValue) <= 193:
                    validation = True
            # in
            elif height_measuring_system[0] == 'i':
                if 59 <= int(rebuiltValue) <= 76:
                    validation = True

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    elif field == 'hcl':
        available_digits = string.digits
        available_chars = string.ascii_lowercase[:6]

        if value[0] == '#':
            splitted = value.split('#')
            if len(splitted[1]) == 6:
                for _ in splitted[1]:
                    if _ in available_digits or _ in available_chars:
                        validation = True
                    else:
                        # print(f"Error on {_}")
                        break

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    elif field == 'ecl':
        valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if value in valid_eye_colors:
            validation = True

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    elif field == 'pid':
        if len(value) == 9:
            validation = True

    return validation


def main():
    DEBUG = False
    if DEBUG:
        data = read_input("testData")
    else:
        data = read_input("data4")

    passportList = manipulateData(data)

    passports = populate_passports(passportList)

    valid_passports = validate_passports(passports)
    print(f"Valid passports: {valid_passports}")


if __name__ == "__main__":
    main()
