print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the treasure island")
print("YOur mission is to find the treasure")
choice1 = input("You are at a crossroad, where do you want to go? type 'left' or 'right' ")

if choice1 ==  "left" or "LEFT":
    choice2 = input('You are come to the lake'
                    'There is the islade middle of the lake'
                    'type "wait " for the boat'
                    'Type "swim" to swim across.\n')
    if choice2 == "Wait":
        choice3 = input('You arrive at the island unharmed'
                        'there is the house of three door.one red'
                        'One Blue and One yellow'
                        'Which one colour do you choose/\n').lower()

        if choice3 ==  "red" :
            print("It is room full to fire: ")
        elif choice3 == "blue":
            print("you entre a room of beast.game over. ")
        elif choice3 == "yellow":
            print("You found the treasure you win!")
        else:
            print("You got attacked by an angry trout . Game over.")

else:
    print("YOu fell in to the hole. Game over")






