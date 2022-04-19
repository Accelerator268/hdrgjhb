def sum_with_exceptions(a, b):

  class NegativeSumError(Exception):
    def __str__(self):
      return 'Sum is negative'

  if a+b < 0:
    raise NegativeSumError
  else:
    print(a+b)


a, b = int(input()), int(input())
sum_with_exceptions(a, b)