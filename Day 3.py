# Solving Day 3 Rucksack Reorganization
#
# Determine the sum of the priorities of misplaced items

import helper
FILENAME = "Day 3 Input.txt"
# Rucksacks and rucksacks broken down into their two compartments
rucksacks = helper.ingest_input(FILENAME)
compartmentalized_rucksacks = [rucksack_compartments(sack) for
                                   sack in rucksacks]

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

### Part One

# Guaranteed that each pack only has one duplicated element across the
# compartments, so can convert from list of sets to list of elements
# with .pop()
duplicates_in_rucksacks = [identify_duplicates(pack).pop() for pack in
                                                            compartmentalized_rucksacks]
priorities = [get_priority(element) for element in duplicates_in_rucksacks]

print(sum(priorities))

### Part Two

# Guaranteed to have elves groupable into groups of 3
n_groups = int(len(rucksacks) / 3)
grouped_packs = [rucksacks[3 * i : 3*i + 3]for i in range(n_groups)]

badges = [identify_duplicates(pack).pop() for pack in grouped_packs]
badge_priorities = [get_priority(element) for element in badges]

print(sum(badge_priorities))
