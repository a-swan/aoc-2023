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
        symbols = []
        for lineNumber, line in enumerate(file):
            for lineIndex, char in enumerate(line.strip()):
                if char == '*':
                    symbols += [(r, c, (lineNumber, lineIndex)) for r in range(lineNumber-1, lineNumber+2) for c in range(lineIndex-1, lineIndex+2)]
        #print(symbols)

        file.seek(0)

        gears = dict()
        part_reg = r'\d+'
        for lineNumber, line in enumerate(file):
            for match in re.finditer(part_reg, line.strip()):
                #index = [(lineNumber, j, symbol[2]) for j in range(*match.span()) for symbol in symbols if (lineNumber, j) == symbol[:2]]
                #print(index)
                #index = []
                found_gear = []
                for j in range(*match.span()):
                    for symbol in symbols:

                        # AND found_gear == False AND match.group() not in gear dictionary
                        if (lineNumber, j) == symbol[:2]:
                            #index.append((lineNumber, j, symbol[2]))
                            
                            if symbol[2] not in found_gear:
                                found_gear.append(symbol[2])

                                if gears.get(symbol[2], False):
                                    gears[symbol[2]].append(int(match.group()))
                                else:
                                    gears[symbol[2]] = [int(match.group())]

        sum = 0
        for g in gears:
            if len(gears[g]) == 2:
                sum += (gears[g][0] * gears[g][1])
        print(sum)

if __name__ == "__main__":
    schematic = sys.argv[1]
    #part1(schematic)
    part2(schematic)
