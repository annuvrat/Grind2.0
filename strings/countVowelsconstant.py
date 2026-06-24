s = "aeoiu"



def countVowCon(s):

 vowels = "aeiouAEIOU"
 const_count  = 0
 vowel_count=0
 for char in s:
  if char in vowels:
   vowel_count+=1
 
  elif char not in vowels:
    const_count+=1


 return const_count,vowel_count

print(countVowCon(s)) 