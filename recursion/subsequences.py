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

def isThereSubsequence(arr,n,k):
    if k == 0: return True
    if n < 0 or k < 0: return False
    l = isThereSubsequence(arr,n-1,k-arr[n])
    r = isThereSubsequence(arr,n-1,k)
    return l or r

def countSubsequenceWithSumK(s,n,k,dp):
    if n == 0:
        if k == 0: return 1
        return 0
    l = countSubsequenceWithSumK(s,n-1,k-s[n],dp)
    r = countSubsequenceWithSumK(s,n-1,k,dp)
    return l+r

def countCombinationSumK(s, n, k, dp):
    if n == 0:
        if k == 0: return 1
        return 0
    l = 0
    if k >= s[n]: l = countCombinationSumK(s, n, k-s[n], dp)
    r = countCombinationSumK(s, n-1, k, dp)
    return l+r

def getAllPermutatons(s, n, visited, ds, res):
    if len(ds) == n:
        res.append(ds[:])
        return
        
    for j in range(n):
        if not visited[j]:
            ds.append(s[j])
            visited[j] = True
            getAllPermutatons(s, n, visited, ds, res)
            visited[j] = False
            ds.pop()

def LIS(arr, i, prev, dp):
    if i == len(arr): return 0
    l = 0
    if dp[i][prev+1] != -1: return dp[i][prev+1]
    if prev == -1 or arr[i] > arr[prev]:
        l = 1 + LIS(arr, i+1, i, dp)
    r = LIS(arr, i+1, prev, dp)
    dp[i][prev+1] = max(l, r)
    return dp[i][prev+1]

def LISTab(arr):
    n = len(arr)
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        for prev in range(n-1, -2, -1):
            l = 0
            if prev == -1 or arr[i] > arr[prev]:
                l = 1 + dp[i+1][i+1]
            r = dp[i+1][prev+1]
            dp[i][prev+1] = max(l, r)
    return dp[0][0]