with open('puzzle.txt', 'r') as file:
    file_code = file.read()

lines = file_code.splitlines()

number = 0
int_position_in_line = []
for line in lines:
    text_in_line = [int(char) for char in line if char.isdigit()]
    print(line, text_in_line)
    if text_in_line:
        number += text_in_line[0] + text_in_line[-1]

            
print(number)