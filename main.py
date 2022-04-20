#B
class DateDelimiterError(Exception):
    def __str__(self):
        return "You should use the '/' sign as a delimiter."


date = input()
if '/' not in date:
    raise DateDelimiterError
else:
    print(date)



#D
class DateDelimiterError(Exception):
    pass


date = input()
if '/' not in date:
    raise DateDelimiterError("You should use the '/' sign as a delimiter.")
else:
    print(date)