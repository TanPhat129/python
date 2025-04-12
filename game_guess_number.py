'''Guess The Number Game:
    - we will generate a random number with the help of randint() function from 1 to 100
    and ask the user to guess it.
    - After every guess, the user will be told if the number is above or below the
    randomly generated number.
    - The user will win if they guess the number maximum five attempts.
    - Ask the user to stop or continue playing again.'''

import random
def guess_number_game():
    is_win = False
    num = random.randint(1, 100)

    for i in range(5):
        guess = int(input('guess a number 1 to 100: '))
        if num == guess:
            print(f'You guessed right! The number {num} is correct.')
            is_win = True
            break
        else:
            if num < guess:
                print(f'The number {guess} is too high.')
            else:
                print(f'The number {guess} is too low.')
        if num != guess and i == 4:
            print(f'correct: {num}')
    return is_win
if __name__ == '__main__':
    count_play = 0
    count_win = 0
    while True:
        count_play += 1
        win = guess_number_game()

        if win:
            count_win += 1

        response = input(' do you want to play again? (y/n) ').lower()
        if response == 'n':
            break

    print(f'So lan choi: {count_play}')
    print(f'So lan win: {count_win}')

