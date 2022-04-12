from string import ascii_lowercase
from random import randint

abc = [ascii_lowercase[randint(0, 25)] for i in range(randint(10, 20))]
vowels = ['a', 'e', 'i', 'o', 'u']
print([i for i in abs if i in vowels])