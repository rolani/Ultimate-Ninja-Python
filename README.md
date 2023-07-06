# Ultimate-Ninja-Python
# Implementing the Ultimate Ninja Battle Combat Game in Python

## Short description:
You are required to prepare a plan for a game of Ultimate Ninja Battle Combat!!! (The exclamation
points are important. The player will be fighting against the computer, and the winner gets
bragging rights. You will create a plan for a game played between the player and the computer.
The player will start the game with a balance of $100. The player will choose a move, and so will the
computer, and the winner of that round will be announced followed by the updated balance
(depending on whether the player won or lost and how much he or she bet). The player should not be
able to bet more than they have in their balance.
The player will choose their move from a list of six possibilities, and the computer will randomly
choose a move as well. Once the player has chosen their move the computers move will be revealed,
and the winner declared. The possible moves are:
1. Punch of Fury
2. Kick of Punishment
3. Sword of Justice
4. Shuriken of Vengeance
5. Nunchucks of Anger
6. Knife of Freedom

The chart below shows how each move performs against the others.

![image](https://github.com/rolani/Ultimate-Ninja-Python/assets/34588531/faf4d7ed-efc1-43d3-a7c2-a32bc15e6f88)



Once the player chooses their move your game will check the computers move and see who wins.
You are welcome to choose other names for the attacks as long as they make sense. For instance, you
may have “Knife of Assessment” rather than “Knife of Freedom”.
At the end of the round the winner is declared and the updated current balance is displayed.
The menu will then be presented again, allowing the player to get Information, Play or Quit. The
player will be forced to quit if the player balance reaches $0.
When the game quits, the game should display “Goodbye [player name]. Your final balance is $
[player’s final balance]. The game will then display the player’s balance history (their balance at the
end of each round).
See the next section for detailed instructions regarding the game functionality.

## Detailed Instructions:
1. Ask the player’s name and welcome them to the game using their name. The player’s
beginning balance of $100 should be displayed.
2. Show game menu
(I)nstructions
(P)lay game
(Q)uit game
ALL other choices will produce an error. The menu will be displayed after every menu choice,
except (Q).
If the player chooses ‘I’ display the following instructions:
Welcome to Ultimate Ninja Battle Combat!!! You will be fighting against the computer,
and the winner gets bragging rights. For each turn you will be asked to use one of the 6
attacks below:

(1) Punch of Fury
(2) Kick of Punishment
(3) Sword of Justice
(4) Shuriken of Vengeance
(5) Nunchucks of Anger
(6) Knife of Freedom.
Choose wisely.

3. If the player chooses ‘P’ from the menu display the player’s total and then ask the player how
much they want to bet. Inform the player that the bet amount must be in multiples of 5. The
player should not be able to bet more than their current balance.
4. Next, ask the player to choose an attack.
(1) Punch of Fury
(2) Kick of Punishment
(3) Sword of Justice
(4) Shuriken of Vengeance
(5) Nunchucks of Anger
(6) Knife of Freedom.
5. Once the player has entered a number the game should display the message “You chose: ” and
their move. Make sure you use the name of the move not just the number they entered. If they
entered anything other than a number between 1 and 6 then display an error message and ask
the user for their move until they enter a valid value.
6. Display the message “The computer chose: ” and the computer’s move.
7. Display the result of the combat, showing that either the computer or the player won.
8. Display the game menu again. The game menu will keep being displayed until the player
chooses quit.
9. If the player chooses “P” but has a $0 balance, the game will quit.
10. If the player chooses ‘Q’ from the menu then display the quit message “Goodbye! [player
name]. Your final balance is [player balance]”.
11. On a new line display:
“Your balance history is:
Starting Balance: $100
After round 1: $55
After round 2: $75
After every menu option other than ‘Q’ the program will return to the menu.
12. If the user enters anything other than the options above then display an error message.
