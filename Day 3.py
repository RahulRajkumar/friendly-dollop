# Solving Day 3 Rucksack Reorganization
#
# Determine the sum of the priorities of misplaced items

FILENAME = "Day 3 Input.txt"

def rucksack_compartments(contents):
    """
    Given the contents of a rucksack (one line of characters),
    split the contents into the two compartments. A rucksack contains
    2n items, the first n are in the first compartment and the second
    n in the second compartment
    """

    number_of_items = len(contents)
    compartment_size = int(number_of_items / 2)
    compartment_one = contents[:compartment_size]
    compartment_two = contents[compartment_size:]

    return [compartment_one, compartment_two]

def identify_duplicates(collection):
    """
    Identify duplicated element between a members of a collection
    """
    return set.intersection(*[set(i) for i in collection])

def get_priority(item):
    """
    Return the priority of an item
    
    An item is either an uppercase or lowercase letter.
    Lowercase letters are prioritized as
    a = 1, b = 2, ...
    Lowercase letters have ascii values starting at 97
    Uppercase letters are prioritized as
    A = 27, B = 28, ...
    Lowercase letters have ascii values starting at 65
    """
    LOWER_START = 97
    UPPER_START = 65
    
    ascii_item = ord(item)

    # Lowercase letters are mapped to 1,...,26
    if ascii_item >= 97 and ascii_item <= 122:
        return ascii_item - LOWER_START + 1
    # Uppercase letters are mapped to 27,...,52
    if ascii_item >= 65 and ascii_item <= 90:
        return ascii_item - UPPER_START + 27

# Input file is newline separated. Each line contains a rucksack
with open(FILENAME) as f:
    rucksacks = [rucksack_compartments(line) for line in f.read().split("\n")]
    # Remove the final, empty element from rucksacks
    rucksacks.pop()

priorities = [get_priority(duplicates(*pack).pop()) for pack in
              rucksacks]

print(sum(priorities))
