# The solution is to first sort the intervals based on the first then second element
# Then we simply iterate each tuple, and for each tuple whose interval overlaps with the current range, we merge that tuple.

def sort_tuples(a, b):
    if a[0] > b[0]:
        return 1
    elif a[0] == b[0]:
        if a[1] > b[1]:
            return 1
        elif a[1] == b[1]:
            return 0
        else:
            return -1
    else:
        return -1

def merge_intervals(intervals):
    intervals.sort(sort_tuples)
    finalIntervals = []
    high = None
    low = None
    for i, t in enumerate(intervals):
        if high == None:
            low = t[0]
            high = t[1]
            continue

        if t[0] < high:
            high = max(high, t[1])
            continue

        finalIntervals.append((low, high))
        low = t[0]
        high = t[1]
    else:
        if low != None and high != None:
            finalIntervals.append((low, high))

    return finalIntervals

print(merge_intervals([(1, 5), (2, 5), (7, 9), (-3, 4)]))
print(merge_intervals([(1, 5), (2, 5), (7, 9), (-3, 4), (3, 8)]))
