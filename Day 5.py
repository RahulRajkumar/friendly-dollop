# Solve Day 5: Supply Stacks

from collections import deque

FILENAME = "Day 5 Input.txt"
# Choose which part of the challenge is being solved
part_one = False
part_two = True

n_stacks = 9
stacks = {i:deque() for i in range(1,n_stacks + 1)}
# Add a special "temp" stack for use in part two
if part_two:
    stacks["temp"] = deque()
max_stack_height = 8

def ingest_across_stacks(line):
    for i in range(n_stacks):
        char = line[1 + 4*i]
        if char != ' ':
            stacks[i + 1].appendleft(char)
            
def move_one_at_a_time(quantity, source, destination):
    for i in range(quantity):
        stacks[destination].append(stacks[source].pop())

def move_in_bulk(quantity, source, destination):
    """
    Bulk movement of crates for part two

    Implemented as moving one at a time to a special temp storage, and
    then from the temp storage to the destination

    """
    move_one_at_a_time(quantity, source, "temp")
    move_one_at_a_time(quantity, "temp", destination)

with open(FILENAME) as f:
    data = f.read().split("\n")
    data.pop()

for i in range(max_stack_height):
    ingest_across_stacks(data[i])

# instructions start on line 11, parse to form:
# [NUMBER_TO_MOVE, SOURCE, DESTINATION]
instructions = [[int(i) for i in line.split(" ") if i.isdecimal()] for line in data[10:]]

if part_one:
    for command in instructions:
        move_one_at_a_time(*command)
if part_two:
    for command in instructions:
        move_in_bulk(*command)

top = [stacks[i][-1] for i in range(1,n_stacks + 1)]
print("".join(top))
