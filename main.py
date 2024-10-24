import random
n = random.randint(1,100)
a = -1
guesses = 0
while(a != n):
    a = int(input("Guess the number: "))
    if(a > n):
        print("Lower number please")
        guesses +=1
    elif(a<n):
        print("Higer number please")
        guesses +=1

print(f"You have guessed the number {n} correcrtly in {guesses} attempt")