import random
def choose_level():
    while True:
        levels = input(' enter to level: ')

        if levels == 'easy':
            return 9
        elif levels == 'medium':
            return  6
        elif levels == 'hard':
            return 4

def guess_number_game():
    is_win = False
    num = random.randint(1, 100)
    level = choose_level()

    for i in range(level):
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
        if num != guess and i == level - 1:
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
