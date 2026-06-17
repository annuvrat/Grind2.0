def merge_sort(arr):
    """
    Sorts an array using merge sort algorithm.
    Time Complexity: O(n log n) in all cases
    Space Complexity: O(n)
    """
    # Base case: if array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide: Find the middle point
    mid = len(arr) // 2
    
    # Conquer: Recursively sort both halves
    left = merge_sort(arr[:mid])   # Sort left half
    right = merge_sort(arr[mid:])  # Sort right half
    
    # Combine: Merge the two sorted halves
    return merge(left, right)


def merge(left, right):
    """
    Merges two sorted arrays into one sorted array
    """
    result = []
    i = j = 0
    
    # Compare elements from left and right arrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements from left array (if any)
    while i < len(left):
        result.append(left[i])
        i += 1
    
    # Add remaining elements from right array (if any)
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result