with open('puzzle.txt', 'r') as file:
    file_code = file.read()

lines = file_code.splitlines()

number = 0
int_position_in_line = []
for line in lines:
    #text_in_line = [int(char) for char in line if char.isdigit()]
    for char in line:
        if char.isdigit():
            int_position_in_line.append(int(char))
            #print(line, text_in_line)

if len(int_position_in_line) >= 2:
    number += int_position_in_line[0] + int_position_in_line[-1]

print(sum(int_position_in_line))            
print(number)