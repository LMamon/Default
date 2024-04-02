with open('puzzle.txt', 'r') as file:
    file_code = file.read()

lines = file_code.splitlines()

number = 0

for i, line in enumerate(lines, start=1):
    num_in_line = [int(char) for char in line if char.isdigit()]

    if len(num_in_line) >= 2:
        line_total = num_in_line[0] + num_in_line[-1]
        number += line_total
    elif len(num_in_line) == 1:
        number += num_in_line[0]

    print(f"Line {i}:", line)

    print("Final combined digits:", number)