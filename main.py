text = '''I've become so numb
I can't feel you there
Become so tired
So much more aware
I'm becoming this
All I want to do
Is be more like me
And be less like you
And I know
I may end up failing too
But I know
You were just like me with someone disappointed in you'''

text_list = text.split()

# set default method

freq_dict = {}


from collections import defaultdict, Counter

  
freq_dict = defaultdict(int)

for word in text_list:
  freq_dict[word] += 1

print(freq_dict['python'])

freq_counter = Counter(text_list)
print(freq_counter.most_common(10))