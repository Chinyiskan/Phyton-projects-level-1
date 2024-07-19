import random

print("""
===================
Rock Paper Scissors
===================
1) ✊
2) ✋
3) ✌️
4) 🦎
5) 🖖
""")

#User pick
user = int(input("Pick a number: "))

#CPU pick
computer = random.randint(1,5)

#Dictionary to store the emojis
emojis = {1:"✊", 2:"✋", 3:"✌️", 4:"🦎", 5:"🖖"}

#print choices
print(f"""
You chose {emojis[user]}
CPU chose {emojis[computer]}
""")

#Program logic  
if user == computer:
    print("It's a draw!")
          
elif (user == 1 and computer == 3) or \
    (user == 2 and computer == 1) or \
    (user == 3 and computer == 2) or \
    (user == 1 and computer == 4) or \
    (user == 4 and computer == 5) or \
    (user == 5 and computer == 3) or \
    (user == 3 and computer == 4) or \
    (user == 4 and computer == 2) or \
    (user == 2 and computer == 5) or \
    (user == 5 and computer == 1) or \
    (user == 3 and computer == 2):
    print("The player won!")

else:
    print("The CPU won!")
    



