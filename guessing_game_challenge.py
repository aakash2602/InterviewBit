import random

random_number = random.randint(0,100)

print (random_number)
print ("Guess a number between 0 to 100 both included")
print ("Take as many guesses as you want")

guess = []
difference = []
while (True):
    number = int(input("Enter a number: "))
    if number < 1 or number > 100:
        print ("OUT Of Bounds")
        continue
    diff = abs(number-random_number)
    if diff == 0:
        print (f'yipee {number} is the number')
        break
    if len(guess) == 0:
        if diff <= 10:
            print ("WARM!")
        else:
            print ("COLD!")
        guess.append(number)
        difference.append(diff)
        continue
    if diff < difference[-1]:
        print ("WARMER!")
    else:
        print ("COLDER!")
    guess.append(number)
    difference.append(diff)


