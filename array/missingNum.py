nums=[8, 2, 4, 5, 3, 7, 1]

def missing(nums):
    sortArray = sorted(nums)
    counter = 1

    for num in sortArray:
        if num == counter:
            counter += 1
        else:
            # If num != counter, then counter is missing
            return counter
    
    # If we went through all numbers, the missing one is at the end
    return counter

print(missing(nums))














    