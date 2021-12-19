import pandas as pd


class ExcelIO:
    def get_arrival_RD(self):

        data = pd.read_excel('./values.xlsx', sheet_name="Arrival")

        a = list()
        r = list()
        for i in range(len(data)):
            a.append(data["Time Between Arrivals"][i])
            temp = data["Random-digit"][i].split(",")
            r.append([int(temp[0]), int(temp[1])])

        return {"Time Between Arrivals": a, "Random-digit": r}

    def get_charge_RD(self):

        data = pd.read_excel('./values.xlsx', sheet_name="Charger")

        a = list()
        r = list()
        for i in range(len(data)):
            a.append(data["Charging Time"][i])
            temp = data["Random-digit"][i].split(",")
            r.append([int(temp[0]), int(temp[1])])

        return {"Time Between Arrivals": a, "Random-digit": r}

    def get_cargo_RD(self):

        data = pd.read_excel('./values.xlsx', sheet_name="Cargo")

        a = list()
        r = list()
        for i in range(len(data)):
            a.append(data["Cargo TorD Time"][i])
            temp = data["Random-digit"][i].split(",")
            r.append([int(temp[0]), int(temp[1])])

        return {"Time Between Arrivals": a, "Random-digit": r}


if __name__ == "__main__":
    a = ExcelIO().get_arrival_RD()
    b = ExcelIO().get_charge_RD()
    c = ExcelIO().get_cargo_RD()
    print(c)
