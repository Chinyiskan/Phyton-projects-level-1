import random


# Function to roll dies and print the result on console:
def dice_rolling():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"🎲 1: {dice1} 🎲 2: {dice2}")


# Main function with the loop for the user interaction:
def main():
    while True:
        user_choice = int(input("Type '1️⃣' to roll the 🎲 and '2️⃣' to exit."))
        if user_choice == 1:
            print(dice_rolling())
        elif user_choice == 2:
            print("Have a good day!")
            break
        else:
            print("Incorrect ❌ Try again!")
            user_choice = int(input("Type '1️⃣' to roll the 🎲 and '2️⃣' to exit."))


main()
