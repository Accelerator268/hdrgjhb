from random import randint


months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
revenues = [randint(500, 2000) for _ in range(12)]
profit = ['n/a']
conclusion = ['n\a', 'great', 'decent', 'need follow up', 'critical']

for i in range(1, 12):
  profit.append('%.1f' % ((revenues[i] - revenues[i-1])*100/revenues[i]))

for i in range(12):
  print(months[i], revenues[i], profit[i], end = '')
  if i == 0:
    print(conclusion[0])
  elif revenues[i]/revenues[i-1] > 1.5:
    print('%', conclusion[1])
  elif 1.5 >= revenues[i]/revenues[i-1] >= 1.25:
    print('%', conclusion[2])
  elif 1.25 > revenues[i]/revenues[i-1] >= 1:
    print('%', conclusion[3])
  elif revenues[i]/revenues[i-1] < 1:
    print('%', conclusion[4])