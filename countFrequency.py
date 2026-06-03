nums = [1, 2, 2, 3, 2, 4]


def count_frequency(nums):
    counts = {}


    for num in nums:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1

    return counts

print(count_frequency(nums))  # Output: {1: 1, 2: 3, 3: 1, 4: 1}