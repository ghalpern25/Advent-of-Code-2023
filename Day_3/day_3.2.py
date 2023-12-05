schematic = open('Day_3/day_3_input.txt').readlines()

schematic = ['.'*len(schematic[0])] + schematic + ['.'*len(schematic[0])]
for i in range(len(schematic) - 1):
    schematic[i] = '.' + schematic[i].strip() + '.'

def get_num(i, j, schematic):
    num = schematic[i][j]
    exhausted = False
    moving_j = j
    while not exhausted:
        moving_j = moving_j - 1
        digit = schematic[i][moving_j]
        if not digit.isdigit():
            exhausted = True
        else:
            num = digit + num
    exhausted = False
    moving_j = j
    while not exhausted:
        moving_j = moving_j + 1
        digit = schematic[i][moving_j]
        if not digit.isdigit():
            exhausted = True
        else:
            num = num + digit

    return int(num)

gear_sum = 0
for i in range(1, len(schematic) - 1):
    for j in range(1, len(schematic[0]) - 1):
        if schematic[i][j] == '*':
            parts = []
            #left and right
            if schematic[i][j - 1].isdigit():
                parts.append(get_num(i, j - 1, schematic))
            if schematic[i][j + 1].isdigit():
                parts.append(get_num(i, j + 1, schematic))

            #above
            if schematic[i - 1][j].isdigit():
                parts.append(get_num(i - 1, j, schematic))
            else:
                if schematic[i - 1][j - 1].isdigit():
                    parts.append(get_num(i - 1, j - 1, schematic))
                if schematic[i - 1][j + 1].isdigit():
                    parts.append(get_num(i - 1, j + 1, schematic))

            #below
            if schematic[i + 1][j].isdigit():
                parts.append(get_num(i + 1, j, schematic))
            else:
                if schematic[i + 1][j - 1].isdigit():
                    parts.append(get_num(i + 1, j - 1, schematic))
                if schematic[i + 1][j + 1].isdigit():
                    parts.append(get_num(i + 1, j + 1, schematic))

            if len(parts) == 2:
                gear_ratio = parts[0] * parts[1]
                gear_sum = gear_sum + gear_ratio

print(gear_sum)