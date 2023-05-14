import pytest
import builtins
from project import win, required, player, play_again, game_level, game_rules
from unittest.mock import Mock, patch


def main():
    test_win()
    test_player()

def test_win():
    assert win(2, 2, 1) == False
    assert win(4, 2, 4) == False
    assert win(2, 1, 0) == True

def test_required():
    # Test when a valid integers are entered
    input_values = ["1", "2", "3", "10"]
    def mock_input(prompt):
        return input_values.pop(0)
    builtins.input = mock_input
    assert required() == 1
    assert required() == 2
    assert required() == 3
    assert required() == 10
    
def test_player():
    #test player function while level is 1
    input_values = ["Rock", "Paper", "Scissor"]
    def mock_input(prompt):
        return input_values.pop(0)
    builtins.input = mock_input
    assert player(1) == "Rock"
    assert player(1) == "Paper"
    assert player(1) == "Scissor"


    #test player function while level is 1
    input_values = ["Rock", "Paper", "Scissor", "Lizard", "Spock"]
    def mock_input(prompt):
        return input_values.pop(0)
    builtins.input = mock_input
    assert player(2) == "Rock"
    assert player(2) == "Paper"
    assert player(2) == "Scissor"
    assert player(2) == "Lizard"
    assert player(2) == "Spock"

def test_play_again():
    # test play_again function in case when user input is yes or no
    input_values = ["yes", "no"]
    def mock_input(prompt):
        return input_values.pop(0)
    builtins.input = mock_input
    assert play_again(1) == "yes"
    assert play_again(1) == "no"

    # test play_again function in case when user input is rules
    input_values = ["rules", "rules"]
    def mock_input(prompt):
        return input_values.pop(0)
    builtins.input = mock_input
   
def test_game_level():
    input_values = ["1", "2", "3"]
    def mock_input(prompt):
        if input_values:
            return input_values.pop(0)
        else:
            return ""

    builtins.input = mock_input

    # Test valid levels
    assert game_level() == "1"
    assert game_level() == "2"   


def test_game_rules():
    assert game_rules("1") == ("""Rules: Rock wins against scissors; 
       paper wins against rock; 
       and scissors wins against paper.
             """)
    assert game_rules("2") == ("""The rules: Scissors cuts paper, 
          paper covers rock, 
          rock crushes lizard, 
          lizard poisons Spock, 
          Spock smashes scissors, 
          scissors decapitates lizard, 
          lizard eats paper, 
          paper disproves Spock, 
          Spock vaporizes rock, 
          and as it always has, rock crushes scissors.""")
    

if __name__ == '__main__':
    main()
    