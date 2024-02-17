def binarySearch(arr, l, h, k):
    mid = (l + h) // 2
    if(l <= h):
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            return binarySearch(arr, l, mid, k)
        else:
            return binarySearch(arr, mid, h, k)
    else: return -1

def binarySearchTab(arr, k):
    l = 0
    h = len(arr) - 1
    while(l <= h):
        mid = (l+h)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            h = mid - 1
        else:
            l = mid + 1 
    return -1

def lowerBound(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] >= target:
            r = mid - 1
        else:
            l = mid + 1
    return l
      
def upperBound(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return l

def LIS(arr):
    n = len(arr)
    res = [arr[0]]
    for i in range(1, n):
        if arr[i] > res[-1]:
            res.append(arr[i])
        else:
            ind = lowerBound(res, arr[i])
            res[ind] = arr[i]
    return len(res)