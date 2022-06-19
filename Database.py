import os
import pickle
from pprint import pprint


def convertToDict(string: str) -> dict:
    """
    This function converts string into dict:
    :param string:
    :return:
    """
    string = string.removesuffix("\n")
    string = string.split(",")
    res = {
        "Name":string[1],
        "Genre":string[2],
        "Year":string[3],
        "Cinema":string[4],
        "Starts":string[5]
    }
    return res


if not os.path.exists("database.bin"):
    with open("cinema.txt", "r") as cinfile:
        filedata = cinfile.readlines()

    database = []
    for info in filedata:
        database.append(convertToDict(info))
    pprint(database)
    with open("database.bin", "wb") as binFile:
        pickle.dump(database, binFile)

with open("database.bin", "rb") as rfile:
    database = pickle.load(rfile)


def updateDatabase():
    with open("database.bin", "wb") as wFile:
        pickle.dump(database, wFile)
print(database[0].get("Name"))