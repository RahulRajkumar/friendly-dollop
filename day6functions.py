from collections import deque

def scan_for_marker(datastream, buffer_size):

    data_buffer = deque(maxlen = buffer_size)
    for place, letter in enumerate(datastream):
        data_buffer.append(letter)
        # Converting to set forces out duplicates. If there are no
        # duplicates and the buffer is filled, then we have seen enough
        # characters to see the starting marker
        if len(set(data_buffer)) == buffer_size:
            # We want 1-indexing
            return place + 1
