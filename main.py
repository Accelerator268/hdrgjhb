def our_decor(func):
  def wrapper(arg_for_func):
    return func(arg_for_func), '$'
  return wrapper


@our_decor
def greet(name):
  return 90


print(greet('John'))