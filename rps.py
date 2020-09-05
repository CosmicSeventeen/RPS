from random import randint
t = ['rock', 'paper', 'scissors']
computer = t[randint(0, 2)]
player = False
while player == False:
    player = input('rock, paper, scissors?')
    if player == computer:
        print('tie!')
    elif player == 'rock':
        print('you lose!', computer, 'covers', player)
    else:
        print('you win!', player, 'smashes', computer)
    elif player == 'paper':
        if computer == 'scissors':
            print('you lose!' computer, 'cut' player)
        else:
            print('you win!', player, 'covers', computer)
    elif player == 'scissors'
        if computer == 'rock':
            print('you lose...', computer, 'smashes', player)
    else:
        print("that's not a valid play. check your spelling!")
    player = False
    computer = t[randint(0,2)]