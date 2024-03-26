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

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def is_match_for(date_string, month, year):
    from datetime import datetime
    dt = datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")
    return True if dt.year == year and dt.month == month else False


def run():
    matches = [x for x in calls if is_match_for(x[2], 9, 2016)]
    sorted_matches = sorted(matches, key=lambda match: int(match[3]), reverse=True)
    longest_call = sorted_matches[0]

    print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(
        longest_call[0], longest_call[len(longest_call) - 1]
    ))

if __name__ == '__main__':
    run()