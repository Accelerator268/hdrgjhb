import random


list = []
for i in range(7):
    for j in range(i, 7):
        list.append([i, j])
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
if len(player_pieces) == 6:
    status = 'player'
else:
    status = 'computer'
print('{} {piece}'.format('Stock pieces:', piece=stock_pieces))
print('{} {piece}'.format('Player pieces:', piece=player_pieces))
print('{} {piece}'.format('Computer pieces:', piece=computer_pieces))
print('{} {domino}'.format('Domino snake:', domino=domino_snake))
print('{} {status}'.format('Status:', status=status))