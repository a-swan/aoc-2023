import sys
import re

parts = []
symbols = []

def checkRow(row, start, end):
    for hit in symbols[row]:
        if hit >= start-1 and hit <= end+1:
            return True

def detectSymbols(row, startIndex, endIndex):
    # Check for symbols at startIndex-1 to endIndex+1
    if row-1 > 0:
        if checkRow(row-1, startIndex, endIndex):
            return True

    if checkRow(row, startIndex, endIndex):
        return True

    if row+1 < len(symbols):
        if checkRow(row+1, startIndex, endIndex):
            return True

def main(schematic):
    for lineNumber,line in enumerate(schematic):
        symbols.append([])
        subIndex = -1

        for index,char in enumerate(line.strip()):
            if char.isnumeric() and index > subIndex:
                partIndex = index

                # lookahead for full number
                subIndex = index
                while subIndex < len(line):
                    if not line[subIndex].isnumeric():
                        break
                    subIndex += 1
                #print(line[partInd:subIndex])
                #print(f"Index {partInd}, {subIndex}")
                parts.append((line[partIndex:subIndex], lineNumber, partIndex, subIndex))
            elif char != '.' and not char.isnumeric():
                #print(char)
                symbols[lineNumber].append(index)
            index = subIndex

    sum = 0
    for part in parts:
        valid = detectSymbols(part[1], part[2], part[3])
        print(f"Part {part[0]} is {valid}")

        if valid:
            sum += int(part[0])
    print(f"Sum: {sum}")

if __name__ == "__main__":
    print("Schematics>>>")
    schematic = sys.stdin.readlines()

    main(schematic)
