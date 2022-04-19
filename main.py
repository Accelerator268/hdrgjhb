def my_decor1(func):
  def wrapper(argforfunc):
    print('It is amazing see you here!')
    return func(argforfunc)
  return wrapper


@my_decor1
def greet(name):
  return f'Hello, {name}!!'

print(greet('John'))

# string decorator2

def my_decor2(func):
  def wrapper(*argsforfunc):
    return ' '.join((func(*argsforfunc), 'RUB'))
  return wrapper


@my_decor2
def calculate(a, b):
  return str(a // b)

print(calculate(1000, 25))