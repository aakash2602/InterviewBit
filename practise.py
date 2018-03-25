def myfunc(sequence):
    output = ''
    for i, value in enumerate(sequence):
        print (i)
        print (value)
        if i == 0:
            output += value.lower()
        else:
            if i % 2 == 0:
                output += value.upper()
            else:
                output += value.lower()
    return output

print (myfunc("Anthromorphism"))