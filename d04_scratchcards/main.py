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

def part2(schematic):
    card_dict = {}
    for line in reversed(open(schematic).readlines()):
        print(line.rstrip())
        card_num = int(line.split(":")[0].split()[1])
        cards = line.split(":")[1].split("|")
        winners = set(cards[0].split())
        players = set(cards[1].split())
        
        won_cards = list(range(card_num + 1, card_num + len(winners) - len(winners-players) + 1))
        print(won_cards)
        
        total_cards = 1
        for card in won_cards:
            print(card)
            total_cards += card_dict[card]
        card_dict[card_num] = total_cards
        print(card_dict)


    print(card_dict)
    print(sum(card_dict.values()))

if __name__ == "__main__":
    schematic = sys.argv[1]
    #part1(schematic)
    part2(schematic)
