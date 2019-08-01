def two_sum(arr, amount):
    m = {}
    for i, n in enumerate(arr):
        t = amount - n
        if t in m:
            return [m[t], i]
        m[n] = i
    return []

print(two_sum([2, 7, 11, 15], 11))
