# -*- coding: UTF-8 -*-
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Griffith Thomas
#               Anjali Kumar
#               Eric Ballard
#               Ana Jimenez
# Section:      208
# Assignment:   Final Project
# Date:         11 14 2020

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
          if i < list.count(hand, j-1):
              possible_bets.append(j + i*4)
          else:
              possible_bets.append(0)
  for i in range(0, 4*len(hand)):
      possible_bets.append(0)
  return possible_bets

# variable redefinition
old_man_hand_size = 5
player_hand_size = 5
    
def bet(current_bet, old_man_hand):
  """Decides whether or not to bet based on 
  the player's bet and the old man's hand"""
# the old man doesn't know the player's hand, so it is not passed in
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
  
  if random.random() > 0.7:
    old_man_bet = max_bet
    bet_size = "high bet"
  else:
    old_man_bet = min_bet
    bet_size = "low bet"
   
  call = 0
  if current_bet > 4 * player_hand_size:
    call = 1
  #elif min_bet == max_bet and current_bet not in old_man_hand_current_round:
  #  call = 1
  elif old_man_bet == 0:
    call = 1
  #elif max_bet == current_bet:
  #  call = 1
  else:
    pass
  if old_man_bet <= current_bet:
    # illegal bet, he needs to make a higher one
    type_d = current_bet % 4
    num_d = num_dice(current_bet)
    if num_d < 4 + old_man_hand.count(type_d):
      old_man_bet = type_d - 1 + (num_d) * 4
    else:
      call = 1
  if call == 1 and current_bet < 0:
    # the old man can't bet because it is first round
    call = 0
    min_bet = min_bet if min_bet > current_bet else current_bet + 1
  if call == 1:
    bet_size = "call"
  return old_man_bet if not call else -1, bet_size

def get_rand_from_list(l):
  """returns a randomly selected element from the list `l`"""
  return l[random.randint(0, len(l) - 1)]

def bark(bet):
  """Returns the bark by the old man. It takes one parameter which is the bet placed by the old man."""
  rad = int(random.random()*4)
  high_bark = ["Ay, let's how you like this!", "Hehehe, you ain't as clever as I", "You gotta lose a few games to win them", "Ha, I'll do you one better!"]
  low_bark = ["Hmmm, I need to take it slower...", "You need to learn patience, whippersnapper", "No need to rush the game", "I doubt you even have this..."]
  call_bark = ["Ay, you think me a fool!", "Ha, this ain't my first game of dice!", "You thought you could swindle me!", "Ay, you're a wily nave, but not wily enough!"]
  if (bet == "high bet"):
    output = high_bark[rad]
  if (bet == "low bet"):
    output = low_bark[rad]
  if (bet == "call"):
    output = call_bark[rad]
  return output
