xyz1 = ', '.join(input().split())
xyz2 = ', '.join(input().split())
print('v1 = (', xyz1, ') & v2 = (', xyz2, ')', sep = '')
xyz1 = xyz1.split(', ')
xyz2 = xyz2.split(', ')
for xy, xz in zip(xyz1, xyz2):
  print(int(xy) + int(xz))