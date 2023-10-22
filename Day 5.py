# Solve Day 5: Supply Stacks

from collections import deque

FILENAME = "Day 5 Input.txt"

n_stacks = 9
stacks = {i:deque() for i in range(1,n_stacks + 1)}
max_stack_height = 8

def ingest_across_stacks(line):
    for i in range(n_stacks):
        char = line[1 + 4*i]
        if char != ' ':
            stacks[i + 1].appendleft(char)
            
def move(quantity, source, destination):
    for i in range(quantity):
        stacks[destination].append(stacks[source].pop())

with open(FILENAME) as f:
    data = f.read().split("\n")
    data.pop()

for i in range(max_stack_height):
    ingest_across_stacks(data[i])

# instructions start on line 11, parse to form:
# [NUMBER_TO_MOVE, SOURCE, DESTINATION]
instructions = [[int(i) for i in line.split(" ") if i.isdecimal()] for line in data[10:]]

for command in instructions:
    move(*command)

top = [stacks[i][-1] for i in range(1,n_stacks + 1)]
print("".join(top))
