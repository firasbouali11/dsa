def maxCoins(nums):
    n = len(nums)
    nums.append(1)
    nums.insert(0, 1)

    def f(i,n,dp):
        if i > n : return 0
        if dp[i][n] != -1 : return dp[i][n]
        maxi = 0
        for j in range(i, n+1):
            cost = (nums[i-1] * nums[j] * nums[n+1]) + f(i,j-1, dp) + f(j+1,n, dp)
            maxi = max(maxi, cost)
        dp[i][n] = maxi
        return dp[i][n]
    
    dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    return f(1,n,dp)

# Front Partioning
def PalindromPartioning(s, i, n, dp):

    def isPalindrom(s, i, j):
        while i <= j:
            if s[i] != s[j]: return False
            i+=1
            j-=1
        return True

    if i == n: return 0
    mini = 1e9
    if dp[i] != -1: return dp[i]
    for j in range(i, n):
        if isPalindrom(s, i, j):
            cost = 1 + PalindromPartioning(s, j+1, n, dp)
            mini = min(mini, cost)
    dp[i] = mini - 1
    return dp[i]