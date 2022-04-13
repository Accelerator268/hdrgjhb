def my_product(list1, list2):
  return list(map(lambda x, y: x+y, list1, list2))


list1 = [1, 2, 3, 4]
list2 = [10, 11, 12, 13]
print(my_product(list1, list2))