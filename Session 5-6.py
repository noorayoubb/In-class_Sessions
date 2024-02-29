#while game
import random
lives = 3

while lives:
    print("you have", lives, "lives left")
    dice_roll = random.randint(1, 6)
    if dice_roll == 6:
        print("you rolled a 6, you win!")
        break

    print("you rolled a", dice_roll, "try again")
    lives -= 1

else:
    print("You lost all your lives, game over")

# I want to print the multiplication table for 1 to 10
for i in range(1, 11):
    for j in range(i, 11):
        print(i, "x", j, "=", i*j)
    print()

#exceptions
try:
    age1 = int(input("What is your age player 1? "))
    age2 = int(input("What is your age player 2? "))
    res = age1 / age2
except ValueError:
    print("I am sorry, but that is not a valid number")
except ZeroDivisionError:
    print("Do not put zero!!")
except:
    print("I am sorry, but now you must die")
else:
    print("Player 1 is older than player 2 by a factor of", res)
finally:
    print("Thank you for playing")

#conditional execution (if statement)
import random
drinks = ["beer", "wine", "whiskey", "rum", "gin tonic", "vodka", "martini", "rakia"]
try:
    age = int(input("How old are you? "))
    country = input("Where you living??")
except ValueError:
    print("I am sorry, but that is not a valid number")

else:
    # Do some sanity checks on age
    if age < 0 or age > 130:
        print("I am sorry, but your age cannot be negative or greater than 130")
    elif age < 18:
        print("I am sorry, too young to play this drinking game everywhere")
    elif age < 21 and country == "US":
        print("I am sorry, too young to play this drinking game in the US")
    else:
        drink = random.choice(drinks)
        print("Take a shot of ", drink, ". Thank you for playing, you are", age, "years old")
