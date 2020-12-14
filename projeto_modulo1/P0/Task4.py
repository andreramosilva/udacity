"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    possible_mkt = []
    # all calls made
    for call in calls:
        possible_mkt.append(call[0])
    possible_mkt_set = set(possible_mkt)
    # removing the ones who received calls
    for call in calls:
        if call[1] in possible_mkt_set:
            possible_mkt_set.remove(str(call[1]))
    # removing the ones who send txt and received
    for msg in texts:
        if msg[0] in possible_mkt_set:
            possible_mkt_set.remove(str(msg[0]))
        if msg[1] in possible_mkt_set:
            possible_mkt_set.remove(str(msg[1]))

    print("These numbers could be telemarketers: ")
    for number in possible_mkt_set:
        print(number)

# O(2N)
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

