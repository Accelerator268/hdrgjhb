try:
  print("Hello,", input())
except NameError:
  print("Hello, stranger!")
else:
  print("What a beautiful name you have!")
finally:
  print("Hope to see you soon!")