def getAllSubsequences(s, ds, i, res):
    if(i >= len(s)):
        res.append(ds[:])
        return
    # pick
    ds.append(s[i])
    getAllSubsequences(s, ds, i+1,res)
    ds.pop()
    #not pick
    getAllSubsequences(s, ds, i+1,res)

    # we can switch the position of pick and not pick 
    return res
    

def subsequenceWithSumK(ss,ds,s,i,k):
    if(i >= len(ss)):
        if s == k:
            print(ds)
        return
    # pick
    ds.append(ss[i])
    s+=ss[i]
    subsequenceWithSumK(ss, ds,s,i+1,k)
    ds.pop()
    s-=ss[i]
    #not pick
    subsequenceWithSumK(ss, ds,s, i+1,k)

def isThereSubsequence(arr,n,k,dp):
    if k == 0: return True
    if n < 0 or k < 0: return False
    if dp[n][k] != -1: return dp[n][k]
    l = isThereSubsequence(arr,n-1,k-arr[n],dp)
    r = isThereSubsequence(arr,n-1,k,dp)
    dp[n][k] = l or r
    return dp[n][k]


def isThereSubsequenceTab(arr, k):
    n = len(arr)
    dp = [[False] * (k+1)] * n
    for i in range(n): dp[i][0] = True 
    for i in range(1, n):
        for j in range(1, k+1):
            l = False
            if j >= arr[i]: l = dp[i-1][j-arr[i]]
            r = dp[i-1][j]
            dp[i][j] = l or r
    return dp[n-1][k]


def countSubsequenceWithSumK(ss,s,i,k,dp):
    if(i >= len(ss)):
        if s == k: return 1
        return 0
    if dp[i] != 0: return dp[i]
    s += ss[i]
    l = dp[i] = countSubsequenceWithSumK(ss,s,i+1,k,dp)
    s -= ss[i]
    r = dp[i] = countSubsequenceWithSumK(ss,s,i+1,k,dp)
    return l+r

def countCombinationSumK(l, i, k, dp):
    if i >= len(l):
        if k == 0: return 1
        return 0
    if dp[i][k] != 0: return dp[i][k]
    s = 0 
    if k - l[i] >= 0:
        s = countCombinationSumK(l, i, k - l[i], dp)
    r = countCombinationSumK(l, i+1, k, dp)
    dp[i][k] = s+r
    return dp[i][k]