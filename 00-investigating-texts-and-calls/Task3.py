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

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
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


def index_matches_area_code(record, area_code, index):
    return area_code in record[index]


def calls_initiated_in_bangalore(data):
    return [x for x in data if index_matches_area_code(x, "080", 0)]


def call_already_exists(data, incoming, outgoing):
    for d in data:
        return True if d[0] == incoming and d[1] == outgoing else False


def do_part_a():
    bangalore_callers = sorted(
        calls_initiated_in_bangalore(calls), key=lambda x: x[0]
    )
    unique_numbers = []

    for call in bangalore_callers:
        for entry in unique_numbers:
            if call[0] == entry:
                break
        else:
            unique_numbers.append(call[0])

    print("The numbers called by people in Bangalore have codes:\n{0}".format(
        "\n".join(unique_numbers)
    ))


def do_part_b():
    bangalore_callers = calls_initiated_in_bangalore(calls)
    bangalore_caller_count = len(bangalore_callers)
    called_bangalore_number_count = 0

    for caller in bangalore_callers:
        if index_matches_area_code(caller, "080", 1):
            called_bangalore_number_count += 1

    msg = "{:2.2%} percent of calls from fixed lines in Bangalore are" \
          "calls to other fixed lines in Bangalore."

    print(msg.format(called_bangalore_number_count / bangalore_caller_count))


do_part_a()
print("\n")
do_part_b()
