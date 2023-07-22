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



arr = [1,5,6,8,9,7,3,3]
dp = [0] * len(arr)
print(countSubsequenceWithSumK(arr,0,0,9,dp))