class NegativeSumError(Exception):
    def __str__(self):
        return 'Sum is negative'


a, b = int(input()), int(input())
if a+b < 0:
    raise NegativeSumError
else:
  print(a+b)