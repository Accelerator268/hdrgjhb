from time import perf_counter


n = int(input())
start = perf_counter()
ending = []
for i in range(1, int(round(n**0.5, 0)+1)):
  if n % i == 0:
    print(i)
    ending.append(n//i)
ending.reverse()
print(*ending, sep = '\n')
end = perf_counter()
print(end-start)