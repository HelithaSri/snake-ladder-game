import random

board = {
    3: 22, 5: 8, 17: 4, 19: 7, 20: 29, 21: 9, 27: 1
}

p1 = 0
p2 = 0
winning = 30

def role_dice():
    return random.randint(1, 6)


def move_player(player, value):
    global p1
    global p2

    if player == 1:
        p1 = p1 + value
        if p1 in board:
            p1 = board[p1]
    else:
        p2 = p2 + value
        if p2 in board:
            p2 = board[p2]


while True:
    input("Player 1 turn, Press enter to roll the dice.")
    role_value = role_dice()
    print("Player 1 rolled a ", role_value)
    move_player(1, role_value)
    print("Player 1 is now  ", p1)
    if p1 >= winning:
        print("Player 1 is Wins")
        break

    input("Player 2 turn, Press enter to roll the dice.")
    role_value = role_dice()
    print("Player 2 rolled a ", role_value)
    move_player(2, role_value)
    print("Player 2 is now  ", p2)
    if p2 >= winning:
        print("Player 2 is Wins")
        break