doc = open('Day_1/day_1_input.txt')
tot = 0
for s in doc:
    first_num = -1
    last_num = -1
    first_found = False
    for c in s:
        if c.isdigit():
            if not first_found:
                first_num = c
                first_found = True
            last_num = c
    tot = tot + int(first_num + '' + last_num)
print(tot)