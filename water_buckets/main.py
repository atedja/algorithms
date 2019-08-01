# We are using breadth-first search and iterate all possible sequences using the given buckets
# Once we find the amount we are searching for, return the sequence

def water_buckets(amount, bucket):
    bucket_count = len(bucket)

    # Keeps track of traversed node so we are not visiting the same node again.
    # A dict of bucket values to bool.
    visited = {}

    # Seed first solution with empty buckets
    nb = [0] * bucket_count
    visited[repr(nb)] = True
    q = [[nb]]

    while len(q) > 0:
        current_seq = q.pop(0)
        last_bucket = current_seq[-1][:]

        for i, b in enumerate(bucket):
            # Found what we are searching for
            if amount == last_bucket[i]:
                return current_seq

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

    return None

print(water_buckets(4, [3, 5]))
print(water_buckets(2, [1, 3, 5]))
print(water_buckets(2, [4, 9]))
