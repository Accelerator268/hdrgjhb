# def exampleexceptions1(x, y):
#   if y == 0:
#     raise ZeroDivisionError('the dem is 0')
#   elif y < 0:
#     raise Exception('the dom is neg')
#   else:
#     print(x / y)

# exampleexceptions1(10, 5)


class OutOfBoundsException(Exception):
    def _init_(self, x):
      self.message = f'{x} can not be processed'
      super()._init_(self.message)


def exampleexceptions4(x):
    try:
        if 3 < x < 30:
            raise OutOfBoundsException(x)
        else:
            print(x)
    except OutOfBoundsException as err:
        print(err)



exampleexceptions4(10)