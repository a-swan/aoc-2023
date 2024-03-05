import sys
import re

parts = []

def part1(schematic):
    with open(schematic, 'r+') as file:
        symbols = set()
        for lineNumber, line in enumerate(file):

            for lineIndex, char in enumerate(line.strip()):
                if char != '.' and not char.isnumeric():
                    #print(char)
                    symbols |= {(r, c) for r in range(lineNumber-1, lineNumber+2) for c in range(lineIndex-1, lineIndex+2)}

        file.seek(0) 

        part_reg = r'\d+'
        sum = 0
        for lineNumber, line in enumerate(file):
            for match in re.finditer(part_reg, line.strip()):
                #print(lineNumber, match)
                if any((lineNumber,j) in symbols for j in range(*match.span())):
                    #print(lineNumber)
                    #print(match.group())
                    sum += int(match.group())

    print(sum)
def part2(schematic):
    with open(schematic, 'r') as file:
        for lineNumber, line in enumerate(file):
            for lineIndex, char in enumerate(line.strip()):
                print(char)

if __name__ == "__main__":
    schematic = sys.argv[1]
    #part1(schematic)
    part2(schematic)
