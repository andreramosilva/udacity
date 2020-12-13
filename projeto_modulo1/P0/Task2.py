"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    #print(texts[0])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    #print(calls[0])
    max_time=0
    phone_num_max_time=[]

    for call in calls:
        #print(call[-1])
        temp = call[-1]
        if int(max_time) < int(temp) :
            max_time=call[-1]
            phone_num_max_time= call
            #print(max_time)

    print(" {} spent the longest time, {} seconds, on the phone during September 2016.".format(phone_num_max_time[0],phone_num_max_time[-1]))

#O(N)
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

