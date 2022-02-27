print("Welcome to my car quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What car brand made the deville models ")
if answer.lower() == "cadillac":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What car brand made the countach model ")
if answer.lower() == "lamborghini":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What car brand made the regal models ")
if answer.lower() == "buick":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what car brand made the raptor pickup ")
if answer.lower() == "ford":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")

input()