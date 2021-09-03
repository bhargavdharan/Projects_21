print("Welcome to my First Game!")

name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello! Welcome..",name, "You are", age, "years old");

health = 10


print("You are starting with",health, "health")

if age >=18:
    print("You are old enough!")
    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Lets Play! ")

        left_or_right = input("First choice... Left or Right(left/right)? ")
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake...Do you want to swim across or go around (across/around) ? ")
            if ans == "around":
                print("You went around and reached the other side of the lake.")
            elif ans == "across":
                print("You managed to get across, but were bite by a fish! You Lost...5 health")
                health -= 2

            ans = input("You noticed a house and a river. which do you go to (river/house) ? ")
            if ans== "house":
                print("You go to the house and are greeted by the owner.... he doesn't like you and you lose.. 5 Health ")
                health -= 5

                if health <=0:
                    print("you now have a 0 health and you lost the game...")
                else:
                    print("You Survived!!! Hurray")

            else:
                print("You Fell in the river and lost!...")

        else:
            print("you fell down and lost..")


    else:
        print("Cya...")


else:
    print("You are not old enough to play....! ")






















# is_older = int(age) >= 18
# print(is_older)











