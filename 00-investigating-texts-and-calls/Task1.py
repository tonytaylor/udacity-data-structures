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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def transpose_list_at_column(data, column_index):
    return [row[column_index] for row in data]


def get_unique_phone_number_count(phone_number_collection):
    return len(set(phone_number_collection))


def collect_and_process(data):
    return sum(
        [get_unique_phone_number_count(collection) for collection in data]
    )


total_unique_phone_numbers = collect_and_process([
    transpose_list_at_column(texts, 0),
    transpose_list_at_column(texts, 1),
    transpose_list_at_column(calls, 0),
    transpose_list_at_column(calls, 1)
])
print("There are {0} different telephone numbers in the records.".format(
    total_unique_phone_numbers
))
