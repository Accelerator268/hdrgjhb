wtT = input().split()
w, t, T = int(wtT[0]), int(wtT[1]), int(wtT[2])
if T%t != 0:
  print((T//t + 1)*w)
else:
  print(T//t * w)