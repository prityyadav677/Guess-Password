# import random
# import string

# length =int(input("Enter password length :"))

# characters = string.ascii_letters + string.digits + string.punctuation
# password = ""

# for i in range(length):
#     password += random.choice(characters)

# print("Generated Password :",password) 
import random 

target = random.randint(1,100)

while True:
    userChoice = input("Guess the target or quit :")
    if(userChoice == "q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess !!")
        break
    elif(userChoice < target):
        print("your number was too small. Take a bigger guess...")
    else:
        print("your number was too big. Take a small guess..")
print("------GAME OVER------")        