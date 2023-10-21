# Solving Day 1: Calorie Counting
#
# We want to find the total number of calories held by
# 1) The elf carrying the most calories
# 2) The three elves carrying the most calories
#
# Input file consists of blankline-delimited blocks of data. Each
# block of data represents the pack of a single elf, and is a
# newline-delimited list of item calorie counts.

FILENAME = "Day 1 Input.txt"

elf_pack_totals = []

with open(FILENAME, 'r') as file:
    current_elf_calories = 0
    for line in file:
        try:
            current_elf_calories += int(line)
        # When we hit a newline character, an error is thrown, at
        # which point we have seen the entirety of that elf's pack
        except:
            elf_pack_totals.append(current_elf_calories)
            current_elf_calories = 0

elf_pack_totals.sort(reverse=True)
max_calories = elf_pack_totals[0]
top_three = elf_pack_totals[0:3]
