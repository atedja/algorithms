solutions = {}

def solve(s, bins):
    if s == 0:
        return []

    # return results if it's already calculated
    key = str(bins)
    if s in solutions and key in solutions[s]:
        return solutions[s][key]

    if not s in solutions:
        solutions[s] = {}

    solution = []
    for i, b in enumerate(bins):
        if b <= s:
            cb = bins.copy()
            del cb[i]

            other_sol = solve(s-b, cb)
            sol = [b]
            for os in other_sol:
                sol2 = sol + os
                if sum(sol2) == s:
                    solution.append(sol2)

            if sum(sol) == s:
                solution.append(sol)

    # remove permutations
    uniq = {}
    for sol in solution:
        sol.sort()
        uniq[str(sol)] = sol
    solution = list(uniq.values())

    # store results
    if len(solution) == 0:
        solutions[s][key] = [[]]
    else:
        solutions[s][key] = solution

    return solutions[s][key]

    
bins = [1, 1, 3, 4, 5, 6]
size = 9
solve(size, bins.copy())
print(solutions)
