from random import randint

RANGE: list = [1, 10]


class Game:
    def __init__(self, number_range: list):

        self.range: list = number_range
        self.number: int = randint(self.range[0], self.range[1])
        self.guess = None

        print(f'Guess the number in range from {self.range[0]} to {self.range[1]}')
        self.make_guess()

    def make_guess(self):
        while True:
            try:
                self.guess: int = int(input("Guess: "))
                if self.guess_in_range():
                    if self.check_answer():
                        return True
            except ValueError:
                print('Incorrect value, input supports only numbers')

    def check_answer(self) -> bool:
        if self.guess_in_range():
            if self.guess == self.number:
                print('Correct.')
                return True
            elif self.guess > self.number:
                print('The number is lower.')
                return False
            elif self.guess < self.number:
                print('The number is higher.')
                return False

    def guess_in_range(self) -> bool:
        if self.range[0] <= self.guess <= self.range[1]:
            return True
        else:
            print("Your guess is out of range")
            return False


game = Game(number_range=RANGE)
