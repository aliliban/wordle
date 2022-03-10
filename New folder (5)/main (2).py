from words import words

from random import choice


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

words = words()
words = choice(words)
word = list(words)



l = 0

while l != 6:
  word = list(words)
  l += 1
  user_word = input("enter a 5 letter word\n")

  user_word_len = 0

  for char in user_word:
    user_word_len += 1

  while user_word_len != 5:
    user_word = input("enter a 5 letter word\n")

  user_word = list(user_word)
  n = 0 
  correct = 0
  d = 0
  repeat = ""
  a = 0
  word_check_in = [""]
  
  for i in range(0,5):  

    for i in range(0,5):

      if user_word[n] == word[n]:
        cuser_word = colored(0,255,0, user_word[n])
        user_word[n] = cuser_word
        correct += 1
        word_check_in.append(user_word[n])
        word[n] = ""
    n+=1

  n = 0

  for i in range(0,5):  

    for i in range(0,5):
      
      if user_word[n] in word and user_word[n] != word_check_in:
        cuser_word = colored(100,100,0, user_word[n])
        user_word[n] = cuser_word
        
        

    n += 1

  
  answer =       user_word[0]+user_word[1]+user_word[2]+user_word[3]+user_word[4]

  answer = answer.replace(" ","")

  print(answer)
  

  if correct == 5 and l != 1:
    print("welldone you got it right in",l,"tries")
    l = 6
  if correct == 5 and l == 1:
    print("welldone u got it right in",l,"try")
    l = 6
  

ans = ""
n = 0 

for char in word:
  ans += word[n]
  n+=1

if correct<5:
  print("too bad the word was",ans)