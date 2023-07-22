def merge(arr, l, mid, h):
    res = []
    i = l
    j = mid + 1
    while i <= mid and j < h:
        if arr[i] > arr[j]:
            res.append(arr[j])
            j+=1
        else:
            res.append(arr[i])
            i+=1
    while(i <= mid):
        res.append(arr[i])
        i+=1
    while(j < h):
        res.append(arr[j])
        j+=1
    for i in range(l,h):
        arr[i] = res[i - l]


def mergeSort(arr, l, h):
    if l == h: return
    mid = (l+h) // 2
    mergeSort(arr, l, mid)
    mergeSort(arr, mid+1, h)
    merge(arr, l, mid, h)

if __name__ == "__main__":
    arr = [1,2,5,3,6]
    mergeSort(arr, 0, len(arr))
    print(arr)