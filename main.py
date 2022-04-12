from random import randint


months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'April', 'September', 'October', 'November', 'December']
revenues = [randint(500, 2000) for _ in range(12)]
profit = ['n/a']
conclusion = ['n\a', 'great', 'decent', 'need follow up', 'critical']

for i in range(1, 12):
  profit.append((revenues(i) - revenues(i-1))/revenues(i)*100)

