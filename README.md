# ROCK PAPER SCISSOR

#### Video Demo:  <https://youtu.be/HAXaNmiojiU>

### Description: 
I created Rock Paper Scissor game. In this program there are 2 different levels and several different features.

### Technical assignment: 
At the begining of the game it starts with the music(Queen - We Will Rock You). Then program greets the user and prompts to enter the required points. So, the game continues until someone reach the required number of points. Whoever reaches the required number of points first wins. Then program asks user to choose level. We have 2 different levels: Level 1 is classical version of Rock Paper Scissor and Level 2 is advanced version with additional options (Lizard and Spock).

### Level 1:
If user choose level 1 then program prints the rules:

#### Rules: 
        Rock wins against scissors;
        paper wins against rock;
        and scissors wins against paper.

User have to input his/her choice from Rock, Paper or Scissor. Computer also choose one randomly from the available choices. If computer and user choices will be same, then it's tie, but if computer choose scissor and user choose paper or computer choose rock and user choose scissor or computer choose paper and user choose rock then computer gets point, otherwise user gets point.

### Level 2:
If user choose level 2 then program prints the rules for advanced version with additional options (Lizard and Spock):

#### Rules: 
        Scissors cuts paper,
        paper covers rock,
        rock crushes lizard,
        lizard poisons Spock,
        Spock smashes scissors,
        scissors decapitates lizard,
        lizard eats paper,
        paper disproves Spock,
        Spock vaporizes rock,
        and as it always has, rock crushes 
        scissors.

So, in the Level 2 program does exaclty same thing what happens for Level 1, but there are just 2 more options.

## Features: 
### The program provides various features:
1. For example, If user does not want to play anymore he/she can input "Stop" anytime and program will exit.

2. If user needs rules, he/she can input "Rules" anytime and according to the chosen level program will print the rules. 

3. It's important that any user input can be case-insensitive(lower or upper case). 

4. I created file art.py where I drew available choices with ASCII Art, so after every decision program prints player and computer choices with paintings and their points. 

5. If player wins, program will congratulate, otherwise it says to user to "try again".  In both cases program asks user if he/she wants to play again. User can print Yes, No or Rules. If user write "yes" then program prompts user the required points and level and explains the rules. If user writes "no", then program will exit.

6. I used try/except statements for catching inapropiate values, so any time when user inputs value which is not defined or is inapropiate, program will ask him/her again.

7. During the game on the background there is music which makes the game more engaging.

# TODO:

## Questions
1. How many points are required to reach?
2. What is users choices?
3. What is computers choices?
4. What is player points?
5. What is computer points?
6. Does player want to play again?

### Inputs, Processes, Outputs
Nouns:
1. required points
2. player choice
3. computer choice
4. win/lose/tie
5. player points
6. computer points
7. win

Verbs:
1. prompts user for required points
2. prompts user to choose level
3. prints rules according the level
4. prompts user for choice
5. randomise computer choice
6. calculate points
7. revealing the winner
8. display points
9. display winner 
10. ask user if wants to play again
11. in the case when user needs rules print the rules
 
Inputs: 
1. required points
2. level
2. users choice
3. users wish to play again
4. user needs rules

Processes:
1. randomise computer choice
2. calculate points
3. revealing the winner

Output:
1. computer points
2. player points
3. computer choice
4. player choice
5. paintings
6. winner
7. congratulate
8. rules

Defined Functions:
1. play_music()
2. required()
3. game_level()
4. game_rules()
5. game_level_1()
6. game_level_2()
7. play_again()
8. win()
9. player()
10. draw() - In the art.py


### Necessary Libraries:
1. random - for randomising the computer choice.
2. sys - for system exit in the case when user does not want to play anymore and writes "Stop".
3. pygame - for music during the game.
4. draw from art.py - It was created by me for visualization of choices.

## Pseudocode

import modules.

Main function which calls other functions and uses while loop.
Define music_file and give it as a parameter to play_music function which will play that music.

Define variable required_points and gave it the value of required function. That function prompts the user required points for win.

Define variable level and gave it the value of game_level function. That function should prompt user to choose LEVEL1 or LEVEL2.

Call game_rules function with parameter of level which gives user rules.

Make while loop which will be the main engine of the program.

In the while loop we have to define variable player_points and computer_points as initialize points for player and computer.

User can choose 2 different level, so if user choose level 1 then we have to use game_level_1 function, otherwise we will use game_level_2 function.

We use play_again function which asks user if he/she wants to play again or not. if user does not want play anymore, then program will be finished.

We have to define game_level_1 function, which will be function for playing game on level1. We give that function 3 different parameters: required_points, player_points and computer_points.

Inside the function we use while loop with win function. while win function returns True than program prompts user for choice, at the same time computer makes choice and program calculates the score for both.loop will break if user write "stop" or someone will reach required points.

We have to define game_level_2 function, which will be the function for playing game on level2. We give that function 3 different parameters: required_points, player_points and computer_points.

Inside the game_level_2 function we use while loop with win function while win function returns True than program prompts user for choice, at the same time computer makes choice and program calculates the score for both. loop will break if user write "stop" or someone reach required points. difference from game_level_1 is that here we have more available_choices.

Win function has 3 different parameters: required_points, player_points and computer_points. This function will be called when someone will reach required points. It returns True and False bools.

Player function has 1 parameter - level. According to level, this function prompts user to make a choice. try/except statements help us to catch any errors.

required function greets the user and asks the needed required points to win. try/except statements help us to catch any errors.

play_again function has 1 parameter - level. It defines available answers. function asks user if he/she wants to play again or not. If user choose rules, then program calls game_rules function according to level. otherwise it returns user's answer and catches errors.

play_music takes 1 parameter called music_file and plays that music.

game_level function has 2 available levels. it asks user to choose LEVEL1 or LEVEL2 and returns users answer try/except statements catches errors.

game_rules function has 1 parameter - level. According to level it prints game rules.
