from string import digits


class NotWordError(Exception):
    def __init__(self, word):
      self.word = word
      self.massage = f'\"{word}\" is not a word, sorry!'
      super().__init__(self.massage)
    


def check_word(word):
  for i in range(len(word)):
    if word[i] in digits:
      raise NotWordError(word)
  else:
    return word


def error_handling(word):
  try:
    return check_word(word)
  except NotWordError:
    return word

word = input()
print(error_handling(word))