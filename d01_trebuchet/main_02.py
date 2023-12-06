import sys
import re

NUMBERS = {
    'one': '1',
    '1': '1',
    'two': '2',
    '2': '2',
    'three': '3',
    '3': '3',
    'four': '4',
    '4': '4',
    'five': '5',
    '5': '5',
    'six': '6',
    '6': '6',
    'seven': '7',
    '7': '7',
    'eight': '8',
    '8': '8',
    'nine': '9',
    '9': '9'
}

def main(val):
    sum = 0
    for line in val:
        nums = re.findall(r'(?:^|(?<=))(?=(one|two|three|four|five|six|seven|eight|nine|\d))(?:(?=)|$)', line)

        if len(nums) > 0:
            print(NUMBERS[nums[0]], NUMBERS[nums[-1]])
            sum += int(''.join((NUMBERS[nums[0]], NUMBERS[nums[-1]])))
    print(sum)

if __name__ == "__main__":
    val = sys.stdin.readlines()

    main(val)
