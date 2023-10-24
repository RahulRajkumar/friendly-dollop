# Day 6: Tuning Trouble

from helper import ingest_input
from day6functions import scan_for_marker

packet_marker_size = 4
message_marker_size = 14

FILENAME = "Day 6 Input.txt"
data = list(ingest_input(FILENAME)[0])

print(scan_for_marker(data, packet_marker_size))
print(scan_for_marker(data, message_marker_size))


