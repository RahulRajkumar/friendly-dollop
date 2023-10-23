# Solving Day 4: Camp Cleanup

from day4functions import generate_section, full_overlap
import helper
FILENAME = "Day 4 Input.txt"
data = helper.ingest_input(FILENAME)
pairs = [line.split(",") for line in data]


full_overlap_count = 0
overlap_count = 0

for assignment in pairs:
    elf_one, elf_two = assignment
    section_one, section_two = [generate_section(elf_one), generate_section(elf_two)]
    full_overlap_count += full_overlap(section_one, section_two)
    overlap_count += not set.isdisjoint(section_one, section_two)

print(f"Number of assignments that completely overlap: {full_overlap_count}")
print(f"Number of assignments with any overlap: {overlap_count:d}")
