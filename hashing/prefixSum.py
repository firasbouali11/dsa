def prefixSum(arr):
    prefix = [0 for _ in range(len(arr))]
    prefix[0] = arr[0]
    for i in range(1,len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
    print(prefix)

def longestSubArray(arr, k):
    # the map will contain (sum -> index)
    prefix = {}
    s = 0
    maxx = 0
    for i in range(len(arr)):
        s += arr[i]
        if s == k:
            maxx = max(maxx, i+1)
        if s-k in prefix:
            maxx = max(maxx, i - prefix[s-k])
        if s not in prefix:
            prefix[s] = i
    return maxx

def countSubArray(arr,k):
    prefix = {0:1}
    s = 0
    count = 0
    for i in range(len(arr)):
        s += arr[i]
        if s-k in prefix:
            count += prefix[s-k]
        if s in prefix:
            prefix[s] = prefix[s] + 1
        else: prefix[s] = 1
    return count
    

arr = [1,5,6,1,1,1,3,0,-1]
print(countSubArray(arr, 3))