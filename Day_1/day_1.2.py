import regex as re

def convert_to_num_char(s):
    conversions = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    try:
        int(s)
        return s
    except:
        return conversions[s]

doc = open('Day_1/day_1_input.txt')
tot = 0
for s in doc:
    nums = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', s, overlapped=True)
    tot = tot + int(convert_to_num_char(nums[0]) + convert_to_num_char(nums[-1]))
print(tot)