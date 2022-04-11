import random

list = [[0, 0], [0, 1], [0, 2], [0, 3],[0, 4], [0, 5], [0, 6], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 3], [3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 5], [5, 6], [6, 6]]
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
print('{} {piece}'.format('Stock pieces:', piece=stock_pieces))
print('{} {piece}'.format('Player pieces:', piece=player_pieces))
print('{} {piece}'.format('Computer pieces:', piece=computer_pieces))
print('{} {domino}'.format('Domino snake:', domino=domino_snake))