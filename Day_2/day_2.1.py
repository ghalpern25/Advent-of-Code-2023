games = open('Day_2/day_2_input.txt')
id_sum = 0
for game in games:
    game_split = game.split(':')
    id = game_split[0][5:]
    sets = game_split[1].split(';')
    add = int(id)
    for set in sets:
        colors = [x.strip() for x in set.split(',')]
        for color in colors:
            num, color_str = color.split(' ')
            match color_str:
                case 'red':
                    if int(num) > 12:
                        add = 0
                        break
                case 'green':
                    if int(num) > 13:
                        add = 0
                        break
                case 'blue':
                    if int(num) > 14:
                        add = 0
                        break
    id_sum = id_sum + add
print(id_sum)