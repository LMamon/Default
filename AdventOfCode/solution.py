with open('puzzle.txt', 'r') as file:
    file_code = file.read()

lines = file_code.splitlines()

number = 0
int_position_in_line = []
for line in lines:
    
    for text in line:
        if text.isdigit():
            int_position_in_line.append(int(text))
    number = int_position_in_line[0] + int_position_in_line[-1]

            
print(number)