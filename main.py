from excel_IO import ExcelIO
from Driver import Driver
import random

arrival_RD = ExcelIO().get_arrival_RD()
charger_RD = ExcelIO().get_charge_RD()
cargo_RD = ExcelIO().get_cargo_RD()


def random_to_data(dictionary):
    x = random.randint(0, 100)

    for i in range(len(dictionary[list(dictionary.keys())[0]])):

        if dictionary[list(dictionary.keys())[1]][i][0] <= x <= dictionary[list(dictionary.keys())[1]][i][1]:
            #print("random", x)
            return dictionary[list(dictionary.keys())[0]][i]


print(arrival_RD[list(arrival_RD.keys())[1]])
print(random_to_data(charger_RD))
