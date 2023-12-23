def hashTable(arr,n,k):
    max_element = max(arr)
    visited = [0 for _ in range(max_element + 1)]
    for i in range(n):
        visited[arr[i]] +=1
    return visited[k]

def mapTable(arr,n,k):
    mpp = {}
    for i in range(n):
        if arr[i] in mpp:
            mpp[arr[i]] +=1
        else: mpp[arr[i]] = 1
    return mpp[k]