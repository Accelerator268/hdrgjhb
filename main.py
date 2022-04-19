# READ

# with open('passwords.txt', 'r', encoding='utf-8') as file:
#   print(file.read(4)) #  read 4 bytes
#   print(file.read())  #  read all/rest of bytes in fileif read before like above

# with open('passwords.txt', 'r', encoding='utf-8') as file:
#   print(file.readline(5)) #  read 5 bytes
#   print(file.readline())  #  read all/rest of bytes in line if read before like above

# with open('passwords.txt', 'r', encoding='utf-8') as file:
#   print(file.readlines()) #  returns list
  
# with open('passwords.txt', 'r', encoding='utf-8') as file:
#   for line in file:
#     print(line) #  returns line + \n
#     print(line.strip()) #  returns line


#WRITE
with open('checked.txt', 'w', encoding='utf-8') as file:
  file.write('new entry - check')
  file.write('NEW new entry - check')  # re-write the line above