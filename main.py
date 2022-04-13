def positive(list1):
  return list(filter(lambda x: x>0, list1))


list1 = [1, 2, 3, 4, -5, -9, 0]
print(positive(list1))