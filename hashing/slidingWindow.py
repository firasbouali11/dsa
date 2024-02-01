#fixed size sliding window
def maxVowels(s, k):
        v = {"a", "e", "i", "o", "u"}
        n = len(s)
        maxi = 0
        for i in range(k):
            if s[i] in v: maxi += 1
        m = maxi
        for i in range(1, n-k+1):
            if s[i-1] in v: maxi-=1
            if s[i+k-1] in v: maxi+=1
            m = max(maxi, m)
        return m

#dynamically sized sliding window
def numSubarraysWithSum(nums, goal):
    def atMost(goal):
        if goal < 0: return 0
        n = len(nums)
        i = s = c = 0
        for j in range(n):
            s += nums[j]
            while s > goal and i < n:
                s -= nums[i]
                i += 1
            if s <= goal:
                c += j-i +1
        return c
    return atMost(goal) - atMost(goal-1)