def hashList(arr,n,k):
    max_element = max(arr)
    count = [0] * (max_element+1)
    for i in range(n):
        count[arr[i]] +=1
    return count[k]

def hashMap(arr,n,k):
    count = {}
    for i in range(n):
        if arr[i] in count:
            count[arr[i]] +=1
        else: count[arr[i]] = 1
        # or we can use instead of if else: count[arr[i]] = count.get(arr[i], 0) + 1
    return count[k]