

inp = []
inp.append(4)
inp.append(3)
inp.append(7)
inp.append(8)
inp.append(6)
inp.append(2)
inp.append(1)
print (inp)

relation = 'l'
for i in range(0, len(inp)-1):
    if relation == 'l':
        relation = 'r'
        if inp[i] > inp[i+1]:
            inp[i], inp[i+1] = inp[i+1], inp[i]
    elif relation == 'r':
        relation = 'l'
        if inp[i] < inp[i+1]:
            inp[i], inp[i+1] = inp[i+1], inp[i]

print (inp)