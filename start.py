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


import print_tools as pt
from print_tools import COLORS as C
import old_man
from random import randint
from time import sleep

#region ###### static variables ######

showHelp  = True
names = [f"{C.BROWN}copper{C.RESET}", f"{C.GRAY}silver{C.RESET}", f"{C.YELLOW}gold{C.RESET}",  f"{C.LIGHTBLUE}diamond{C.RESET}"]

tutorial = f"""Swindlestones is a dice and bluffing game. The player and their opponent each have a pre-defined number of four-sided dice. Each side of each die is made of a different precious metal: ({C.BROWN}copper{C.RESET}, {C.GRAY}silver{C.RESET}, {C.YELLOW}gold{C.RESET}, and {C.LIGHTBLUE}diamond{C.RESET}).
To start, both players secretly roll and look at their dice. Then, they each take turns either making a bet or call. To make a bet, they make a claim about how many of a certain material was rolled in total. Claims must always be “greater” than the previously made claim. A greater number or more valuable material will be defined as greater, with a greater number always taking precedence.
Ex: One {C.LIGHTBLUE}diamond{C.RESET} is not “greater” than two {C.BROWN}copper{C.RESET}.
To “call” their opponent, the player must simply state “I call”. This forces the hands to be revealed, confirming or disproving their opponent’s claim. If the claim was true, the caller loses a die; if the claim was false, the opponent loses a die. After a call, the dice are re-rolled (dice are not re-rolled after a claim).
The goal is to be the last player with dice remaining.
Press enter to continue"""
#endregion

#region ###### function definitions ######

def rolldice(length):
  """Returns a list of random numbers to use as dice. The number of dice/ length of the list is determined by the parameter."""
  return [randint(0, 3) for i in range(length)]

def countMaterials(hand):
  """Retruns the number of a particular material in the hand. The material is determined by the parameter."""
  count = [0,0,0,0]
  for v in hand:
    count[v] += 1
  return count

def getValue(bet):
  """Converts a list of [number, material] to a number value"""
  return bet[0] * 4 + bet[1]

def decodeBet(val):
  """Converts a number value for a bet to a list of [number, material]"""
  return val // 4 + 1, val % 4

def stringToBet(text):
  """Converts a string of the form "1 copper" or "1 c" to a number value"""
  listvals = text.split(" ")
  if len(listvals) != 2:
    listvals = [text[0], text[1]]
  number = int(listvals[0]) - 1
  l = listvals[1][0].lower()
  material = 0 if l == "c" else 1 if l == "s" else 2 if l == "g" else 3 if l == "d" else -1
  if material == -1:
    raise ValueError("Incorrect material type. Should be copper, silver, gold, diamond, c, s, g, d: " + listvals[1])
  return getValue([number, material])

def checkBet(bet, hand1, hand2):
  """Check whether the bet is valid and return the result"""
  number, material = decodeBet(bet)
  pt.narrate(f"The claim is {number} {names[material]}")
  sums = countMaterials(hand1 + hand2)
  pt.narrate(f"There are {sums[material]} {names[material]}.")
  return number <= sums[material]

def printOutput(win, loss):
  """Outouts a files with the number of wins and losses"""
  gameplay = open('SwindlestonesGameplay.csv', 'w')
  gameplay.write("Game Summary\n")
  gameplay.write(",Wins,Losses\n")
  gameplay.write(",{},{}".format(win, loss))
  

