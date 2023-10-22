# Helper function for Advent of Code

def ingest_input(filename):
    """
    Input for Advent of Code is typically newline separated, with
    each line containing a relevant block of data. More processing may
    be necessary for individual challenges
    """
    with open(filename) as f:
        data = f.read().split("\n")
        # Remove empty element marking end of file
        data.pop()
    return data
