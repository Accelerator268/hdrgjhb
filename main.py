num = [i for i in range(10)]
even = list(filter(lambda x: x%2==0, num))
odd = list(filter(lambda x: x%2, num))

my_sum = 0
i = 0
my_sum = list(map(lambda x, y: x + y, even, odd))

reminders = list(map(lambda x: x%3, my_sum))

nonzero_reminders = list(filter(lambda x: x, reminders))

print(nonzero_reminders)