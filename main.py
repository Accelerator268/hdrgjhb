n = [int(input()) for i in range(int(input()))]
k = int(input())
new_list = []

leng = len(n)//k
ost = len(n)%k

if k == ost or k+1 == ost:
  for i in range(leng+1):
    new_list.append(n[:leng])
    n = n[leng:]
    if ost > 0:
      new_list[i].append(n.pop(0))
      ost-=1
else:
  leng+=1
  for i in range(leng):
    new_list.append(n[:leng])
    n = n[leng:]
  new_list.append(n)
print(new_list)