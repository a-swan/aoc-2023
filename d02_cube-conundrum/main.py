import sys

def main(gameData, red=12, green=13, blue=14):
    CUBES = {
        'red': red,
        'green': green,
        'blue': blue
    }
    valid = 0
    for gameLine in gameData:
        id, games = gameLine.split(":")
        split = games.strip().replace(";","").replace(",","").split(" ")

        cubeSet = {'red': 0, 'green': 0, 'blue': 0}
        for i,k in zip(split[0::2], split[1::2]):
            if cubeSet[k] < int(i):
                cubeSet[k] = int(i)
        #valid.append(cubeSet)
        valid += cubeSet['red'] * cubeSet['green'] * cubeSet['blue']
    print(valid)

if __name__ == "__main__":
    print("Games>>>")
    gameData = sys.stdin.readlines()

    main(gameData)
