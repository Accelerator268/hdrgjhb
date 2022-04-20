ND = input().split()
n, d = int(ND[0]), int(ND[1])
list = [int(i) for i in input().split()]
reversed_list = list.copy()
reversed_list.reverse()
count = 0
for i in range(len(list)):
  if list[i] == d:
    list[i] = 0
    reversed_list[-i-1] = 0
    count += 1
  elif list[i]<d:
    for j in range(i, len(reversed_list)):
      if reversed_list[j] != 0 and list[i]+reversed_list[j] <= d:
        list[i], list[-j-1], reversed_list[j], reversed_list[-i-1] = 0, 0, 0, 0
        count+=1

print(count)