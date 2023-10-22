# Solving Day 2: Rock Paper Scissors
#
# Compute the total score of a Rock Paper Scissors Tournament Guide

FILENAME = "Day 2 Input.txt"

opponent_moves_dictionary = {'A' : "Rock", 'B' : "Paper", 'C' :
                             "Scissors"}
player_moves_dictionary = {'X' : "Rock", 'Y' : "Paper", 'Z' :
                             "Scissors"}
shape_values = {"Rock" : 1, "Paper" : 2, "Scissors" : 3}
outcome_dictionary = {0 : "Draw", 1 : "Win", 2 : "Lose"}
outcome_scores = {"Lose" : 0, "Draw" : 3, "Win" : 6}
instruction_dictionary = {'X' : "Lose", 'Y' : "Draw", 'Z' : "Win"}

outcome_dictionary_inv = {v : k for k,v in outcome_dictionary.items()}
player_moves_inv = {v : k for k,v in player_moves_dictionary.items()}
shape_values_inv = {v : k for k,v in shape_values.items()}

def value_of(entry):
    """
    Take an entry from the strategy guide of the form
    entry = ["opponent_move", "player_move"]
    and return the numeric value of the moves in the entry according
    to the shape_values dictionary
    """
    opponent_move, player_move = entry
    return [ shape_values[opponent_moves_dictionary[opponent_move]],
             shape_values[player_moves_dictionary[player_move]] ]

def outcome_of(entry):
    """
    Take an entry from the strategy guide of the form
    entry = ["opponent_move", "player_move"] and return whether the
    player won, lost, or drew

    A Player Wins iff the difference of the value of their move with
    the value of the opponent's move is 1 mod 3
    A Draw is 0 mod 3, and a Loss is 2 mod 3
    """
    opponent_move, player_move = value_of(entry)
    return outcome_dictionary[(player_move - opponent_move) % 3]

def score_of(entry):
    """
    Take an entry from the strategy guide of the form
    entry = ["opponent_move", "player_move"] and return the score of
    the entry. A score is the sum of the value of the result and the
    value of the player's move
    """
    outcome = outcome_of(entry)
    player_move = player_moves_dictionary[entry[1]]
    
    return outcome_scores[outcome] + shape_values[player_move]

def second_score_of(entry):
    outcome_value = outcome_scores[instruction_dictionary[entry[1]]]
    player_move = generate_player_move(entry)
    player_move_value = shape_values[player_moves_dictionary[player_move]]
    return outcome_value + player_move_value

def generate_player_move(entry):
    opponent_move, instruction = entry
    offset = outcome_dictionary_inv[instruction_dictionary[instruction]]
    opponent_move = shape_values[opponent_moves_dictionary[opponent_move]]
    player_move = (opponent_move + offset) % 3
    if player_move == 0:
        player_move = 3
    player_move = player_moves_inv[shape_values_inv[player_move]]
    return player_move
    
    
# Input file is newline separated. Each line contains a
# (space-separated) pair of letters denoting first the opponent's move
# and then your response
with open(FILENAME) as f:
    guide = [line.split() for line in f.read().split("\n")]
    # Remove the final, empty element from guide
    guide.pop()

scores = [second_score_of(entry) for entry in guide]
