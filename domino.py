import random


domino_snake = []
while ([6, 6] not in domino_snake) and ([5, 5] not in domino_snake):
    stock_pieces, computer_pieces, player_pieces = [[i, j] for i in range(7) for j in range(i, 7)], [], []
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

player_pieces_negative = player_pieces.copy()
for i in range(len(player_pieces_negative)):
    player_pieces_negative[i] = player_pieces_negative[i][::-1]


computer_pieces_negative = computer_pieces.copy()
for i in range(len(computer_pieces_negative)):
    computer_pieces_negative[i] = computer_pieces_negative[i][::-1]

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

while True:
    try:
        game_mod = int(input('\nSelect game mod:\n1 - Easy\n2 - Normal\n3 - Difficult\n'))
    except ValueError:
        print('Invalid input')
    else:
        if game_mod == 1 or 2 or 3:
            break
        else:
            print('Invalid input')



while len(player_pieces) != 0 and len(computer_pieces) != 0 and status != 'draw' and status != 'computer_disable' and status != 'player_disable':
    print('==============================================================================================================')
    print('Stock size: %s\nComputer pieces: %s\n\n' % (len(stock_pieces), len(computer_pieces)))
    if len(domino_snake) > 7:
        print(*domino_snake[:3], '...', *domino_snake[-3:])
    else:
        print(*domino_snake)
    print('{}{}'.format('\n\n', 'Your pieces:'))
    for count, your_pieces in enumerate(player_pieces):
        print(count + 1, your_pieces, sep=':')


    if status == 'computer':
        print('\nStatus: Computer is about to make a move. Press "Enter" to continue\n')
        while True:
            computer_command = input()
            if computer_command == '':
                break
            else:
                print('Invalid input')
        status = 'player'

        if game_mod == 1:
            while True:
                computer_command = random.randint(-len(computer_pieces), len(computer_pieces))
                if computer_command == 0 and len(stock_pieces) != 0:
                    computer_pieces.append(stock_pieces.pop(random.randint(0, len(stock_pieces)-1)))
                    computer_pieces_negative.append(computer_pieces[-1][::-1])
                    break
                elif 1 <= computer_command <= len(computer_pieces):
                    if domino_snake[-1][-1] == computer_pieces[computer_command-1][0]:
                        domino_snake.append(computer_pieces.pop(computer_command - 1))
                        computer_pieces_negative.remove(computer_pieces_negative[computer_command-1])
                        break
                    elif domino_snake[-1][-1] == computer_pieces_negative[computer_command - 1][0]:
                        domino_snake.append(computer_pieces_negative.pop(computer_command - 1))
                        computer_pieces.remove(computer_pieces[computer_command - 1])
                        break
                elif -1 >= computer_command >= -len(computer_pieces):
                    if domino_snake[0][0] == computer_pieces[abs(computer_command) - 1][1]:
                        domino_snake = [computer_pieces.pop(abs(computer_command) - 1)] + domino_snake
                        computer_pieces_negative.remove(computer_pieces_negative[abs(computer_command) - 1])
                        break
                    elif domino_snake[0][0] == computer_pieces_negative[abs(computer_command) - 1][1]:
                        domino_snake = [computer_pieces_negative.pop(abs(computer_command) - 1)] + domino_snake
                        computer_pieces.remove(computer_pieces[abs(computer_command) - 1])
                        break

        elif game_mod == 3:
            difficult_list = domino_snake.copy() + computer_pieces.copy()
            frequent_list = [0, 0, 0, 0, 0, 0, 0]
            for i in difficult_list:
                frequent_list[i[0]] += 1
                frequent_list[i[-1]] += 1
            max_list = [0 for _ in range(len(computer_pieces))]
            for i in range(len(computer_pieces)):
                max_list[i] = frequent_list[computer_pieces[i][0]] + frequent_list[computer_pieces[i][-1]]
            for i in range(1, len(computer_pieces)+1):
                computer_command = max_list.index(max(max_list))+1
                if domino_snake[-1][-1] == computer_pieces[computer_command - 1][0]:
                    domino_snake.append(computer_pieces.pop(computer_command - 1))
                    computer_pieces_negative.remove(computer_pieces_negative[computer_command - 1])
                    break
                elif domino_snake[-1][-1] == computer_pieces_negative[computer_command - 1][0]:
                    domino_snake.append(computer_pieces_negative.pop(computer_command - 1))
                    computer_pieces.remove(computer_pieces[computer_command - 1])
                    break
                elif domino_snake[0][0] == computer_pieces[abs(computer_command) - 1][1]:
                    domino_snake = [computer_pieces.pop(abs(computer_command) - 1)] + domino_snake
                    computer_pieces_negative.remove(computer_pieces_negative[abs(computer_command) - 1])
                    break
                elif domino_snake[0][0] == computer_pieces_negative[abs(computer_command) - 1][1]:
                    domino_snake = [computer_pieces_negative.pop(abs(computer_command) - 1)] + domino_snake
                    computer_pieces.remove(computer_pieces[abs(computer_command) - 1])
                    break
                max_list[i - 1] = 0
            else:
                if stock_pieces != 0:
                    computer_pieces.append(stock_pieces.pop(random.randint(0, len(stock_pieces) - 1)))
                    computer_pieces_negative.append(computer_pieces[-1][::-1])
                else:
                    status = 'computer_disable'
        elif game_mod == 2:
            game_mod_normal = random.randint(1, 2)
            if game_mod_normal == 1:
                while True:
                    computer_command = random.randint(-len(computer_pieces), len(computer_pieces))
                    if computer_command == 0 and len(stock_pieces) != 0:
                        computer_pieces.append(stock_pieces.pop(random.randint(0, len(stock_pieces) - 1)))
                        computer_pieces_negative.append(computer_pieces[-1][::-1])
                        break
                    elif 1 <= computer_command <= len(computer_pieces):
                        if domino_snake[-1][-1] == computer_pieces[computer_command - 1][0]:
                            domino_snake.append(computer_pieces.pop(computer_command - 1))
                            computer_pieces_negative.remove(computer_pieces_negative[computer_command - 1])
                            break
                        elif domino_snake[-1][-1] == computer_pieces_negative[computer_command - 1][0]:
                            domino_snake.append(computer_pieces_negative.pop(computer_command - 1))
                            computer_pieces.remove(computer_pieces[computer_command - 1])
                            break
                    elif -1 >= computer_command >= -len(computer_pieces):
                        if domino_snake[0][0] == computer_pieces[abs(computer_command) - 1][1]:
                            domino_snake = [computer_pieces.pop(abs(computer_command) - 1)] + domino_snake
                            computer_pieces_negative.remove(computer_pieces_negative[abs(computer_command) - 1])
                            break
                        elif domino_snake[0][0] == computer_pieces_negative[abs(computer_command) - 1][1]:
                            domino_snake = [computer_pieces_negative.pop(abs(computer_command) - 1)] + domino_snake
                            computer_pieces.remove(computer_pieces[abs(computer_command) - 1])
                            break
            elif game_mod_normal == 2:
                difficult_list = domino_snake.copy() + computer_pieces.copy()
                frequent_list = [0, 0, 0, 0, 0, 0, 0]
                for i in difficult_list:
                    frequent_list[i[0]] += 1
                    frequent_list[i[-1]] += 1
                max_list = [0 for _ in range(len(computer_pieces))]
                for i in range(len(computer_pieces)):
                    max_list[i] = frequent_list[computer_pieces[i][0]] + frequent_list[computer_pieces[i][-1]]
                for i in range(1, len(computer_pieces) + 1):
                    computer_command = max_list.index(max(max_list)) + 1
                    if domino_snake[-1][-1] == computer_pieces[computer_command - 1][0]:
                        domino_snake.append(computer_pieces.pop(computer_command - 1))
                        computer_pieces_negative.remove(computer_pieces_negative[computer_command - 1])
                        break
                    elif domino_snake[-1][-1] == computer_pieces_negative[computer_command - 1][0]:
                        domino_snake.append(computer_pieces_negative.pop(computer_command - 1))
                        computer_pieces.remove(computer_pieces[computer_command - 1])
                        break
                    elif domino_snake[0][0] == computer_pieces[abs(computer_command) - 1][1]:
                        domino_snake = [computer_pieces.pop(abs(computer_command) - 1)] + domino_snake
                        computer_pieces_negative.remove(computer_pieces_negative[abs(computer_command) - 1])
                        break
                    elif domino_snake[0][0] == computer_pieces_negative[abs(computer_command) - 1][1]:
                        domino_snake = [computer_pieces_negative.pop(abs(computer_command) - 1)] + domino_snake
                        computer_pieces.remove(computer_pieces[abs(computer_command) - 1])
                        break
                    max_list[i - 1] = 0
                else:
                    if stock_pieces != 0:
                        computer_pieces.append(stock_pieces.pop(random.randint(0, len(stock_pieces) - 1)))
                        computer_pieces_negative.append(computer_pieces[-1][::-1])
                    else:
                        status = 'computer_disable'

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
                    if player_command == 0 and len(stock_pieces) != 0:
                        player_pieces.append(stock_pieces.pop(random.randint(0, len(stock_pieces) - 1)))
                        player_pieces_negative.append(player_pieces[-1][::-1])
                        break
                    elif 1 <= player_command <= len(player_pieces):
                        if domino_snake[-1][-1] == player_pieces[player_command - 1][0]:
                            domino_snake.append(player_pieces.pop(player_command - 1))
                            player_pieces_negative.remove(player_pieces_negative[player_command - 1])
                            break
                        elif domino_snake[-1][-1] == player_pieces_negative[player_command - 1][0]:
                            domino_snake.append(player_pieces_negative.pop(player_command - 1))
                            player_pieces.remove(player_pieces[player_command - 1])
                            break
                        else:
                            print('Invalid input')
                    elif -1 >= player_command >= -len(player_pieces):
                        if domino_snake[0][0] == player_pieces[abs(player_command) - 1][1]:
                            domino_snake = [player_pieces.pop(abs(player_command) - 1)] + domino_snake
                            player_pieces_negative.remove(player_pieces_negative[abs(player_command) - 1])
                            break
                        elif domino_snake[0][0] == player_pieces_negative[abs(player_command) - 1][1]:
                            domino_snake = [player_pieces_negative.pop(abs(player_command) - 1)] + domino_snake
                            player_pieces.remove(player_pieces[abs(player_command) - 1])
                            break
                        else:
                            print('Invalid input')
                else:
                    print('Invalid input')


    if domino_snake[0][0] == domino_snake[-1][-1]:
        count = 0
        possible_draw = domino_snake[0][0]
        for i in range(len(domino_snake)):
            if possible_draw in domino_snake[i]:
                count += 1
            if count == 7:
                status = 'draw'

print(*domino_snake)

if len(computer_pieces) == 0:
    print('\nStatus: The game is over. Computer won!')
elif len(player_pieces) == 0:
    print('\nStatus: The game is over. You won!')
elif status == 'draw':
    print('\nStatus: The game is over. It\' a draw!')