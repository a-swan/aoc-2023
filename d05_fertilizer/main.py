import sys

def parse(schematic):
    rules = {}
    with open(schematic, 'r') as file:
        label = ''
        seeds = []
        rules = {}
        for lineNumber, line in enumerate(file):
            # Detect seeds line
            if lineNumber == 0:
                seeds = list(map(int, line.split(":")[1].split()))
            elif len(line) > 1:
                # Detect label line
                if line.find('-') > 0:
                    label = line.rstrip().split()[0]
                    rules[label] = []
                # Detect conversion rules
                else:
                    rules[label].append(list(map(int, line.rstrip().split())))
                    #conversions.append(set(line.rstrip().split()))
    return seeds, rules

def part1(schematic):
    seeds, rules = parse(schematic)
    #print(seeds)
    #print(rules)
    seeds_conversions = []
    for seed in seeds:
        translations = [seed]
        for key, convs in rules.items():
            translations.append(translations[-1])
            print(seed, key)
            for conv in convs:
                tar = translations[-1]
                if tar in range(conv[1], conv[1] + conv[2]):
                    a = conv[0]
                    b = conv[1]
                    s = conv[2]
                    #print(f"tar: {tar} - b: {b} = {tar - b} + {a} = {a + (tar - b)}")
                    translations[-1:] = [conv[0] + (tar - conv[1])]
                    break
        #print(f"\n")
        seeds_conversions.append(translations)

    print(seeds_conversions)
    lowest = seeds_conversions[0][-1]
    for s_c in seeds_conversions:
        if s_c[-1] < lowest:
            lowest = s_c[-1]
    print(lowest)

if __name__ == "__main__":
    schematic = sys.argv[1]
    part1(schematic)
