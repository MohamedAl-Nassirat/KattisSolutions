word="polarbear"
def searcha(word):
  count = 0
  listword = [word]
  for letter in word:
    listword.append(letter)
  for item in listword:
    if item == "a":
      return listword[count:]
    else:
      count+=1
    
print(word)