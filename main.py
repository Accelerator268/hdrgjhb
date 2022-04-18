a, b = int(input()), int(input())

while True:
  try:
    a/b
  except ZeroDivisionError:
    print('Error')
  else:
    print(a/b)
    break
  finally:
    b+=2