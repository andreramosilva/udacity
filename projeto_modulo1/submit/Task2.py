"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    max_time = 0
    phone_num_max_time = ''
    time_dic = {}

    for call in calls:
        if time_dic.get(call[0]):
            time_dic[call[0]] += int(call[-1])
        else:
            time_dic[call[0]] = int(call[-1])
        if time_dic.get(call[1]):
            time_dic[call[1]] += int(call[-1])
        else:
            time_dic[call[1]] = int(call[-1])

    for phone, time in time_dic.items():
        if int(max_time) < int(time):
            max_time = time
            phone_num_max_time = phone


    print(" {} spent the longest time, {} seconds, on the phone during September 2016.".format(phone_num_max_time, max_time ))

# O(N)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

