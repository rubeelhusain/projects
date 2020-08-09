import random

def computerGuess(lowval, highval, randnum, count = 1):
    if highval >= lowval:
        guess = lowval + (highval - lowval) // 2
        #if guess is in middle, it is found!
        if guess == randnum:
            return count

        #if guess is greater than the number

        #it must be found in the lower half of the set of numbsers
        #between the lower value and the guess
        elif guess > randnum:
            count = count+1
            return computerGuess(lowval,guess-1,randnum,count)

        #it must be found in the upper half of the set of numbsers
        #between the upper value and the guess
        else:
            count = count+1
            return computerGuess(guess+1,highval,randnum,count)

    else:
        #number not found
        return -1
#end of function

#generate a random number between 1 and 100
randnum = random.randint(1,1001)

count = 1
guess = -99
while (guess!=randnum):
    #get user's input
    guess = (int)(input("Enter your guess between 1 and 1000: "))
    if guess < randnum:
        print("higher")
    elif guess > randnum:
        print("lower")
    else:
        print ("you guessed it!")
        break
    count = count + 1
#end of loop
a= count
b=computerGuess(1,1000,randnum)
print ("You took "+ str(a)+" steps to guess the number")
print ("Computer took "+ str(b)+ " steps to guess the number")
print("")
if a<b:
    print("Won!!")
elif a>b:
    print("Lost!")
else:
    print("Draw!!")
