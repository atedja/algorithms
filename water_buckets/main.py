# We are using breadth-first search and iterate all possible sequences using the given buckets
# Once all the solutions have been traversed, we sort them and pick the shortest one

# This ultimately holds the final solution.
# Key is the amount and Value is the sequence.
result = {}

# Keeps track of traversed node so we are not visiting the same node again.
# A dict of bucket values to bool.
visited = {}

def water_buckets(amount, bucket):
    bucket_count = len(bucket)

    # Seed first solution with empty buckets
    nb = [0] * bucket_count
    visited[repr(nb)] = True
    q = [[nb]]
    result[0] = [nb]

    while len(q) > 0:
        current_seq = q.pop(0)
        for i, b in enumerate(bucket):
            last_bucket = current_seq[-1][:]

            # Add current sequence to the result
            # Duplicates are okay, we will sort them later
            if not last_bucket[i] in result:
                result[last_bucket[i]] = []
            result[last_bucket[i]].append(current_seq)

            # Fill up bucket
            if last_bucket[i] < bucket[i]:
                nb = last_bucket[:]
                nb[i] = bucket[i]
                if not repr(nb) in visited:
                    visited[repr(nb)] = True
                    q.append(current_seq + [nb])

            # Dump bucket
            if last_bucket[i] > 0:
                nb = last_bucket[:]
                nb[i] = 0
                if not repr(nb) in visited:
                    visited[repr(nb)] = True
                    q.append(current_seq + [nb])

                # Since bucket not empty, we can dump this bucket to another
                for j, b in enumerate(bucket):
                    if i == j: continue

                    if last_bucket[j] < bucket[j]:
                        diff = min(bucket[j] - last_bucket[j], last_bucket[i])
                        nb = last_bucket[:]
                        nb[i] -= diff
                        nb[j] += diff
                        if not repr(nb) in visited:
                            visited[repr(nb)] = True
                            q.append(current_seq + [nb])

    for v, sols in result.items():
        shortest = sorted(sols, key=len)[0]
        result[v] = shortest

    if amount in result:
        return result[amount]
    else:
        return None

print(water_buckets(4, [1, 3, 5]))
