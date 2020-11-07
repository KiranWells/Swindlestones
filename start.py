import print_tools as pt
from print_tools import COLORS as C
import old_man
from random import randint
from time import sleep

#region ###### static variables ######

showHelp  = True
old_man_bark = {
    'call': "call",
    'low': "low",
    'high': "high"
}
names = [f"{C.BROWN}copper{C.RESET}", f"{C.GRAY}silver{C.RESET}", f"{C.YELLOW}gold{C.RESET}",  f"{C.LIGHTBLUE}diamond{C.RESET}"]

tutorial = f"""Swindlestones is a dice and bluffing game. The player and their opponent each have a pre-defined number of four-sided dice. Each side of each die is made of a different precious metal: ({C.BROWN}copper{C.RESET}, {C.GRAY}silver{C.RESET}, {C.YELLOW}gold{C.RESET}, and {C.LIGHTBLUE}diamond{C.RESET}).
To start, both players secretly roll and look at their dice. Then, they each take turns either making a bet or call. To make a bet, they make a claim about how many of a certain material was rolled in total. Claims must always be “greater” than the previously made claim. A greater number or more valuable material will be defined as greater, with a greater number always taking precedence.
Ex: One {C.LIGHTBLUE}diamond{C.RESET} is not “greater” than two {C.ORANGE}copper{C.RESET}.
To “call” their opponent, the player must simply state “I call”. This forces the hands to be revealed, confirming or disproving their opponent’s claim. If the claim was true, the caller loses a die; if the claim was false, the opponent loses a die. After a call, the dice are re-rolled (dice are not re-rolled after a claim).
The goal is to be the last player with dice remaining.
Press enter to continue"""

#endregion

#region ###### function definitions ######

def rolldice(length):
  return [randint(0, 3) for i in range(length)]

def countMaterials(hand):
  count = [0,0,0,0]
  for v in hand:
    count[v] += 1
  return count

def getValue(bet):
  """Converts a list of [number, material] to a number value"""
  return bet[0] * 4 + bet[1]

def decodeBet(val):
  """Converts a number value for a bet to a list of [number, material]"""
  return val // 4, val % 4

def stringToBet(text):
  """Converts a string of the form "1 copper" or "1 c" to a number value"""
  listvals = text.split(" ")
  if len(listvals) != 2:
    listvals = [text[0], text[1]]
  number = int(listvals[0])
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

def play():
  player_dice_total = 5
  old_man_dice_total = 5
  global showHelp
  while True:
    # roll dice
    pt.narrate("You both roll the dice.")
    player_hand = rolldice(player_dice_total)
    old_man_hand = rolldice(old_man_dice_total)

    pt.printDice(player_hand)
    while True:
      # the old man bets
      old_man_bet = old_man.bet(old_man_hand)
      pt.old_man(f"I say {old_man_bet}")

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

      while "call" not in text_input:
        try:
          bet = stringToBet(text_input)
          break
        except:
          pt.printCentered("Incorrect format. Call or use '1g'", height=3)
          text_input = pt.traveler("1 c")

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

      # check the player's choice is valid
      if player_bet < old_man_bet:
        pt.printCentered("Your bet must always be greater than the previous bet")
      
      # give the old man a chance to call
      choice = old_man.callOrNot(player_bet)

      if choice:
        pt.printDice(player_hand + old_man_hand)
        valid = checkBet(old_man_bet, player_hand, old_man_hand)
        if valid:
          pt.narrate("The old man's call was correct. You lose this round")
          player_dice_total -= 1
        else:
          pt.narrate("Your bet was valid! The Old Man loses this round")
          old_man_dice_total -= 1
        break

      # turn off help after first loop
      showHelp = False
    
    if (old_man_dice_total < 1 or player_dice_total < 1):
      break

  winner = "traveler" if old_man_dice_total == 0 else "Old Man"
  pt.narrate(f"The game has finished. The {winner} won.")
  return winner

#endregion

#region ###### main execution ######

# start with a title
pt.printTitle()
input()

# print the introduction text
pt.clear()
pt.printCentered("""Hello, welcome to Swindle Stones.
You are a traveler who has entered a tavern with a handful of coins
You see a man in the corner motioning for you to come over""", height=10)
pt.old_man("Have you played Swindle Stones before?")
response = pt.traveler("y/n").lower()
if response == "yes" or response == 'y':
  # skip tutorial
  showHelp = False
else:
  pt.old_man("Let me give you the basics, then.")
  sleep(1)
  pt.clear()
  pt.printCentered(tutorial, padding=10)
  input()
  pt.clear()

# copper, silver, gold, diamond

material_names = ["copper", "silver", "gold", "diamond"]

while True:
  winner  = play()
  pt.old_man("Would you like to play again?")
  text = pt.traveler("y/n").lower()
  if text == "y" or text == "yes":
    continue
  else:
    break

pt.clear()

#endregion

