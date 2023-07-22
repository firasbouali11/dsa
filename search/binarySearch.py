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
    

if __name__ == "__main__":
    arr = [1,5,6,7,8,9,11,15,20]
    ind = binarySearch(arr, 0,len(arr), 11)
    print(ind)