import random
num = random.randint(1, 100)
print("randon number：%d" %num)
flag = True
count = 0

while flag:
    guess_num = int(input("Guess the number: "))
    count = count + 1
    if(guess_num == num):
        print("You guessed it right!")
        flag = False
    else:
        print("You guessed it wrong!")
        if guess_num > num:
            print("Your guess is greater than the number!")
        else:
            print("Your guess is lesser than the number!")
        flag = True
    print(f"flag: {flag}")
print("Number of guesses: ", count)

print("Game over ",end=' ')