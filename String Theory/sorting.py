def qsort(a):
    print (a)
    if len(a) == 0:
        return ''

    if len(a) == 1:
        return str(a[0])

    q = a[0]
    a_less = [elem for elem in a[1:] if elem < q]
    a_greater = [elem for elem in a[1:] if elem >= q]

    a_less = qsort(a_less)
    a_greater = qsort(a_greater)

    return a_less.strip() + ' ' + str(q) + ' ' + a_greater.strip()

def mergearray(a, b):
    i = 0
    j = 0
    # print (a)
    # print (b)
    n = len(a)
    m = len(b)
    output = []
    while i<n or j<m:
        if i >= n:
            output.append(b[j])
            j = j + 1
        elif j >= m:
            output.append(a[i])
            i = i + 1
        elif a[i] <= b[j]:
            output.append(a[i])
            i = i + 1
        else:
            output.append(b[j])
            j = j + 1
    return output
    # print (output)


def mergesort(a):
    print (a)
    length = len(a)
    if length == 0:
        return []
    if length == 1:
        return a

    median = int((length+1)/2)
    a_first = mergesort([a[i] for i in range(0, median)])
    a_second = mergesort([a[i] for i in range(median, length)])
    # print ("Merging now")
    # print (a_first)
    # print (a_second)
    return mergearray(a_first, a_second)


a = [15, 14, 13, 12, 11, 10, 9, 8, 7]
print (qsort(a).strip())
print (mergesort(a))