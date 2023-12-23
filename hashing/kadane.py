#get the subarray with maximum sum
def kadane(arr):
    s = 0
    maxx = arr[0]
    first = 0
    last = 0
    for i in range(len(arr)):
        s += arr[i]
        if s > maxx:
            maxx = s
            last = i
        if s < 0: 
            s = 0
            first = i+1
    return s, arr[first: last]
