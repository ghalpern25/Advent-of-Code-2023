import math

cards = open('Day_4/day_4_input.txt')

total_points = 0
for card in cards:
    all_numbers = [x.strip() for x in card.split(':')[1].split('|')]
    winning_numbers = all_numbers[0].split()
    my_numbers = all_numbers[1].split()
    matches = 0
    for winning_num in winning_numbers:
        if winning_num in my_numbers:
            matches += 1
    if matches > 0:
        total_points += int(math.pow(2, matches - 1))

print(total_points)