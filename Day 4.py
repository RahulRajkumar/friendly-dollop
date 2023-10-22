# Solving Day 4: Camp Cleanup

import helper
FILENAME = "Day 4 Input.txt"
data = helper.ingest_input(FILENAME)
pairs = [line.split(",") for line in data]

def generate_section(section_string):
    """
    Take a section string formatted as "A-B", meaning sections [[A,B]],
    and produce the set {A,A+1,...,B}
    """
    begin, end = section_string.split("-")
    begin, end = int(begin), int(end)
    section = {i for i in range(begin, end+1)}
    return section

def full_overlap(set_one, set_two):
    return set.issubset(set_one, set_two) or set.issuperset(set_one, set_two)

full_overlap_count = 0
overlap_count = 0

for assignment in pairs:
    elf_one, elf_two = assignment
    section_one, section_two = [generate_section(elf_one), generate_section(elf_two)]
    full_overlap_count += full_overlap(section_one, section_two)
    overlap_count += not set.isdisjoint(section_one, section_two)

print(f"Number of assignments that completely overlap: {full_overlap_count}")
print(f"Number of assignments with any overlap: {overlap_count:d}")