def play():
  """Runs the main body of the game itself."""
  player_dice_total = 5
  old_man_dice_total = 5
  global showHelp
  while True:
    # roll dice
    pt.narrate("You both roll the dice.")
    player_hand = rolldice(player_dice_total)
    old_man_hand = rolldice(old_man_dice_total)
    player_bet = -1

    pt.printDice(player_hand)
    while True:
      # the old man bets
      old_man_bet, type_bet = old_man.bet(player_bet, old_man_hand, len(player_hand))
      if old_man_bet == -1:
        pt.old_man(old_man.bark('call'))
        pt.old_man("I call!")
        sleep(1)
        pt.printDice(player_hand)
        pt.printDice(old_man_hand)
        valid = checkBet(player_bet, player_hand, old_man_hand)
        if not valid:
          pt.narrate("The old man's call was correct. You lose this round")
          player_dice_total -= 1
        else:
          pt.narrate("Your bet was valid! The Old Man loses this round")
          old_man_dice_total -= 1
        break

      num, mat = decodeBet(old_man_bet)
      pt.old_man(old_man.bark(type_bet))
      pt.old_man(f"{num} {names[mat]}")

      # the player makes a choice
      if showHelp:
        pt.printCentered(f"""Make a bet based on your hand as a number and type
      Ex: "1 {C.YELLOW}gold{C.RESET}" or "2 {C.BROWN}copper{C.RESET}"
      This can be abbreviated to "1 g" or "2 c"
      Your bet should be higher than the Old Man's (number always trumps)
      This means 2 {C.BROWN}copper{C.RESET} is greater than 1 {C.LIGHTBLUE}diamond{C.RESET}
      
      You can also call by stating "I call" or simply "call"
      Your hand is displayed above""", height=1, linespacing=1)

      text_input = pt.traveler("1 c")

      if "concede" in text_input:
        pt.narrate("You concede to the old man.")
        pt.old_man("Ay, don't be a poor sport.")
        return False

      while "call" not in text_input:
        try:
          bet = stringToBet(text_input)
          # check the player's choice is valid
          if bet <= old_man_bet:
            pt.printCentered("Your bet must always be greater than the previous bet", height=3)
            text_input = pt.traveler("1 c")
            if "concede" in text_input:
              pt.narrate("You concede to the old man.")
              pt.old_man("Ay, don't be a poor sport.")
              return False
            continue
          break
        except:
          pt.printCentered("Incorrect format. Call or use '1g'", height=3)
          text_input = pt.traveler("1 c")
          if "concede" in text_input:
            pt.narrate("You concede to the old man.")
            pt.old_man("Ay, don't be a poor sport.")
            return False

      # handle the player's call
      if "call" in text_input:
        pt.printDice(player_hand)
        pt.printDice(old_man_hand)
        valid = checkBet(old_man_bet, player_hand, old_man_hand)
        if valid:
          pt.narrate("The old man's bet was valid. You lose this round")
          player_dice_total -= 1
        else:
          pt.narrate("Your call was correct! The Old Man loses this round")
          old_man_dice_total -= 1
        break

      # use the player bet
      player_bet = stringToBet(text_input)

      # turn off help after first loop
      showHelp = False
    
    if (old_man_dice_total < 1 or player_dice_total < 1):
      break

  winner = f"{pt.traveler_color}traveler{C.RESET}" if old_man_dice_total == 0 else f"{pt.old_man_color}Old Man{C.RESET}"
  pt.narrate(f"The game has finished. The {winner} has won.")
  return old_man_dice_total == 0

#endregion

#region ###### main execution ######

# I think that this is how you are supposed to do main code
if __name__ == "__main__":
  # start with a title
  pt.printTitle()
  input()
  pt.clear()

  # print description
  pt.printCentered("""This is the game of Swindlestones, a strategic dice game based on predicting values on the table and making bets.
  This program can:
  generate random numbers to resemble a dice roll
  create a tavern-like environment with dialogue and symbols
  simulate an opponent using an AI that intuitively places challenging bets
  allow the user to play an enjoyable game of Swindlestones 
  output a file with the number of wins and losses
  
  Press enter to continue""")
  input()
  pt.clear()

  # print the introduction text
  pt.printCentered("""You are a traveler from a distant place, entering a tavern with only a handful of coins in your possession.
  As you make your way through the dimly lit room, you notice the peculiar old man in the corner watching you. 
  You meet eyes, and he quickly looks away to stare at something lying on the table in front of him.
  Your curiosity has been sparked, you decide to approach the old man. 
  He turns to you with a knowing look and motions to what he had previously been fixated on- some strange dice with colored faces.
  \"Would you like to play?\"
  Press enter to continue""", padding=10)
  input()
  pt.clear()

  # give the option for a tutorial
  pt.old_man("Have you played Swindle Stones before?")
  response = pt.traveler("y/n").lower()
  if (response == "yes") or (response == 'y'):
    # skip tutorial
    showHelp = False
  else:
    if (response == "no") or (response == "n"):
      pt.old_man("Aye then, let me teach you a thing or two about dice!")
    else:
      pt.old_man("I'm not sure I understand, but I'll give you a refresher anyway")
    sleep(1)
    pt.clear()
    # prints with a 10% padding
    pt.printCentered(tutorial, padding=10)
    input()
    pt.clear()

  wins = 0
  losses = 0
  while True:
    winner = play()
    if winner == True:
      wins += 1
    else:
      losses += 1
    pt.old_man("Would you like to play again?")
    text = pt.traveler("y/n").lower()
    if text == "y" or text == "yes":
      continue
    else:
      printOutput(wins, losses)
      break

  pt.clear()
  pt.printCentered("Your wins and losses have been printed to SwindlestonesGameplay.csv\nPress Enter to exit", padding=20)
  input()
  pt.clear()

#endregion

