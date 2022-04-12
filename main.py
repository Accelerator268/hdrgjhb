from string import ascii_lowercase
from random import randint

abc = [ascii_lowercase[randint(0, 25)] for i in range(randint(10, 20))]
vowels = ['a', 'e', 'i', 'o', 'u']
qwerty = list(filter(lambda x: x in vowels, abc))
print(abc)
print(qwerty)

#'y' в расчет не идет, по заданию должно быть 5 гласных