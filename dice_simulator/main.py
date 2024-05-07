from random import randint


def roll_dice() -> int:
    return randint(1, 6)


while True:
    try:
        user_input = input('How many dice would you like to roll?: ')
        if user_input.lower() == 'exit':
            print('Goodbye')
            break
        if int(user_input) <= 0:
            print("Enter a number that's greater than 0")

        print(*[roll_dice() for dice in range(int(user_input))], sep=', ')
    except ValueError:
        print('Please enter a valid number')