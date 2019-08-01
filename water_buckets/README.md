### Problem

Generalized water bucket problem.
Given a desired amount of water and using only N buckets, return the generalized solution to reach the desired amount.

### Example

    amount: 4
    buckets: [3, 5]

    # Notice the order of bucket matters.
    # Fill up 3, transfer 3 to 5, fill up 3, transfer 3 to 5 [1, 5], empty 5, move remaining on 3 to 5 [0, 1], fill up 3, move 3 to 5 to get 4.
    return: [[0, 0], [3, 0], [0, 3], [3, 3], [1, 5], [1, 0], [0, 1], [3, 1], [0, 4]]

    amount: 2
    buckets: [1, 3, 5]
    return: [[0, 0, 0], [0, 3, 0], [1, 2, 0]]
