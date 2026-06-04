nums1 = [1,2,2,1]
nums2 = [2,2]


def intersection(nums1, nums2):
    counts = {}
    result = []
    for num in nums1:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1

    for num in nums2:
        if num in counts and counts[num] > 0:
            result.append(num)
            counts[num] -= 1

    return result

print(intersection(nums1, nums2))

