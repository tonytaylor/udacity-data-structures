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
COLUMN_CALL_ORIGINATING_NUMBER = 0
COLUMN_CALL_RECEIVING_NUMBER = 1
COLUMN_CALL_TIMESTAMP = 2
COLUMN_CALL_DURATION = 3
COLUMN_TEXT_ORIGINATING_NUMBER = 0
COLUMN_TEXT_RECEIVING_NUMBER = 1
COLUMN_TEXT_TIMESTAMP = 2


def get_originating_calls(data):
    return [x[COLUMN_CALL_ORIGINATING_NUMBER] for x in data]


def filter_originating_calls_not_in_data_column(originating_calls, data, column_index):
    output = []

    for call in originating_calls:
        for x in data:
            if x[column_index] == call:
                break
        else:
            output.append(call)

    return output


def find_possible_telemarketers():
    originating_calls = get_originating_calls(calls)
    output = []

    filtered_receiving_calls = filter_originating_calls_not_in_data_column(
        originating_calls, calls, COLUMN_CALL_RECEIVING_NUMBER
    )
    filtered_originating_texts = filter_originating_calls_not_in_data_column(
        originating_calls, texts, COLUMN_CALL_ORIGINATING_NUMBER
    )
    filtered_receiving_texts = filter_originating_calls_not_in_data_column(
        originating_calls, texts, COLUMN_TEXT_RECEIVING_NUMBER
    )
    all_filters = filtered_receiving_calls + filtered_originating_texts + filtered_receiving_texts

    for c in all_filters:
        for entry in output:
            if entry == c:
                break
        else:
            output.append(c)

    return sorted(output)


def get_telemarketer_report(possible_telemarketers):
    return "These numbers could be telemarketers:\n{0}".format(
        "\n".join(possible_telemarketers)
    )


print(get_telemarketer_report(find_possible_telemarketers()))
