import numpy as np


class ValidatorCNP:
    def __init__(self, data: str):
        self.__CNP = data

        if (len(data) != 13) or (not isinstance(data, str)):
            raise Exception("Invalid length")

        self.__sex = int(self.__CNP[:1])
        self.__birth_year = int(self.__CNP[1:3])
        self.__birth_month = int(self.__CNP[3:5])
        self.__birth_day = int(self.__CNP[5:7])
        self.__county = int(self.__CNP[7:9])
        self.__unique_id = int(self.__CNP[9:-1])
        self.__end_flag_validator = int(self.__CNP[-1])

        # print(f"__sex: {self.__sex}")
        # print(f"__birth_year: {self.__birth_year}")
        # print(f"__birth_month: {self.__birth_month}")
        # print(f"__birth_day: {self.__birth_day}")
        # print(f"__county: {self.__county}")
        # print(f"__unique_id: {self.__unique_id}")
        # print(f"__end_flag_validator: {self.__end_flag_validator}")

        self.validate()

    @property
    def sex(self):
        SEX_VALUES = {
            1: "M",
            2: "F",
            3: "M",
            4: "F",
            5: "M",
            6: "F",
            7: "M",
            8: "F",
        }
        return SEX_VALUES[self.__sex]

    @property
    def county(self):
        ROMANIA_COUNTIES = {
            "1": "Alba Iulia",
            "2": "Arad",
            "3": "Arges",
            "4": "Bacau",
            "5": "Bihor",
            "6": "Bistrita Nasaud",
            "7": "Botosani",
            "8": "Brasov",
            "9": "Braila",
            "10": "Buzau",
            "11": "Caras Severin",
            "12": "Cluj",
            "13": "Constanta",
            "14": "Covasna",
            "15": "Dambovita",
            "16": "Dolj",
            "17": "Galati",
            "18": "Gorj",
            "19": "Harghita",
            "20": "Hunedoara",
            "21": "Ialomița",
            "22": "Iasi",
            "23": "Ilfov",
            "24": "Maramures",
            "25": "Mehedinti",
            "26": "Mures",
            "27": "Neamt",
            "28": "Olt",
            "29": "Prahova",
            "30": "Satu Mare",
            "31": "Salaj",
            "32": "Sibiu",
            "33": "Suceava",
            "34": "Teleorman",
            "35": "Timis",
            "36": "Tulcea",
            "37": "Vaslui",
            "38": "Valcea",
            "39": "Vrancea",
            "40": "Bucuresti",
            "41": "Bucuresti S.1",
            "42": "Bucuresti S.2",
            "43": "Bucuresti S.3",
            "44": "Bucuresti S.4",
            "45": "Bucuresti S.5",
            "46": "Bucuresti S.6",
            "51": "Calarasi",
            "52": "Giurgiu",
        }
        return ROMANIA_COUNTIES[str(self.__county)]

    def __repr__(self):
        return self.__CNP

    def validate(self):
        if (len(self.__CNP) != 13) or (not isinstance(self.__CNP, str)):
            raise Exception("Invalid length")

        self.validate_birth_year()
        self.validate_birth_month()
        self.validate_birth_day()
        # NOTE: sex has to be tested once dates are also valid since it depends on them
        self.validate_sex()
        self.validate_county()
        self.validate_unique_id()
        self.validate_end_flag_validator()

        # (sex, birth_year, birth_month, birth_day, county, unique_id, end_flag_validator) = self.extract_parameters()

    # def extract_parameters(self):
    #     sex = self.__CNP[:1]
    #     birth_year = self.__CNP[1:3]
    #     birth_month = self.__CNP[3:5]
    #     birth_day = self.__CNP[5:7]
    #     county = self.__CNP[7:9]
    #     unique_id = self.__CNP[9:11]
    #     end_flag_validator = self.__CNP[-1]
    #
    #     return (sex,birth_year, birth_month, birth_day, county, unique_id, end_flag_validator)

    def validate_sex(self):
        if self.__sex < 1 or self.__sex > 9:
            raise Exception("Invalid sex")

        # if self.__sex < 1 or self.__sex > 9:
        #     raise Exception("Invalid sex")
        #
        # if self.__sex == 1 or self.__sex == 2:
        #     if self.__birth_year < 1900 or self.__birth_year > 1999:
        #         raise Exception("Invalid sex")
        #
        # if self.__sex == 3 or self.__sex == 4:
        #     if self.__birth_year < 1800 or self.__birth_year > 1899:
        #         raise Exception("Invalid sex")
        #
        # if self.__sex == 5 or self.__sex == 6:
        #     if self.__birth_year < 2000 or self.__birth_year > 2099:
        #         raise Exception("Invalid sex")

    def validate_birth_year(self):
        if self.__birth_year < 0 or self.__birth_year > 99:
            raise Exception("Invalid birth year")

    def validate_birth_month(self):
        if self.__birth_month < 1 or self.__birth_month > 12:
            raise Exception("Invalid birth month")

    def validate_birth_day(self):
        if self.__birth_day < 0:
            raise Exception("Invalid birth day")

    def validate_county(self):
        if self.__county < 1 or self.__county > 52:
            raise Exception("Invalid county")

    def validate_unique_id(self):
        if self.__unique_id < 1 or self.__unique_id > 999:
            raise Exception("Invalid unique ID")

    def validate_end_flag_validator(self):
        MULTIPLIER = "279146358279"
        # array with each individual number on a sepparate index
        # both should be the same length
        CNP_list = np.array(list(map(lambda x: int(x), list(self.__CNP[:-1]))))
        multiplier_list = np.array(list(map(lambda x: int(x), list(MULTIPLIER))))

        # Function operation that creates a relation from the last CNP value to all other values
        computation_restul = np.dot(CNP_list, multiplier_list) % 11

        validator = 1 if computation_restul == 10 else computation_restul

        # print(f"Validator is: {validator}")
        # print(f"Input flag: {self.__end_flag_validator}")

        if self.__end_flag_validator != validator:
            raise Exception("Control number is invalid")


if __name__ == "__main__":
    CNP = ValidatorCNP('5010715070070')
    print(f"CNP is: {CNP}")
    print(CNP.sex)
    print(CNP.county)
