import math

def calculateSquareFunctions(a, x, d, e, y, searchValue):
    try:
        calculations = {
            "a": lambda: ((x - d) ** 2 + e) / y,
            "x": lambda: [int(d + math.sqrt((y - e) / a)), int(d - math.sqrt((y - e) / a))],
            "d": lambda: -(math.sqrt((y - e) / a) - x),
            "e": lambda: (a * (x - d) ** 2) / 2,
            "y": lambda: a * (x - d) ** 2 + e
        }
    except ValueError:
        return []

    if searchValue in calculations:
        return calculations[searchValue]()
    else:
        raise Exception("No Valid Numbers")

def renderGrid(grid, values, height, width, isBold: bool):

    a = values["a"]
    d = values["d"]
    e = values["e"]
    i = e
    lastCords = {"x": [0, 0], "y": e}

    while i <= height // 2:
        if a < 0:
            y = -i
        else:
            y = i

        Xs = calculateSquareFunctions(a, None, d, e, y, "x")
        
        if len(Xs) == 0:
            continue
        rangePos = range(lastCords["x"][0] + 1, Xs[0])
        rangeNeg = range(Xs[1] + 1, lastCords["x"][1])

        #Render values which are on the same line as the previous one
        for value in rangePos:
            grid[y - 1][value] = 1

            if isBold:
                for cords in getSurroundingPoints(value, y - 1):
                    grid[cords[1]][cords[0]] = 1

        for value in rangeNeg:
            grid[y - 1][value] = 1

            if isBold:
                for cords in getSurroundingPoints(value, y - 1):
                    grid[cords[1]][cords[0]] = 1

        #Render normal values
        for x in Xs:
            grid[y][x] = 1

            if isBold:
                for cords in getSurroundingPoints(x, y):
                    try:
                        grid[cords[1]][cords[0]] = 1
                    except:
                        pass

        lastCords = {"x": Xs, "y": y}
        i += 1

    return grid


def getSurroundingPoints(x, y) -> list[list[int]]:
    surroundingPoints = []
    for e in range(-1, 2):
        for i in range(-1, 2):
            surroundingPoints.append([x + e, y + i])
    return surroundingPoints