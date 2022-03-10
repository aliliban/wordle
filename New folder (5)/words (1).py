def words():
  with open("wordle-answers-alphabetical.txt", "r") as   a_file:
    content = a_file.readlines()
    n = 0
    words = []
    for line in content:
      words.insert(n, content[n])
      for line in content:
        word = words[n]
        word = word.replace("\n","")
        words[n] = word
      n += 1
    return words

def words_real_check():
  with open("wordle-allowed-guesses.txt", "r") as   a_file:
    content = a_file.readlines()
    n = 0
    words = []
    for line in content:
      words.insert(n, content[n])
      for line in content:
        word = words[n]
        word = word.replace("\n","")
        words[n] = word
      n += 1
    return words