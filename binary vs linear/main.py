import random


list = [[i, j] for i in range(7) for j in range(i, 7)]
domino_snake = []
while ([6, 6] not in domino_snake) and ([5, 5] not in domino_snake):
import random


list = [[i, j] for i in range(7) for j in range(i, 7)]
domino_snake = []
while ([6, 6] not in domino_snake) and ([5, 5] not in domino_snake):
    stock_pieces, computer_pieces, player_pieces = list.copy(), [], []
    for _ in range(14):
        n = random.choice(stock_pieces)
        computer_pieces.append(n)
        stock_pieces.remove(n)
    for _ in range(14):
        n = random.choice(stock_pieces)
        player_pieces.append(n)
        stock_pieces.remove(n)
    if [6, 6] in computer_pieces:
        domino_snake.append([6, 6])
        computer_pieces.remove([6, 6])
    elif [6, 6] in player_pieces:
        domino_snake.append([6, 6])
        player_pieces.remove([6, 6])
    elif [5, 5] in computer_pieces:
        domino_snake.append([5, 5])
        computer_pieces.remove([5, 5])
    elif [5, 5] in player_pieces:
        domino_snake.append([5, 5])
        player_pieces.remove([5, 5])
if len(player_pieces) < len(computer_pieces):
    status = 'player'
else:
    status = 'computer'
#print('{} {piece}'.format('Stock pieces:', piece=stock_pieces))
#print('{} {piece}'.format('Player pieces:', piece=player_pieces))
#print('{} {piece}'.format('Computer pieces:', piece=computer_pieces))
#print('{} {domino}'.format('Domino snake:', domino=domino_snake))
#print('{} {status}'.format('Status:', status=status))


#print('==============================================================================================================')
#print('Stock size: %s\nComputer pieces: %s\n\n\n%s\n' % (len(stock_pieces), len(computer_pieces), *domino_snake))
#print('{}{}'.format('\n', 'Your pieces:'))
#for count, your_pieces in enumerate(player_pieces):
#    print(count+1, your_pieces, sep = ':')
#if status == 'computer':
#    print('\nStatus: Computer is about to make a move. Press "Enter" to continue\n')
#    status = 'player'
#elif status == 'player':
#    print('\nStatus: It\'s your turn to make a move. Enter your command.\n')
#    status = 'computer'


while len(player_pieces) != 0 and len(computer_pieces) != 0 and status != 'draw':
    print('==============================================================================================================')
    print('Stock size: %s\nComputer pieces: %s\n\n' % (len(stock_pieces), len(computer_pieces)))
    #if len(domino_snake) > 7:
    #    print(*domino_snake[:3], '...', *domino_snake[-3:])
    #else:
    print(*domino_snake)
    print('{}{}'.format('\n\n', 'Your pieces:'))
    for count, your_pieces in enumerate(player_pieces):
        print(count + 1, your_pieces, sep=':')
    if status == 'computer':
        computer_command = input('\nStatus: Computer is about to make a move. Press "Enter" to continue\n')
        status = 'player'
        domino_snake.append(computer_pieces.pop(random.randint(0, len(computer_pieces)-1)))
    elif status == 'player':
        print('\nStatus: It\'s your turn to make a move. Enter your command.\n')
        status = 'computer'
        while True:
            try:
                player_command = int(input())
            except ValueError:
                print('Invalid input')
            else:
                if -len(player_pieces)<= player_command <= len(player_pieces):
                    break
                else:
                    print('Invalid input')
        if player_command == 0:
            player_pieces.append(stock_pieces.pop(random.randint(0, len(stock_pieces))))
        elif 1 <= player_command <= len(player_pieces):
            domino_snake.append(player_pieces.pop(player_command-1))
        elif -1
    count = 0
    
    
    
    
    
    
    

if len(computer_pieces) == 0:
    print('Status: The game is over. Computer won!')
elif len(player_pieces) == 0:
    print('Status: The game is over. You won!')
elif status == 'draw':
    print('Status: The game is over. It\' a draw!')
