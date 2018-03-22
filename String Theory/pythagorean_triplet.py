import math

def find_triplet(arr):
    arr = sorted(arr)
    sqr_arr = arr
    arr = [int(math.pow(num, 2)) for num in arr]
    # print (sorted(arr))
    # print (arr.sort())
    print (arr)
    for i in range(len(arr)-1, 1, -1):
        sum = arr[i]
        start = 0
        end = i - 1
        while end > start:
            if sum > arr[start] + arr[end]:
                start = start + 1
            elif sum  < arr[start] + arr[end]:
                end = end - 1
            else:
                print (sqr_arr[start], sqr_arr[end], sqr_arr[i])
                start = start + 1
                end = end - 1

if __name__ == '__main__':
    # arr = input().strip().split()
    arr = [3, 1, 4, 6, 5]
    print (arr)
    # arr = [int(elem) for elem in arr]
    find_triplet(arr)