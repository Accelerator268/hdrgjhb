import random


list = [[i, j] for i in range(7) for j in range(i, 7)]
domino_snake = []
while ([6, 6] not in domino_snake) and ([5, 5] not in domino_snake):
    stock_pieces, computer_pieces, player_pieces = list.copy(), [], []
    for _ in range(7):
        n = random.choice(stock_pieces)
        computer_pieces.append(n)
        stock_pieces.remove(n)
    for _ in range(7):
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
print('{} {piece}'.format('Stock pieces:', piece=stock_pieces))
print('{} {piece}'.format('Player pieces:', piece=player_pieces))
print('{} {piece}'.format('Computer pieces:', piece=computer_pieces))
print('{} {domino}'.format('Domino snake:', domino=domino_snake))
print('{} {status}'.format('Status:', status=status))


print('==============================================================================================================')
print('Stock size: %s\nComputer pieces: %s\n\n\n%s\n' % (len(stock_pieces), len(computer_pieces), domino_snake))
print('{}{}'.format('\n', 'Your pieces:'))
for count, your_pieces in enumerate(player_pieces):
    print(count, your_pieces, sep = ':')
if status == 'computer':
    print('\nStatus: Computer is about to make a move. Press "Enter" to continue\n')
    status = 'player'
elif status == 'player':
    print('\nStatus: It\'s your turn to make a move. Enter your command.\n')
    status = 'computer'