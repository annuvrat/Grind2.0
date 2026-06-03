s = "bananaeioouu"


def CountVowel(s:str):
  counts = {}
  vowels= {}
  vowel = "aeoui"
  vowelCount = 0

    
  for num in s:
    if num not in  counts:
      counts[num] = 0

    counts[num]+= 1

  for num,i in counts.items():
    if num in vowel:
        vowels[num] = i
        vowelCount+=i

  return vowelCount if vowelCount>0 else False
    



print(CountVowel(s))
