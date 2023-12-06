import sys
import re

def main(val):
    sum = 0
    for line in val:
        nums = re.findall(r'\d', line)

        if len(nums) > 0:
            sum += int(''.join((nums[0], nums[-1])))
    print(sum)

if __name__ == "__main__":
    val = sys.stdin.readlines()

    main(val)
