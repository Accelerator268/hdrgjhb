from functools import reduce
from collections import Counter


stock = [[0, 6], [3, 4], [1, 4], [4, 5], [3, 5], [1, 2], [1, 3], [0, 1], [5, 6], [6, 6], [0, 4], [1, 1], [2, 3], [0, 3], [3, 3], [2, 4], [1, 5], [2, 6], [3, 6], [0, 2], [4, 4]]


new_stock = reduce(lambda x, y: x + y, stock)
print(new_stock)


new_new_stock = [item for sublist in stock for item in sublist]
print(new_new_stock)