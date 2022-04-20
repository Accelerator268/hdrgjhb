from string import digits


class NotWordError(Exception):
    def __init__(self, word):
        self.message = f'%s is not a word, sorry!' % word
        super().__init__(self.message)


def check_word(word):
    for i in range(len(word)):
        if word[i] in digits:
            raise NotWordError(word)  # raise only once!!!
    return word


def error_handling(word):
    try:
        print(check_word(word))   # print positive
    except NotWordError as err:
        print(err)                # print negative not raise again :)))


word = input()
error_handling(word)