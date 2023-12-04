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