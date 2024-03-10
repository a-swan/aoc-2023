import sys
import math

def part1(schematic):
    with open(schematic, 'r') as file:
        points = 0
        for lineNumber, line in enumerate(file):
            cards = line.split(":")[1].split("|")
            winners = set(cards[0].split())
            players = set(cards[1].split())
            matches = len(winners) - len(winners - players)
            points += math.floor(2**(matches-1))
        print(points)

            

if __name__ == "__main__":
    schematic = sys.argv[1]
    part1(schematic)
