# Solving Day 1: Calorie Counting

FILENAME = "Day 1 Input.txt"

max_calories = 0

with open(FILENAME, 'r') as file:
    current_elf_calories = 0
    for line in file:
        try:
            current_elf_calories += int(line)
        # When we hit a newline character, an error is thrown, at
        # which point we have seen the entirety of that elf's pack. So
        # we compare the current elf's calories with the maximum and
        # replace if necessary
        except:
            max_calories = max(max_calories, current_elf_calories)
            current_elf_calories = 0

print(max_calories)
