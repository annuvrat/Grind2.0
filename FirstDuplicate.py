nums = "abca"


def first_duplicate(nums):
    seen = set()
    

    for num in nums:
        if num in seen:
            return  str(num)
        seen.add(num)



    return False


print(first_duplicate(nums))  # Output: 5