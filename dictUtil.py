import math

red = "\u001b[31m"
yellow = "\u001b[33m"
black = "\u001b[30m"
reset = "\u001b[0m"

def generateGrid(width: int, height: int) -> dict:
    grid: dict = {}

    i = math.floor(height / 2) * - 1
    while i <= math.floor(height / 2):
        grid[i] = {}

        e = (math.floor(width / 2)) * - 1
        while e <= math.floor(width / 2):
            grid[i][e] = 0
            e += 1
        i += 1

    return grid

def changeDictValue(grid: dict,x: int, y: int, newValue: any) -> dict:
    grid[x][y] = newValue
    return grid

def displayDict(grid: dict, width: int, height: int, highlight: any) -> None:
    i = math.floor(height / 2)

    while i >= math.floor(height / 2) * -1:
        e = math.floor(width / 2) * -1
        while e <= math.floor(width / 2):
            value = grid[i][e]
            if value == highlight:
                print(yellow + str(value) + reset, end="")
            elif value == 0:
                print(" ", end="")
            else:
                print(str(value), end="")
            e += 1
        print(i)
        i -= 1