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
Print Tools for Swindlestones
=============================

This is a general collection of output managing tools for 
the game Swindlestones

Attributes:
-----------
  COLORS: a list of escape characters to change the color 
  of the following text printed to console
  
  COPPER, SILVER, GOLD, DIAMOND:
    Represent the materials that each corresponds to.
    For use in methods that take a material
  
  screenwidth: the width of the console, in columns
  
  screenheight: the height of the console, in lines

Methods:
--------
  warn:
    print a warning

  error:
    print an error

  cprint:
    print a message in a certain color

  move:
    move the cursor to the given x, y coordinates in the console

  clear:
    clear the console

  getColor:
    get a color value from a given material

  printDice:
    print a graphical representation of a given list of material values

  printTitle:
    print the SwindleStones title

  printCentered:
    print a horizontally and vertically centered clock of 
    text with a given amount of padding

  old_man:
    print the message in a dialogue format, with the old man's name and color preceding it

  traveler:
    get input from the user, prompted with the traveler's name and color preceding it

  narrate:
    print a narration message
"""

from enum import Enum
from sys import stdout
from os import system, name
from shutil import get_terminal_size
import re

class COLORS:
  """A collection of color-changing escape sequences"""
  BLACK     = "\033[;30m"
  RED       = "\033[;31m"
  ERROR     = "\033[;31m"
  GREEN     = "\033[;32m"
  YELLOW    = "\033[1;33m"
  WARNING   = "\033[1;33m"
  BLUE      = "\033[;34m"
  LIGHTBLUE = "\033[1;34m"
  PURPLE    = "\033[;35m"
  CYAN      = "\033[;36m"
  WHITE     = "\033[;37m"
  ORANGE    = "\033[;33m"
  BROWN     = "\033[2;33m"
  TURQUOISE = "\033[1;32m"
  GRAY      = "\033[2;37m"
  RESET     = "\033[0m"

COPPER  = 0
SILVER  = 1
GOLD    = 2
DIAMOND = 3

screenwidth = get_terminal_size().columns
screenheight = get_terminal_size().lines

old_man_color = COLORS.ORANGE
narrator_color = "\033[1;2;37m"
traveler_color = COLORS.BLUE

_DEBUG = True

def warn(message):
  """Print a yellow warning message to the console if DEBUG is True"""
  message = message.replace(COLORS.RESET, COLORS.WARNING)
  if (True):
    print(COLORS.WARNING + "Warning: " + message + COLORS.RESET)

def error(message):
  """Print a red error message to the console if DEBUG is True"""
  message = message.replace(COLORS.RESET, COLORS.ERROR)
  if (True):
    print(COLORS.ERROR + "Error: " + message + COLORS.RESET)

def cprint(message, color, sep=" ", end="\n", file=stdout, flush=False):
  """Print the given message in the given color, from COLORS"""
  print(color + message + COLORS.RESET, sep=sep, end=end, file=file, flush=flush)

def move(x,y):
  """Move the cursor to the given `x`, `y` coordinates in the console
    
    The coordinates start at 1, 1 in the top left corner"""
  print(f"\033[{int(y)};{int(x)}H", end="", flush=True)
  # for i in range(int(x)):
  #   print(" ", end="")

def clear():
  """A platform-independent way to clear the console"""
  if name == "nt":
    system("cls")
  else:
    system("clear")

def center(line, width, fill=" "):
  """returns a line centered to a given width with `fill` as the fill character, ignoring escape sequences"""
  actualtext = re.sub("\033((?![a-zA-Z]).)*[a-zA-Z]", "", line)
  actualwidth = len(actualtext)
  fillstart = int((width - actualwidth) / 2)
  # return fillstart
  fillend = width - actualwidth - fillstart
  if (width < actualwidth):
    return line
  else:
    return fill * fillstart + line + fill * fillend

def getColor(material):
  """
  Get a color and fill string to use in printing materials.
  
  Provides the characters for filling an area and the color 
  codes for styling that area for the given material type.

    Args:
      val: the integer code for the material (0-3)
    
    Returns:
      A tuple containing the color code and fill string, intended 
      to be destructured.
      (
        color_code (str): a string of ascii escape characters to change the 
          color of output
        fill (str): a single-character string that can be used to fill areas
          to maintain the correct look
      ) (tuple : str,str)
  """
  color_code = COLORS.RESET
  fill = " " # no fill
  if material == COPPER:
    # copper
    color_code = COLORS.ORANGE # yellow (not bold)
    fill = "▒" # light fill
  elif material == SILVER:
    # silver
    color_code = COLORS.WHITE # white
    fill = "▒" # light fill
  elif material == GOLD:
    # gold
    color_code = COLORS.YELLOW # bold yellow
    fill = "▓" # medium fill
  elif material == DIAMOND:
    # diamond
    color_code = COLORS.LIGHTBLUE # bold blue
    fill = "█" # solid fill
  else:
    warn("Incorrect material type: getColor")
  return (color_code, fill)

def printDice(hand):
  """
  Print the dice represented in the iterable hand
  
  Prints a text representation of each die result in 
  hand in a centered horizontal line
  
  Args:
    hand: an iterable yielding material values from printtools
    representing the values for each die
  
  Returns:
    None
  """
  die_text = [" \033[0m▁▁▁▁ ",
              "▕{0}{1}\033[0m▏",
              "▕{0}{1}\033[0m▏",
              " ▔▔▔▔ "]
  # manualwidth = len(hand) * 10 - 4
  # padding = " " * ((screenwidth - manualwidth) // 2)
  for line in die_text:
    outline = ""
    for i, die in enumerate(hand):
      cc, fill = getColor(die)
      fill *= 4
      outline += line.format(cc, fill) + ("" if i == len(hand) - 1 else "    ")
    print(center(outline, screenwidth))

def printTitle(color=COLORS.YELLOW):
  """
  Print the title screen for Swindlestones
  
  This clears the screen and fills its entirety. 
  It also automatically resizes to the console window's size, 
  though only before printing (it is not responsive)
  
  Args:
    color: 
      The color escape sequence to print the title in.
      The welcome text below will be gray regardless
  """
  clear()
  width = screenwidth
  height = screenheight
  swindlestones = [
    "  __-/                   |\   ,,         __-/    ,                          ",
    " (__/   ;                 \\\\  ||        (__/    ||                         ",
    "(_ --_  \\\\/\/\ \\\\ \\\\/\\\\  / \\\\ ||  _-_  (_ --_  =||=  /'\\\\ \\\\/\\\\  _-_   _-_, ",
    "  --_ ) || | | || || || || || || || \\\\   --_ )  ||  || || || || || \\\\ ||_.  ",
    " _/  )) || | | || || || || || || ||/    _/  ))  ||  || || || || ||/    ~ || ",
    "(___-   \\\\/\\\\/ \\\\ \\\\ \\\\  \\\\/  \\\\ \\\\,/  (___-    \\\\, \\\\,/  \\\\ \\\\ \\\\,/  ,-_-  ",
    "▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁"
  ]
  for i in range(max((int(height / 4 - 3), 0))):
    print()
  for line in swindlestones:
    cprint(line.center(width), color)
  for i in range(max((int(height / 4 - 4), 0))):
    print()
  for i in range(max((int(height / 4 - 1), 0))):
    print()
  cprint("Welcome".center(width), "\033[1;2;37m")
  cprint("Press enter to continue".center(width), "\033[1;2;37m")
  for i in range(max((int(height / 4 - 1), 0))):
    print()

def printCentered(
    text, 
    width=screenwidth, 
    height=screenheight, 
    padding=0,
    linespacing=2
  ):
  """
  Prints the given text horizontally and vertically centered
  
  The text given will be output with the given `width`, not breaking words,
  and a minimum height of `height`. These both default to the full width and
  height of the console window. The text will have a distance of
  `padding` percentage from the edge on each side (default: 0), and line spacing
  of `linespacing`, where `linespacing` is a positive integer (default: 2).
  """
  textlines = [""]
  linewidth = 0
  currentline = 0
  paragraphs = text.split("\n")
  
  padd_cols = int(screenwidth * padding / 100)

  textwidth = width - padd_cols * 2
  
  # break the text into lines no wider than the width available from the given padding
  for n, lines in enumerate(paragraphs):
    for word in lines.split(" "):
      plainword = re.sub("\033((?![a-zA-Z]).)*[a-zA-Z]", "", word)
      linewidth += len(plainword)
      if (linewidth > textwidth):
        textlines[currentline] = textlines[currentline][:-1]
        linewidth = len(plainword)
        currentline+=1
        textlines.append(word)
      else:
        textlines[currentline] += word
      linewidth += 1
      textlines[currentline] += " "
    if n == len(paragraphs) - 1:
      continue
    for i in range(linespacing):
      textlines.append("")
      currentline+=1
      linewidth = 0
  # remove the trailing space
  textlines[len(textlines) - 1] = textlines[len(textlines) - 1][:-1]
  # print it out vertically centered
  for i in range(max((int(height / 2 - len(textlines) / 2), 0))):
    print()
  for line in textlines:
    # print horizontally centered
    # fixed to support escape characters
    print(center(line, width))
  for i in range(max((int(height / 2 - len(textlines) / 2), 0))):
    print()

def old_man(message, end="\n"):
  """Prints the message with the old man's name and color before it"""
  # message = message.replace(COLORS.RESET, old_man_color)
  print(old_man_color + "The Old Man: " + COLORS.RESET + message, end=end)

def traveler(message):
  """Get's input by printing the traveler's name and color before a hint, which is placed in parentheses"""
  # message = message.replace(COLORS.RESET, traveler_color)
  return input(traveler_color + f"Traveler ({message}): " + COLORS.RESET)

def narrate(message):
  """Print a message in the narration style"""
  message = message.replace(COLORS.RESET, narrator_color)
  cprint(message, narrator_color)