nums = [3,0,1,4,5,6,7,8,9]


def missingNumber(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    print(expected_sum)
    actual_sum = sum(nums)
    print(actual_sum)
    return expected_sum - actual_sum


print(missingNumber(nums))
    