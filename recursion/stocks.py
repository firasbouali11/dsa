def sellBuy2(arr, n, i, buy):
    if i == n or (i == n-1 and buy): return 0
    if buy:
        l = -1 * arr[i] + sellBuy2(arr, n, i+1, False)
        r = sellBuy2(arr, n, i+1, True)
        return  max(l, r)
    else:
        l = arr[i] + sellBuy2(arr, n, i+1, True)
        r = sellBuy2(arr, n, i+1, False)
        return max(l, r)
    
def sellBuy1(arr):
    n = len(arr)
    buy = arr[0]
    profit = 0
    for i in range(1, n):
        cost = arr[i] - buy
        profit = max(cost, profit) 
        buy = min(buy, arr[i])        
    return profit
