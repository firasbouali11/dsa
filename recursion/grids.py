def minimumPath(g, i, j, dp):
    if i == 0 or j == 0: return g[0][0] 
    if i<0 or j<0: return 1e9
    if dp[i][j] != -1: return dp[i][j]
    l = minimumPath(g, i-1, j, dp)
    r = minimumPath(g, i, j-1, dp)
    dp[i][j] = g[i][j] + min(l,r)
    return dp[i][j]