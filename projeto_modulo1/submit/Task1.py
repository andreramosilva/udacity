"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    telnumbers=[]
    unic_numbers=[]
    for message in texts:
        #print(message[0])
        if message[0] not in telnumbers:
            telnumbers.append(message[0])
        if message[1] not in telnumbers:
            telnumbers.append(message[1])

    print(len(telnumbers))

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        if call[0][0] not in telnumbers:
            telnumbers.append(call[0][0])
        if call[0][1] not in telnumbers:
            telnumbers.append(call[0][1])
    print(len(telnumbers))

print("There are {} different telephone numbers in the records.".format(len(telnumbers)))
# O(2N)
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
