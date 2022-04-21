# digits = 'abc'

import itertools

# lst1, lst2, lst3 = [1, 2], [3, 4], [5, 6]

# # chain


# for num in itertools.chain(lst1, lst2, lst3):
#   print(num)

# # product

# first = ['Hi', 'Bye']
# second = ['Anton', 'Anna']

# my_gen = (opt for i in range(1, 4) for opt in itertools.product(digits, repeat=i))
 

# for opt in my_gen:
#   print(''.join(opt))


# combinations

flowers = ['a1', 'a2', 'a3', 'a4']

my_iter = itertools.combinations(flowers, 3)

for opt in my_iter:
  print(opt)