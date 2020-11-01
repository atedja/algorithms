def longest_substring(s):
    """
    Finds the longest non-overlapping repeating substring in string s.
    Returns the substring, and array of indices where the substring occurs.
    """

    n = len(s)
    dp = [[0 for x in range(n+1)]
            for y in range(n+1)]

    ind = 0
    longest = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if (s[i-1] == s[j-1] and dp[i-1][j-1] < (j-i)):
                dp[i][j] = dp[i-1][j-1] + 1
                if (dp[i][j] > longest):
                    longest = dp[i][j]
                    ind = i
            else:
                dp[i][j] = 0

    return s[ind-longest:ind]


string="aaacaaabaalalaaab"
longest=longest_substring(string)
print(longest)
