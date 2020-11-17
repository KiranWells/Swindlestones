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
      for j in range (0, 4):
          if i < hand.count(j):
              possible_bets.append(j + i*4)
          else:
              possible_bets.append(-1)
  # for i in range(0, 4*len(hand)):
  #     possible_bets.append(0)
  return possible_bets

previous_player_bet = 0
previous_old_man_bet = 0
    
def bet(current_bet, old_man_hand, player_hand_size):
  """Decides whether or not to bet based on 
  the player's bet and the old man's hand"""
# the old man doesn't know the player's hand, so it is not passed in
  global previous_old_man_bet
  global previous_player_bet
  old_man_hand_current_round = find_possible_bets(old_man_hand)
  # print(old_man_hand_current_round)

  # code to attempt a bluff
  if random.random() > 0.9:
    # print("bluffing")
    try:
      old_man_hand_current_round[current_bet + 4] = current_bet + 4 #*int(random.random()*2+1)
    except:
      pass

  # calculates min and max bets
  max_bet = max(old_man_hand_current_round)
  min_bet = max_bet
  for value in old_man_hand_current_round:
    if value > current_bet and value < min_bet:
      min_bet = value
      break
  # print("max", max_bet)
  # print("min", min_bet)
  
  if random.random() > 0.8:
    old_man_bet = max_bet
    bet_size = "high bet"
  else:
    old_man_bet = min_bet
    bet_size = "low bet"
   
  call = 0

  # impossible claim fix
  if current_bet > 4 * player_hand_size:
    # print("calltest")
    mat_type = current_bet % 4
    num_of_old_man = old_man_hand.count(mat_type)
    if current_bet // 4 > player_hand_size + num_of_old_man - 1:
      call = 1
  elif old_man_bet == 0:
    call = 1
  else:
    pass
  
  # recognize a one-up
  if current_bet // 4 == previous_old_man_bet // 4 + 1 and current_bet % 4 == previous_old_man_bet % 4:
    # print("oneup")
    if current_bet // 4 > old_man_hand.count(current_bet % 4):
      call = 1
  
  # illegal bet fix
  if old_man_bet <= current_bet:
    if max_bet > current_bet:
      old_man_bet = max_bet
    else:
      # print("myfix")
      # illegal bet, he needs to make a higher one
      counts = [old_man_hand.count(i) for i in range(4)]
      # add the player's bet to the known dice counts
      # / 1.5 to offset the players bet since it may be false
      # counts[current_bet % 4] += current_bet // 4 / 1.5
      type_d = counts.index(max(counts))
      num_d = current_bet // 4
      if current_bet // 4 < player_hand_size + old_man_hand.count(current_bet % 4) - 2:
        if random.random() > 0.1:
          old_man_bet = type_d + (num_d + 1) * 4
        else:
          old_man_bet = current_bet + random.randint(1,3)
      else:
        call = 1

  # first round fix
  if call == 1 and current_bet < 0:
    # the old man can't call because it is first round
    call = 0
    old_man_bet = min_bet if min_bet > current_bet else current_bet + 1

  # update previous 
  previous_old_man_bet = old_man_bet
  previous_player_bet = current_bet

  if old_man_bet == min_bet:
    bet_size = "low bet"
  else:
    bet_size = "high bet"

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
