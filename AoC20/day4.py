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
        for (k, v) in fields.items():
            if k == 'cid' or k == 'valid':
                continue
            elif v is None:
                noneFields += 1
        if not noneFields:
            p.set_validity(True)
            valid += 1

    return valid


def main():
    DEBUG = False
    if DEBUG:
        data = read_input("testData")
    else:
        data = read_input("data4")

    passportList = manipulateData(data)

    # t = ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd']
    # t = passportList[2]

    passports = populate_passports(passportList)

    # Passports data
    # for p in passports:
    #     print(vars(p))

    valid_passports = validate_passports(passports)
    print(f"Valid passports: {valid_passports}")


if __name__ == "__main__":
    main()
