# Solving Day 3 Rucksack Reorganization
#
# Determine the sum of the priorities of misplaced items

from day3functions import rucksack_compartments, identify_duplicates, get_priority
import helper
FILENAME = "Day 3 Input.txt"
# Rucksacks and rucksacks broken down into their two compartments
rucksacks = helper.ingest_input(FILENAME)
compartmentalized_rucksacks = [rucksack_compartments(sack) for
                                   sack in rucksacks]
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
