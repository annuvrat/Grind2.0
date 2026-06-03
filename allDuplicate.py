nums = [5, 1,1, 3, 5, 2]


def first_duplicate(nums):
    seen = set()
    result =[]

    for num in nums:
        if num in seen:
            result.append(num)
        seen.add(num)



    return result if result else False


print(first_duplicate(nums))  # Output: 5