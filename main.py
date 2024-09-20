from dictUtil import *
from quadratischeFunktionen import *
import os
import shutil

width = shutil.get_terminal_size().columns - 1
height = shutil.get_terminal_size().lines

width = int(input("Breite: "))
height = int(input("Höhe: "))

grid = generateGrid(width, height)

values = {
    "a": int(input("Steigung a: ")),
    "x": None,
    "d": int(input("Verschiebung d (x Achse): ")),
    "e": int(input("Verschiebung e (y Achse): ")),
    "y": None
}
bold = ""
while bold != "y" and bold != "n":
    bold = input("Fett? (y/n): ")

if bold == "y":
    bold = True
else:
    bold = False

displayDict(renderGrid(grid, values, height, width, bold), width, height, 1)

