s = "banana"


def charFreq(s):
    counts = {}



    for num in s:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1

    return counts

print(charFreq(s))
