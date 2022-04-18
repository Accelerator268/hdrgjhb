a, b = int(input()), int(input())

try:
  print(a/b)
except ZeroDivisionError:
  print('The Error!')