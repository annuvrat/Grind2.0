
arr= [2,5,23,25]


def isSorted(arr):
    n =len(arr)
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            return False
        

    

    return True


print(isSorted(arr))
