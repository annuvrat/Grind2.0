arr = [12,34,35,46346]
revers= arr[::-1]
print(revers)
result = []
for  i in range(len(arr)-1,-1,-1):
   result.append(arr[i])


print(result)