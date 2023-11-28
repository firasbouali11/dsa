# longest commom subsequence between 2 strings
def lcs(s,t,i,j,dp):
    if i == -1 or j == -1: return 0
    if dp[i][j] != -1: return dp[i][j]
    if s[i] == t[j]: 
        dp[i][j] = 1 + lcs(s,t,i-1,j-1,dp)
        return dp[i][j]
    l = lcs(s,t,i-1,j,dp)
    r = lcs(s,t,i,j-1,dp)
    dp[i][j] = max(l,r)
    return dp[i][j] 
    
def minimumInsertionToBePlaindrom(s):
    dp = [[-1] * (len(s)) for _ in range(len(s))]
    t = s[::-1]
    n = len(s)-1
    x = lcs(s,t,n,n,dp)
    return n - x + 1

s = "awfasdfw"
print(minimumInsertionToBePlaindrom(s))