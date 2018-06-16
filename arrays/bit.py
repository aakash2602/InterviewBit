# class Solution:
    # @param a : list of integers
    # @param b : integer
    # @return a list of integers
def rotateArray(a, b):
    ret = []
    b = b % len(a)
    print (b)
    for i in range(len(a)):
        print (i)
        if i + b < len(a):
            ret.append(a[i + b])
        else:
            ret.append(a[i - b])
        print (ret)
    return ret


print (rotateArray([ 14, 5, 14, 34, 42, 63, 17, 25, 39, 61, 97, 55, 33, 96, 62, 32, 98, 77, 35 ], 56))