x = 4
k = 3

#division by 2**k
res = x >> k

#multiplication by 2**k
res = x << k

#check if x is a power of 2 
res = (x & (x-1)) == 0

#check if x is odd (== 0 for even)
res = (x & 1) == 1

#check if the kth bit is set
res = (x & (1 << k)) != 0

#clear the kth bit
res = x & ~(1 << k)

#set the kth bit
res = x | (1 << k)

#toggle the kth bit
res = x ^ (1 << k)

#clear the last bit (rightmost)
res = x & (x - 1)

#return the last set bit
res = (x & (x-1)) ^ x

def countSetBits(x):
    count = 0
    while x > 0:
        count += (x & 1)
        x >>= 1
    return count 

def countSetBitsV2(x):
    count = 0
    while x != 0:
        x = x & (x-1)
        count += 1
    return count

def singleNumber2Buckets(l):
    ones = 0
    twos = 0
    for e in l:
        ones = (ones ^ e) & ~twos # add to ones if not in twos or delete from ones if in twos
        twos = (twos ^ e) & ~ones # add to twos if it got deleted from ones
    return ones

def singleNumber3Buckets(l):
    x = 0
    for e in l: x ^= e
    b1 = 0
    b2 = 0
    last = (x & (x-1)) ^ x
    for e in l:
        if e & last == 0:
            b1 ^= e
        else:
            b2 ^= e
    return b1, b2