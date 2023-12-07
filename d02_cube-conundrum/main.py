import sys

def main(gameData, red=12, green=13, blue=14):
    CUBES = {
        'red': red,
        'green': green,
        'blue': blue
    }
    valid = []
    for gameLine in gameData:
        id, games = gameLine.split(":")
        split = games.strip().replace(";","").replace(",","").split(" ")

        cubeSet = {'red': 0, 'green': 0, 'blue': 0}
        for i,k in zip(split[0::2], split[1::2]):
            if cubeSet[k] < i:
                cubeSet[k] = i
        valid.append(cubeSet)
    print(valid)

if __name__ == "__main__":
    print("Games>>>")
    gameData = sys.stdin.readlines()

    main(gameData)
