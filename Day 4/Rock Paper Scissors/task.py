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

#
# import random
#
# comps =  ['rock', 'paper', 'scissors']
#
# ai1 = random.choice(comps)
# ai2 = random.choice(comps)
#
# print(ai1)
# print(ai2)
# if ai1 == ai2:
#     print("It's a tie")
# elif ai1=='rock' and ai2=='paper':
#     print("ai2 wins")
# elif ai1=='paper' and ai2=='scissors':
#     print(f"ai2 wins, choosed {ai2}")
# else:
#     print(f"ai1 wins, choosed {ai1}")
#



## Optimized oop code:

import random
class RockPaperScissors:
    def __init__(self):
        self.options = ['Rock', 'Paper', 'Scissors']
        self.rules = {'Rock': S, 'Paper Scissors': None, 'Scissors': None}
