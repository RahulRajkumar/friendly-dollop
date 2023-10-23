# Solving Day 2: Rock Paper Scissors
#
# Compute the total score of a Rock Paper Scissors Tournament Guide

from day2functions import score_of, second_score_of
import helper
FILENAME = "Day 2 Input.txt"
guide = [line.split() for line in helper.ingest_input(FILENAME)]



# Part One
score = sum([score_of(entry) for entry in guide])
print(score)
# Part Two    
score = sum([second_score_of(entry) for entry in guide])
print(score)
