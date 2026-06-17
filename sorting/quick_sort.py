def quick_sort(arr):
    # If array has 1 or 0 items, it's already sorted!
    if len(arr) <= 1:
        return arr
    
    # Step 1: Pick a pivot (I'll pick the middle element)
    pivot = arr[len(arr) // 2]
    
    # Step 2: Create 3 empty lists
    left = []    # For numbers smaller than pivot
    middle = []  # For numbers equal to pivot
    right = []   # For numbers greater than pivot
    
    # Step 3: Put each number in the right list
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            middle.append(num)
        else:  # num > pivot
            right.append(num)
    
    # Step 4: Recursively sort left and right, then combine!
    return quick_sort(left) + middle + quick_sort(right)