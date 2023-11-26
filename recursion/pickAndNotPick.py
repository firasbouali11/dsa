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

def oneSubsequenceWithSumK(ss,ds,s,i,k):
    if(i >= len(ss)):
        if s == k:
            print(ds)
            return True
        return False
    # pick
    ds.append(ss[i])
    s+=ss[i]
    if oneSubsequenceWithSumK(ss,ds,s,i+1,k): return True
    ds.pop()
    s-=ss[i]
    #not pick
    if oneSubsequenceWithSumK(ss,ds,s,i+1,k): return True

def countSubsequenceWithSumK(ss,s,i,k,dp):
    if(i >= len(ss)):
        if s == k:
            return 1
        return 0
    if dp[i] != 0:
        return dp[i]
    # pick
    s += ss[i]
    l = dp[i] = countSubsequenceWithSumK(ss,s,i+1,k,dp)
    s -= ss[i]
    #not pick
    r = dp[i] = countSubsequenceWithSumK(ss,s,i+1,k,dp)
    return l+r

def countCombinationSumK(l, i, k, dp):
    if i == len(l): return 0
    if k == 0: return 1
    if dp[i][k] != 0:
        return dp[i][k]
    s = 0 
    if k - l[i] >= 0:
        s = countCombinationSumK(l, i, k - l[i], dp)
    r = countCombinationSumK(l, i+1, k, dp)
    dp[i][k] = s+r
    return dp[i][k]


arr = [1,5,6,8,9,7,3,3]
dp = [0] * len(arr)
print(countSubsequenceWithSumK(arr,0,0,9,dp))


arr2 = [1,2]
k = 3
dp = [[0] * len(range(k+1)) for _ in range(len(arr2) + 1)]
x = countCombinationSumK(arr2, 0, k, dp)
print(x)