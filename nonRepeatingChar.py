s=[4,1,2,1,2]

def firstUniqChar(s):
  counts = {}
  result = []

  for ch in s:
    if ch not in counts:
      counts[ch]= 0
    counts[ch] += 1

  for ch,i in counts.items():
    if i==1:
      result.append(ch)


  return str(result)



print(firstUniqChar(s))
