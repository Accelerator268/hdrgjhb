# # map

  

nums = [n for n in range(10)]
# # # double_n = [n * 2 for n in nums]
# # print(nums)
# # # print(double_n)

# # def doubler(x):
# #   return x * 2

# # double_numbers = list(map(doubler, nums))
# # print(double_numbers)

# # a, b = map(int, (input(), input()))
# # print(a, b)


# double_numbers = list(map(lambda x: x * 2, nums))

# print(double_numbers)


# x_list = [1, 2, 4]
# y_list = [4, 6, 8]
# z_list = [9, 10, 10]

# res = list(map(lambda x, y, z: x + y + z, x_list, y_list, z_list))
# print(res)

#filter

odd_numbers = list(filter(lambda x: x % 2, nums))
print(odd_numbers)
