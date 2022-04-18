my_dict = {
  1: 'a',
  2: 'b'
}

print(my_dict.items())

rev_dict = {v: k for k, v in my_dict.items()}
print(rev_dict)