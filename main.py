ND = input().split()
n, d = int(ND[0]), int(ND[1])
list = [int(i) for i in input().split()]
reversed_list = list.copy()
reversed_list.reverse()
print(list, reversed_list)
count = 0
for i in range(len(list)):
  if list[i] == d:
    list[i] = 0
    reversed_list[-i-1] = 0
    count += 1
  elif list[i]<d:
    for j in reversed(list):
      if list[j] != 0 and list[i]+list[j] <= d:
        list[i], list[j] = 0, 0
        count+=1

print(count)