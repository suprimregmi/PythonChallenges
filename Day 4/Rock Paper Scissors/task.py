rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random

comps =  ['rock', 'paper', 'scissors']

ai1 = random.choice(comps)
ai2 = random.choice(comps)

print(ai1)
print(ai2)
if ai1 == ai2:
    print("It's a tie")
elif ai1=='rock' and ai2=='paper':
    print("ai2 wins")
elif ai1=='paper' and ai2=='scissors':
    print(f"ai2 wins, choosed {ai2}")
else:
    print(f"ai1 wins, choosed {ai1}")




## Optimized:

import random
# class RockPaperScissors:
#     def __init__(self):
#         self.choices = ['rock', 'paper', 'scissors']
#         self.rules = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
#     def get_choice(self):
#         return random.choice(self.choices)
#     def determine_winner(self,ai1,ai2):
#         if ai1==ai2:
#             return "It's a tie"
#         elif self.rules[ai1] == ai2:
#             return f" AI1 wins chose {ai1}"
#         else:
#             return f"AI2 wins chose{ai2}"
#     def play(self):
#         ai1 = self.get_choice()
#         ai2 = self.get_choice()
#     print("AI1: ", ai1)
#     print("AI2", ai2)
#     print(self.determine_winner(ai1,ai2))
# if __name__ == '__main__':
#     game = RockPaperScissors()
#     game.play()




import random
class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.rules = {
            'rock': 'scissors',
            'scissors': 'paper',
            'paper': 'rock'
        }
    def get_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, ai1, ai2):
        if ai1 == ai2:
            return "It's a tie"
        elif self.rules[ai1] == ai2:
            return f"AI1 wins, chose {ai1}"
        else:
            return f"AI2 wins, chose {ai2}"
    def play(self):
        ai1 = self.get_choice()
        ai2 = self.get_choice()
        print("AI1:", ai1)
        print("AI2:", ai2)
        print(self.determine_winner(ai1, ai2))
if __name__ == "__main__":
    game = RockPaperScissors()
    game.play()

