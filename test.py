

# import print_tools as pt
# from print_tools import printCentered as cprint
# from random import randint
# import time
# from PIL import Image

# def rolldice(length):
#   return [randint(0, 3) for i in range(length)]

# datalist = []
# w = 0
# h = 0

# def printImage(data, width, height):
#   ratio = width / pt.screenwidth
#   theight = height / ratio * .5
#   pxw = int(ratio)
#   pxh = int(ratio / 3*5)
#   for i in range(int(theight)):
#     for j in range(pt.screenwidth):
#       size = 5
#       y = int(i * ratio / .5)
#       x = int(j * ratio)
#       pix = [0,0,0,0]
#       for sx in range(pxw):
#         for sy in range(pxh):
#           spix = data[x + sx + (y + sy) * width]
#           for nv, v in enumerate(spix):
#             pix[nv] += v
#       pix = [int(el / pxw / pxh) for el in pix]
#       print(f"\033[48;2;{pix[0]};{pix[1]};{pix[2]}m" + " ", end="")
#     print()
#   print(pt.COLORS.RESET)

# # Uncomment to blow your mind
# im = Image.open('crystals.png')
# printImage(im.getdata(), im.width, im.height)
# input()

# pt.printTitle()
# input()
# pt.clear()
# cprint("So you’ve played Swindlestones before?")
# pt.move(pt.screenwidth / 2 - 3, pt.screenheight / 4 * 3)
# inn = input()
# if inn.lower() == "no" or inn.lower() == 'n':
#   pt.clear()
#   cprint("Swindlestones is a dice and bluffing game. The player and their opponent each have a pre-defined number of four-sided dice. Each side of each die is made of a different precious metal: (" + pt.COLORS.ORANGE + "copper" + pt.COLORS.RESET + ", " + pt.COLORS.GRAY + "silver" + pt.COLORS.RESET + ", " + "\033[38;2;255;200;0m" + "gold" + pt.COLORS.RESET + ", and " + pt.COLORS.LIGHTBLUE + "diamond" + pt.COLORS.RESET +""").
# To start, both players secretly roll and look at their dice. Then, they each take turns either making a bet or call. To make a bet, they make a claim about how many of a certain material was rolled in total. Claims must always be “greater” than the previously made claim. A greater number or more valuable material will be defined as greater, with a greater number always taking precedence.
# Ex: One diamond is not “greater” than two coppers.
# To “call” their opponent, the player must simply state “I call”. This forces the hands to be revealed, confirming or disproving their opponent’s claim. If the claim was true, the caller loses a die; if the claim was false, the opponent loses a die. After a call, the dice are re-rolled (dice are not re-rolled after a claim).
# The goal is to be the last player with dice remaining.""", padding=10)
#   input()
# pt.clear()
# cprint("Here is your hand:", height=3)
# hand = rolldice(5)
# pt.printDice(hand)
# cprint("What would you like to claim?", height=3)
# pt.move(pt.screenwidth / 2 - 7, 10)
# input()
# pt.move(0, pt.screenheight - 1)
