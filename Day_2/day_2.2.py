games = open('Day_2/day_2_input.txt')
power_sum = 0
for game in games:
    game_split = game.split(':')
    id = game_split[0][5:]
    sets = game_split[1].split(';')
    min_red, min_green, min_blue = 0,0,0
    for set in sets:
        colors = [x.strip() for x in set.split(',')]
        for color in colors:
            num, color_str = color.split(' ')
            num = int(num)
            match color_str:
                case 'red':
                    if num > min_red:
                        min_red = num
                case 'green':
                    if num > min_green:
                        min_green = num
                case 'blue':
                    if num > min_blue:
                        min_blue = num
    power = min_red * min_green * min_blue
    power_sum = power_sum + power
print(power_sum)