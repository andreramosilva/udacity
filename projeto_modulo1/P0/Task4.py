"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    msg_numb_list=[]
    call_no_message=[]
    for msg in texts:
        msg_numb_list.append(msg[0])
        #print(msg[0])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        if call[0] not in msg_numb_list:
            call_no_message.append(call[0])

    call_no_message_set = set(call_no_message)
    print("These numbers could be telemarketers: \n",call_no_message_set)
#O(2N)
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

