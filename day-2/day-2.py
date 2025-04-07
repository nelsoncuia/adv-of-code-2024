# Open the file and read the content
with open(r"C:\Users\nelso\Projects\Advent of Code 2024\adv-of-code-2024\day-2\input-day-2.txt", 'r') as file:
    lines = file.readlines()


def is_list_decreasing(lst):
    # Check if the list is strictly decreasing
    return all(x > y for x, y in zip(lst, lst[1:]))

def is_list_increasing(lst):
    # Check if the list is strictly increasing
    return all(x < y for x, y in zip(lst, lst[1:]))


input_list = []


# Iterate through each line and split by spaces
for line in lines:
    words = line.split()  # This will split by any whitespace
    input_list.append([int(word) for word in words])
