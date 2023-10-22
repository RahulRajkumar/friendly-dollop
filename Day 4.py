# Solving Day 4: Camp Cleanup

FILENAME = "Day 4 Input.txt"

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

with open(FILENAME) as f:
    pairs = [line.split(",") for line in f.read().split("\n")]
    # Remove final, empty element from pairs
    pairs.pop()

overlaps = 0
for assignment in pairs:
    elf_one, elf_two = assignment
    section_one, section_two = [generate_section(elf_one), generate_section(elf_two)]
    overlaps += full_overlap(section_one, section_two)
