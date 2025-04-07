# Open the file and read the content
with open('/advent-of-code-2024/day-1/input-2.txt', 'r') as file:
    lines = file.readlines()

# Initialize empty lists
list1 = []
list2 = []

# Iterate through each line and split by spaces
for line in lines:
    words = line.split()  # This will split by any whitespace
    list1.extend(words[:len(words)//2])
    list2.extend(words[len(words)//2:])


int_list1 = [int(x) for x in list1]
int_list2 = [int(x) for x in list2]

# Print the resulting lists
int_list1.sort()
int_list2.sort()


dist_list = [abs(int_list1 - int_list2) for int_list1, int_list2 in zip(int_list1, int_list2)]
dist_result = sum(dist_list)



similarity_list = []

for number in int_list1:
    count = int_list2.count(number)
    similarity_list.append(number*count)

print('similarity result:', sum(similarity_list))
