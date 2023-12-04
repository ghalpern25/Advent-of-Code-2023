schematic = open('Day_3/day_3_input.txt').readlines()

parts_sum = 0
for i in range(len(schematic)):
    in_num = False
    current_num = ''
    is_part = False
    for j in range(len(schematic[0]) - 1):
        c = schematic[i][j]
        if c.isdigit():
            in_num = True
            current_num = current_num + c

            if i > 0:
                if not schematic[i - 1][j].isdigit() and not schematic[i - 1][j] == '.':
                    is_part = True
            if j > 0:
                if not schematic[i][j - 1].isdigit() and not schematic[i][j - 1] == '.':
                    is_part = True
            if i < len(schematic) - 1:
                if not schematic[i + 1][j].isdigit() and not schematic[i + 1][j] == '.':
                    is_part = True
            if j < len(schematic[0]) - 2:
                if not schematic[i][j + 1].isdigit() and not schematic[i][j + 1] == '.':
                    is_part = True
            if i > 0 and j > 0:
                if not schematic[i - 1][j - 1].isdigit() and not schematic[i - 1][j - 1] == '.':
                    is_part = True
            if i < len(schematic) - 1 and j < len(schematic[0]) - 2:
                if not schematic[i + 1][j + 1].isdigit() and not schematic[i + 1][j + 1] == '.':
                    is_part = True
            if i < len(schematic) - 1 and j > 0:
                if not schematic[i + 1][j - 1].isdigit() and not schematic[i + 1][j - 1] == '.':
                    is_part = True
            if i > 0 and j < len(schematic[0]) - 2:
                if not schematic[i - 1][j + 1].isdigit() and not schematic[i - 1][j + 1] == '.':
                    is_part = True

        else:
            if in_num and is_part:
                parts_sum = parts_sum + int(current_num)
            in_num = False
            is_part = False
            current_num = ''
        
    if in_num and is_part:
        parts_sum = parts_sum + int(current_num)

print(parts_sum)