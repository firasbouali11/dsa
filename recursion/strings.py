# longest commom subsequence between 2 strings
def lcs(s,t,i,j,dp):
    if i < 0 or j < 0: return 0
    if dp[i][j] != -1: return dp[i][j]
    if s[i] == t[j]: 
        dp[i][j] = 1 + lcs(s,t,i-1,j-1,dp)
        return dp[i][j]
    l = lcs(s,t,i-1,j,dp)
    r = lcs(s,t,i,j-1,dp)
    dp[i][j] = max(l,r)
    return dp[i][j] 

def lcsTab(s, t):
    n = len(s)
    m = len(t)
    dp = [[0] * (m+1)] * (n+1)
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]: 
                dp[i][j] = 1 + dp[i-1][j-1]
            else: 
                l = dp[i-1][j]
                r = dp[i][j-1]
                dp[i][j] = max(l,r)
    return dp[n][m]
    
def minimumInsertionToBePlaindrom(s):
    dp = [[-1] * (len(s)) for _ in range(len(s))]
    t = s[::-1]
    n = len(s)
    # x = lcs(s,t,n-1,n-1,dp)
    x = lcsTab(s,t)
    return n - x

def wildcardMatch(s, pattern, i, j, dp):
    if i < 0 and j>=0: 
        for jj in range(j):
            if pattern[jj] != "*": return False
        return True
    if j < 0 and i >=0: return False
    if i < 0 and j < 0: return True
    if dp[i][j] != -1: return dp[i][j]
    if s[i] == pattern[j]:
        dp[i][j] = wildcardMatch(s, pattern, i-1, j-1, dp)
        return dp[i][j]
    if pattern[j] == "*":
        r = wildcardMatch(s, pattern, i-1, j, dp)
        l = wildcardMatch(s, pattern, i, j-1, dp)
        dp[i][j] =  r or l
        return dp[i][j]
    return False

"""
when converting recursion to tabulation if we have base cases with negative breaks
lets make it a base 1 index recursion and:
    1- write the base case
    2- indicies from 1 -> n
    3- copy paste the recursion
"""
def wildcardMatchTab(s, pattern):
    n = len(s)
    m = len(pattern)
    dp = [[False] * (m+1) for _ in range(n+1)]
    dp[0][0] = True
    for j in range(1,m+1):
        if pattern[j-1] == "*": dp[0][j] = True
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i-1] == pattern[j-1]:
                dp[i][j] = dp[i-1][j-1]
            elif pattern[j-1] == "*":
                r = dp[i-1][j]
                l = dp[i][j-1]
                dp[i][j] =  r or l
    return dp[n][m]