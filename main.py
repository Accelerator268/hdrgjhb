class LessThanError(Exception):
    def __str__(self):
        return 'There is an error!'


x = 100
if x < 101:
    raise LessThanError