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

'''
#Steps
--> Create Class
 --> init and: define options add rule
 --> Create choice for ai function
 --> play game: here pas player 1 and to and passs the choices in winner_function
'''
import random
class RockPaperScissors(object):
    def __init__(self):
        choose = ['rock','paper','scissors']
        rule =  {
            'rock': 'scissors',
            'scissors': 'paper',
            'paper': 'rock'
        }
    def playerschoice(self):
        return random.choice(self.choose)
    def winner_function(self,player1,player2):
        if player1==player2:
            return 'tie'
        elif self.rules[player1]== player2:

