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

        valid.append(int(id.split(" ")[1]))
        for i,k in zip(split[0::2], split[1::2]):
            if CUBES[k] < int(i):
                valid.pop()
                break

    print(sum(valid))

if __name__ == "__main__":
    print("Games>>>")
    gameData = sys.stdin.readlines()

    main(gameData)
