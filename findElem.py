arr=[1,2,3,4,5]
k=2

def findNumber(arr, k):
  for num in arr:
    if num==k:
        return "YES"
        
  return "NO"


print(findNumber(arr,k))