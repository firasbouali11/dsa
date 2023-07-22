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


if __name__ == "__main__":
    arr = [1,1,2,3,5,1,9,8,5,22,2,2,2]
    n = len(arr)
    print(hashTable(arr,n,1))
    print(mapTable(arr,n,5))