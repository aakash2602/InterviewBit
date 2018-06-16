# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 2.7
    print(S)
    arr = S.strip().split('.')
    arr_new = []
    for i in range(len(arr)):
        arr_new.extend(arr[i].strip().split('?'))
    arr = []
    for i in range(len(arr_new)):
        arr.extend(arr_new[i].strip().split('!'))

    print(arr)
    max = 0
    for i in range(len(arr)):
        print (arr[i])
        count_words = len(arr[i].strip().split())
        print (count_words)
        if count_words > max:
            max = count_words

    return max


if __name__ == "__main__":
    S = "Forget     CVs..Save   time . x x"
    print (solution(S))
