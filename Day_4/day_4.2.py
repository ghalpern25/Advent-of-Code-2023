cards = open('Day_4/day_4_input.txt').readlines()

total_points = 0
card_qty = [1]*len(cards)
for i in range(len(cards)):
    all_numbers = [x.strip() for x in cards[i].split(':')[1].split('|')]
    winning_numbers = all_numbers[0].split()
    my_numbers = all_numbers[1].split()
    matches = 0
    for winning_num in winning_numbers:
        if winning_num in my_numbers:
            matches += 1
    for j in range(i + 1, i + matches + 1):
        card_qty[j] += card_qty[i]

print(sum(card_qty))