n=5
arr1 =[1,2,3,4,6]

arr2 = [1,2,4,5,6]
m=5


def Union(arr1,arr2,n,m):
    result = []
    for num in arr1:
        if num not in result:
            result.append(num)
    
    # Add all elements from arr2
    for num in arr2:
        if num not in result:
            result.append(num)
    
    # Sort the result
    return sorted(result)


print(Union(arr1,arr2,n,m))


