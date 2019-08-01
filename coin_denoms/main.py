# Using memoization to store previous optimal solutions
solutions = {}
solutions[0] = []

def change(amount, denoms):
    if amount in solutions: return solutions[amount]

    # gather all possible ways, then select the one with the shortest length
    sols = []
    for d in denoms:
        if d <= amount:
            sols.append([d] + change(amount-d, denoms))
    sols = sorted(sols, key=len)
    solutions[amount] = sols[0]

    return solutions[amount]

print(change(42, [10, 8, 5, 1]))
