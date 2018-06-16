import collections

if __name__ == "__main__":
    n = int(input().strip())
    arr = [''] * n
    for i in range(n):
        arr[i] = input().strip()
        # print(arr[i])
    key, rev, ctype = input().strip().split()
    key = int(key)
    value = collections.defaultdict()
    sort_arr = []
    for i in range(n):
        key_val = arr[i].split()[key - 1]
        # if '68077' in key_val:
        #     print ("i: " + key_val)
        if ctype == 'numeric':
            key_val = int(key_val)
        else:
            key_val = key_val
        if key_val in value:
            value[key_val].append(arr[i])
        else:
            value[key_val] = [arr[i]]
            sort_arr.append(key_val)
    if ctype == 'numeric':
        sort_arr = sorted(sort_arr)
    else:
        sort_arr = sorted(sort_arr, key=str.lower)
    # print (sort_arr)
    if rev == 'false':
        for i in range(len(sort_arr)):
            key_val = sort_arr[i]
            # print (key_val)
            if len(value[key_val]) > 1:
                # new_arr = sorted(value[key_val], key=str.lower)
                for j in range(len(value[key_val])):
                    print (value[key_val][j])
            else:
                print (value[key_val][0])
    else:
        for i in range(len(sort_arr) - 1, -1, -1):
            key_val = sort_arr[i]
            # print (key_val)
            if len(value[key_val]) > 1:
                # new_arr = sorted(value[key_val], key=str.lower)
                for j in range(len(value[key_val]) -1, -1, -1):
                    print (value[key_val][j])
            else:
                print (value[key_val][0])
                
    
