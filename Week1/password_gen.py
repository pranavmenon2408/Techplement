import random

SPECIAL_CHARS = [33, 35, 36, 37, 38, 42, 43, 64, 124, 126]

class PassWordGenerator:
    def __init__(self, length:int, upper_case:bool =True, lower_case:bool =True, numbers:bool =True, special_chars:bool=True) -> None:
        self.length = length
        self.password = []
        self.upper_case = upper_case
        self.lower_case = lower_case
        self.numbers = numbers
        self.special_chars = special_chars

    def generate_password(self) -> str:

        '''
        Generates a random password by storing random upper-case, lower-case,
        numbers, special characters using the random library.

        First takes 1 character per each case given as True,
        then inserts 1 character from any case chosen randomly and
        inserted into any position in the list 'self.password' then final list\
        returned in a form of string using join.
        '''

        possible_chars = []
        if self.special_chars:
            possible_chars.append([chr(SPECIAL_CHARS[random.randint(0, len(SPECIAL_CHARS)-1)]) for i in range(1, random.randint(2, self.length))])
        if self.upper_case:
            possible_chars.append([chr(random.randint(65,90)) for i in range(1, random.randint(2, self.length))])
        if self.lower_case:
            possible_chars.append([chr(random.randint(97,122)) for i in range(1, random.randint(2, self.length))])
        if self.numbers:
            possible_chars.append([chr(random.randint(48,57)) for i in range(1, random.randint(2, self.length))])

        self.password = [possible_chars[i][random.randint(0, len(possible_chars[i])-1)] for i in range(len(possible_chars))]

        for i in range(self.length - len(self.password)):
            random_case= random.randint(0, len(possible_chars)-1)
            random_char= possible_chars[random_case][random.randint(0, len(possible_chars[random_case])-1)]
            if self.password.count(random_char) >=2 :
                i-=1
                continue
            self.password.insert(random.randint(0, len(self.password)), random_char)

        return ''.join(self.password)


def main() -> None:
    length = int(input("Enter the length of the password: "))
    upper_case = input("Do you want upper case characters in the password? (y/n): ")
    lower_case = input("Do you want lower case characters in the password? (y/n): ")
    numbers = input("Do you want numbers in the password? (y/n): ")
    special_chars = input("Do you want special characters in the password? (y/n): ")

    upper_case = True if upper_case == 'y' else False
    lower_case = True if lower_case == 'y' else False
    numbers = True if numbers == 'y' else False
    special_chars = True if special_chars == 'y' else False

    password_gen = PassWordGenerator(length, upper_case=upper_case, lower_case=lower_case, numbers=numbers, special_chars=special_chars)
    password = password_gen.generate_password()
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()

