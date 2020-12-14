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

    bangalore_fix = []
    bangalore_mob = []
    telemarketers = []
    called_by_bang = []
    called_to_bang = []
    mobile=['7', '8', '9']
    for call in calls:
        if call[0].startswith("(080)"):

            bangalore_fix.append(call)

        aux = len("080 ")+1
        is_mobile = len(call[0])//2

        if call[0][4] == "7" or call[0][4] == "8" or call[0][4] == "9":

            bangalore_mob.append(call)

        if call[0].startswith("140"):

            telemarketers.append(call)

    prefix_list = []
    for call in bangalore_fix:

        if call[1].startswith("(080)"):
            called_to_bang.append(call[1])
        if call[1].startswith("("):
            limit=call[1].index(")")

            called_by_bang.append(call[1][:limit])

        if call[1][0] in mobile:

            called_by_bang.append(call[1][0])

    called_set = set(called_by_bang)
    print("The numbers called by people in Bangalore have codes:")
    for x in called_set:
        print(x)
    print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round((len(called_to_bang)/len(called_by_bang))*100)))
#O(2N)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
