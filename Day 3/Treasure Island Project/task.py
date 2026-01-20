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
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")

# option = input("left or right ? ")
# if option == "Left":
#     option2 = input("swim or wait ? ")
#     if option2 == "Wait":
#         option3  = input("Which door? ")
#         if option3 =='Yellow':
#             print("You win!")
#         elif option3 =='Red':
#             print("Burned by fire. \n  Game Over.")
#         elif option3 =='Blue':
#             print('''Eaten by Beasts.\
#                         Game Over.''')
#         else:
#             print("Game Over.")
#     else:
#         print('''Attacked by trout.\n\tGame Over.''')
#
# else:
#     print('''Fall into a hole\n\tGame Over.''')
#


## Using OOP:
#
# class TreasureIslandGame:
#     def __init__(self):
#         print("Welcome to Treasure Island.")
#         print("Your mission is to find the treasure.\n")
#
#     def start(self):
#         choice = input("left or right").lower()
#         if choice =='left':
#             self.lake()
#         else:
#             self.game_over("Fall into a hole.")
#     def lake(self):
#         choice = input("Swim or Wait").lower()
#         if choice =='swim':
#             self.house()
#         else:
#             self.game_over("Attacked by trout.")
#     def house(self):
#         choice = input("Which door? (Red / Blue / Yellow) ").lower()
#         if choice == "yellow":
#             print("🎉 You win!")
#         elif choice == "red":
#             self.game_over("Burned by fire.")
#         elif choice == "blue":
#             self.game_over("Eaten by beasts.")
#         else:
#             self.game_over("Wrong choice.")
#
#     def game_over(self, reason):
#         print(f"{reason}\nGame Over.")

# game = TreasureIslandGame()
# game.start()

class Dog:
    def __init__(self, name):
        self.name = name

d1 = Dog("Tommy")
d2 = Dog("Rocky")







