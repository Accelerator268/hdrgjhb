import random

#для сдвига берем в расчет только положительные числа
move = random.randint(1, 10)
print(move)
a_sorted = [random.randint(0, 10) for _ in range(10)]
a_sorted.sort()
a_new = []
if move > len(a_sorted):
    move %= len(a_sorted)
for i in range(len(a_sorted)):
    a_new.append(a_sorted[i - move])
print('{} {a_sorted}'.format('отсортированный массив:', a_sorted = a_sorted))
print('{} {a_new}'.format('сдвинутый массив:', a_new = a_new))
print('{} {maximum}'.format('максимум массива:', maximum = a_new[move-1]))