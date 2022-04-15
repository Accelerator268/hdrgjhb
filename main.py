from time import perf_counter


n = int(input())
start = perf_counter()
i = 2
while i**2 < n+1:
  if n % i == 0 and n != i:
    print(i)
  while n % i == 0:
    n //= i
  i += 1
if n != 1:
  print(n)
end = perf_counter()
print(end - start)
