# Swindlestones

A python game based on the game of the same name

## Gameplay

The player and their opponent each have a pre-defined number of four-sided dice. Each side of each die is made of a different precious metal: (copper, silver, gold, and diamond).

To start, both players secretly roll and look at their dice. Then, they each take turns either making a bet or call. To make a bet, they make a claim about how many of a certain material was rolled in total. Claims must always be “greater” than the previously made claim. A greater number or more valuable material will be defined as greater, with a greater number always taking precedence.

Ex: One diamond is not “greater” than two coppers.

To “call” their opponent, the player must simply state “I call”. This forces the hands to be revealed, confirming or disproving their opponent’s claim. If the claim was true, the caller loses a die; if the claim was false, the opponent loses a die. After a call, the dice are re-rolled (dice are not re-rolled after a claim).

The goal is to be the last player with dice remaining.

## Program Execution

Once started, the game will open with an introductory text explaining that the player is a traveler with some coins who enters into the tavern. At the gambling tables is an old man, who invites them over to play a game of “Swindlestones”. 

The old man opens with: “So you’ve not played Swindlestones before?”. The player is then able to confirm or deny, triggering a tutorial if they admit to never playing the game.

The game then opens providing five dice, starting with a roll (the results of the player’s hand will be printed on screen) and the Old Man’s claim. The players would then play the game as outlined above.

Once the bot or the player runs out of dice they lose. After the game, the bot responds gleefully or sulks (depending on win condition), and then the player has the option to play again.

If the player wins, the number of dice used by each player increases, and if they lose, it decreases (to a limit of 8 and 3 respectively).

## Example Run

Each hand would be a list filled with randomly selected letters representing the material type, [C, S, G, D]. The player can see their own hand, and the bot can see its own hand, but neither can be certain what the other has. So let’s say that the player rolls a C, a S, two Gs, and a D. The player can open by betting that there’s one G. The bot has two Gs, so it raises the bet to three Gs. From the bot’s bet, the player guesses that he has two Gs, so the player bets four Gs. The bot guesses that the player is lying, and calls. Then both hands are revealed. There really are four Gs, so the bot loses a dice. The dice are rerolled and another round begins.

## The Bot

The Old Man is a simple artificial intelligence bot designed to make basic assumptions and bets based on them. It will always call when a bet is impossible and will attempt to “judge” how likely a bet is based on comparing the known and possible numbers of materials.

### Calling

The bot should check to see if the bet is possible based on what it knows. For example, if both the bot and the player each have four dice, the bot has no Ds, and the player bets five Ds, then the bot should immediately call. Similarly, the bot should call when a given bet is highly unlikely. Such as the bot having no Ds and the player betting four Ds. It’s possible but unlikely that the player has four Ds, but if the bot bets five Ds then the player will probably call them and the bot would be lying. So a particularly high bet that is not supported by the bot’s hand will get called.

So the bot will call when:

- The bet is impossible
- The bet is unlikely

### Betting

The bot will choose to bet high or low, and the bot will choose whether it considers the player’s bet as true. It doesn’t really matter to the bot what it bet in the past, but it does matter what the player has bet. So the bot will keep track of that.
