def check_w_letter(a, b):

  class NegativeSumError(Exception):
    def __str__(self):
      return 'This is your Exception message!'

  if b in a:
    raise NegativeSumError
  else:
    print(a)


a, b = input(), input()
check_w_letter(a, b)