# tai or xiu
import random
def game():
    print("Welcome to the game!")
    print('So tien hien co cua ban la 100.000')
    money = 100000
    bet = int(input("How many do you bet? "))

    count_play = 0
    count_win = 0

    while True:
        count_play += 1
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        result = dice_1 + dice_2
        guess = int(input("Guess Tai (1) or Xiu(2) and (5): "))
        if guess == 1:
            guess = 'tai'
        elif guess == 2:
            guess = 'xiu'
        elif guess == 5:
            guess = 5
        if result < 5:
            if guess == 'tai':
                print(f'You win! {dice_1} + {dice_2} = {result}')
                count_win += 1
                money = money + bet
            else:
                print(f'You lose! {dice_1} + {dice_2} = {result}')
                money = money - bet
        elif result == 5:
            if guess == 5:
                print(f'You win! {dice_1} + {dice_2} = {result}')
                money = money + (bet * 3)
                count_win += 1
            else:
                print(f'You lose! {dice_1} + {dice_2} = {result}')
                money = money - bet
        else:
            if guess == 'xiu':
                print(f'You win! {dice_1} + {dice_2} = {result}')
                money = money + bet
                count_win += 1
            else:
                print(f'You lose! {dice_1} + {dice_2} = {result}')
                money = money - bet
        if money <= 0:
            print('Ban da het tien!!!')
            break

        response = input(' do you want to play again? (y/n) ').lower()
        if response == 'n':
            break

    print('Thank you for playing!')
    print(f'So lan da choi la: {count_play}')
    print(f'So lan win la: {count_win}')
    print(f'So tien hien tai cua ban la: {money}')
if __name__ == '__main__':
    game()