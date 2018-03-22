def match_greater(a, b):
    if (ord(a) > ord(b)):
        return True
    else:
        return False

def match_lesser(a, b):
    if (ord(a) < ord(b)):
        return True
    else:
        return False

def match_equal(a, b):
    if (ord(a) == ord(b)):
        return True
    else:
        return False

t = int(input().strip())
for i in range(t):
    first = input().strip() + "z"
    second = input().strip() + "z"
    len_first = len(first)
    #     first = [ord(first[i]) for i in range(len_first)]
    len_second = len(second)
    #     second = [ord(second[i]) for i in range(len_second)]
    i = 0
    j = 0
    output = ''
    while i < len_first or j < len_second:
        if i >= len_first:
            output = output + second[j]
            # print("1")
            j = j + 1
        elif j >= len_second:
            output = output + first[i]
            # print("2")
            i = i + 1
        elif match_lesser(first[i], second[j]):
            # print("3")
        # elif ord(first[i]) < ord(second[j]):
            output = output + first[i]
            i = i + 1
        elif match_greater(first[i], second[j]):
            # print("4")
        # elif ord(first[i]) > ord(second[j]):
            output = output + second[j]
            j = j + 1
        elif match_equal(first[i], second[j]):
        # elif ord(first[i]) == ord(second[j]):
            intd_f = first[i]
            f_lock = 0
            intd_s = second[j]
            s_lock = 0
            i_add = 1
            mode = 0
            min_f = intd_f
            min_s = intd_s
            count = 0
            i_before = 0
            all_same = 1
            while True:
                print (i_add)
                if i + i_add < len_first:
                    print (first[i + i_add])
                    print (i)
                if j + i_add < len_second:
                    print(second[j + i_add])
                    print (j)
                if i + i_add >= len_first:
                    # print ("5")
                    # mode = 0
                    output = output + intd_f
                    i = i + len(intd_f)
                    break
                elif j + i_add >= len_second:
                    # print("6")
                    # mode = 1
                    output = output + intd_s
                    j = j + len(intd_s)
                    break
                elif ord(first[i+i_add]) < ord(second[j+i_add]):
                    # print("7")
                    # intd_f = intd_f + first[i + i_add]
                    # mode = 0
                    output = output + intd_f
                    i = i + len(intd_f)
                    break
                elif ord(first[i+i_add]) > ord(second[j+i_add]):
                    # print("8")
                    # intd_s = intd_s + second[j+i_add]
                    # mode = 1
                    output = output + intd_s
                    j = j + len(intd_s)
                    break
                else:
                    # print ("else")
                    if ord(first[i + i_add]) == ord(first[i]) or count > 0:
                        print ("inside equality match")
                        print (count)
                        print (first[i + i_add])
                        print (first[i + count])
                        if count == 0:
                            i_before = i + i_add
                            print (i)
                            print ("inside count == 0 loop")
                            count = count + 1
                        # elif f_lock == 1 or s_lock == 1:
                        #     count = 0
                        elif match_equal(first[i + i_add], first[i + count]):
                            count = count + 1
                        elif match_greater(first[i + i_add], first[i + count]):
                            if all_same == 0:
                                output = output + first[i:i_before] + second[j:j + i_before - i] #+ first[i_before:i + i_add + 1]
                                print (first[i:i_before])
                                print (second[j:j + i_before - i])
                                print (first[i_before:i + i_add + 1])
                                j = j + i_before - i
                                i = i_before
                                print (i)
                                print (j)
                                print (i_before)
                            elif all_same == 1:
                                output = output + first[i:i + i_add] + second[j:j + i_add]  # + first[i_before:i + i_add + 1]
                                # print (first[i:i_before])
                                # print (second[j:j + i_before - i])
                                # print (first[i_before:i + i_add + 1])
                                j = j + i_add
                                i = i + i_add
                                # print (i)
                                # print (j)
                                # print (i_before)
                            count = 0
                            break
                        elif match_lesser(first[i + i_add], first[i + count]):
                            count = 0

                    if first[i + i_add] != first[i]:
                        all_same = 0

                    # print("5")
                    # if (ord(first[i + i_add]) > ord(min_f)):
                    #     min_f = first[i + i_add]
                    # if (ord(second[j + i_add]) > ord(min_s)):
                    #     min_s = second[j + i_add]
                    if ord(first[i + i_add]) < ord(min_s) and f_lock == 0:
                        intd_f = intd_f + first[i + i_add]
                    else:
                        f_lock = 1
                    if ord(second[j + i_add]) < ord(min_f) and s_lock == 0:
                        intd_s = intd_s + second[j + i_add]
                    else:
                        s_lock = 1
                    i_add = i_add + 1
                # print(ord(first[i + i_add]))
                # print(ord(second[j + i_add]))
                # i_add = i_add + 1
            # print (i_add)
            # if mode == 0:
            #     # print (intd_f)
            #     output = output + intd_f
            #     # output = output + first[i]
            #     i = i + len(intd_f)
            #     # i = i + i_add + 1
            # elif mode == 1:
            #     # print(intd_s)
            #     output = output + intd_s
            #     # output = output + second[j]
            #     # j = j + i_add + 1
            #     j = j + len(intd_s)
    print(output.replace("z", ""))
