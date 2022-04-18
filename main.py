import sys


try:
  a = int(input())
  b = int(input())
  print(a/b, c)
except ZeroDivisionError:
  e_type, e_object, e_traceback = sys.exc_info()
  print('ZeroDivisionError exception on line', e_traceback.tb_lineno, end = '!')
except NameError as err:
  e_type, e_object, e_traceback = sys.exc_info()
  print('NameError exception on line', e_traceback.tb_lineno, end = '!')
except ValueError as err:
  e_type, e_object, e_traceback = sys.exc_info()
  print('ValueError exception on line', e_traceback.tb_lineno, end = '!')
