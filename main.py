class NotInBoundsError(Exception):
    def __str__(self):
      return 'There is an error!'


def check_integer(num):
  if 45 < num < 67:
    return num
  else:
    raise NotInBoundsError


def error_handling(num):
  try:
    return check_integer(num)
  except NotInBoundsError:
    return 'There is an error!'

num = 30
print(error_handling(num))