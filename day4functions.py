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
