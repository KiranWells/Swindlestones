"""
Old Man AI fo Swindlestones 
===========================

This is the artificial intelligence that the player will be 
playing against. The methods will take the information that 
the old man would have and returns a decision based on that

Attributes:
-----------
  none yet

Methods:
--------
  bet:
    Decides what to bet based on the old man's hand
"""

import random

def num_dice(bet):
  """translates bet number to dice number"""
  output = bet // 4 + 1
  return output

def mat_dice(bet):
  """translates bet number to material"""
  if bet % 4 == 0:
      mat = "copper"
  if bet % 4 == 1:
      mat = "silver"
  if bet % 4 == 2:
      mat = "gold"
  if bet % 4 == 3:
      mat = "diamond"
  return(mat)

def find_possible_bets(hand):
  """creates a list of bets for the round"""
  possible_bets = []
  for i in range (0, len(hand)):
      for j in range (1, 5):
          if i < list.count(hand, j):
              possible_bets.append(j + i*4)
          else:
              possible_bets.append(0)
  for i in range(0, 4*len(hand)):
      possible_bets.append(0)
  return possible_bets

#variable redefinition
old_man_hand_size = 5
player_hand_size = 5
# total_hand_size = old_man_hand_size + player_hand_size
# # player_hand = []
# # old_man_hand = []
# # current_bet = int(random.random()*1.5*total_hand_size + 1)
# min_bet = 0
# old_man_bet = 0

# fills both hands
# for i in range(0, player_hand_size):
#     player_hand.append(int(4*random.random())+1)
# for i in range(0, old_man_hand_size):
#     old_man_hand.append(int(4*random.random())+1)
    
def bet(current_bet, old_man_hand):
  """Decides whether or not to bet based on 
  the player's bet and the old man's hand"""
# the old man doesn't know the player's hand, so it is not passed in
# I now print it outside
  old_man_hand_current_round = find_possible_bets(old_man_hand)
  if random.random() > 0.5:
    try:
      old_man_hand_current_round[current_bet + 3] = current_bet + 4*int(random.random()*2+1)
    except:
      pass

  # calculates min and max bets
  max_bet = max(old_man_hand_current_round)
  min_bet = max_bet
  for value in old_man_hand_current_round:
    if value > current_bet and value < min_bet:
      min_bet = value
      break
  
  # if min_bet < current_bet:
  #   min_bet = current_bet + 1
  #   max_bet = current_bet + 1

  # print("possible bets: ", old_man_hand_current_round)
  # # print("player hand: ", player_hand)
  # print("old man hand: ", old_man_hand)
  # print("max bet is:", max_bet, "or", num_dice(max_bet), mat_dice(max_bet))
  # print("current bet is:", current_bet, "or", num_dice(current_bet), mat_dice(current_bet))

  if random.random() > 0.5:
    old_man_bet = max_bet
  else:
    old_man_bet = min_bet
  
  # if min_bet == 0:
  #   print("no min bet")
  # else:
  #   print("min bet is:", min_bet, "or", num_dice(min_bet), mat_dice(min_bet))
      
  call = 0
  if current_bet > 4*player_hand_size:
    call = 1
  elif min_bet == max_bet and current_bet not in old_man_hand_current_round:
    call = 1
  elif old_man_bet == 0:
    call = 1
  elif max_bet == current_bet:
    call = 1
  else:
    pass
    # print("final bet is:", old_man_bet, "or", num_dice(old_man_bet), mat_dice(old_man_bet))
  if call == 1 and current_bet < 0:
    # the old man can't bet because it is first round
    call = 0
    min_bet = min_bet if min_bet > current_bet else current_bet + 1
  return old_man_bet if not call else -1

# checks to see who wins the round
# if 0 == 1:
#     print("call!")
#     if current_bet in find_possible_bets(player_hand + old_man_hand):
#         print("old man looses!")
#     else:
#         print("player looses!")