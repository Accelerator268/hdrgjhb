ND = input().split()
n, d = int(ND[0]), int(ND[1])
list = [int(i) for i in input().split()]
count = 0
for i in range(len(list)):
  if list[-1]-4>list[i]:
    for j in range(i+1, len(list)):
      if list[j]-4>=list[i]:
        count+=1
  elif list[-1]-4==list[i]:
    count+=1

print(count)