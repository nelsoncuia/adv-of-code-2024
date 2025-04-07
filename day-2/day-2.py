# Open the file and read the content
with open('/Users/nelsonrodrigues/Projects/advent-of-code-2024/day-2/input-day-2.txt', 'r') as file:
    lines = file.readlines()


list1 = []


# Iterate through each line and split by spaces
for line in lines:
    words = line.split()  # This will split by any whitespace
    list1.append(words)

int_list1 = []

for word in list1:
    int_list1.append([int(x) for x in word])


for report in int_list1:
    for i in range(1:len(report)):
        if report[i] 
    
        
    
    


print(int_list1)
