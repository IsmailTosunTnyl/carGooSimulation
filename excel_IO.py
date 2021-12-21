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

    def export_report_page2(self, drivers, chargers, cargos):

        charger_util = [0 for _ in chargers]
        cargo_util = [0 for _ in cargos]
        total_driver_count = len(drivers)
        total_charger_waiting_time = 0
        total_cargo_waiting_time = 0
        charger_queue_counter = 0
        cargo_queue_counter = 0
        for driver in drivers:
            charger_util[driver.charger_no - 1] += driver.charging_time
            cargo_util[driver.cargo_no - 1] += driver.cargo_TorD_Time
            total_charger_waiting_time += driver.queue_time
            total_cargo_waiting_time += driver.cargo_queue_time

            if driver.queue_time != 0:
                charger_queue_counter += 1
            if driver.cargo_queue_time != 0:
                cargo_queue_counter += 1

        for charger in chargers:
            charger_util[charger.charger_no - 1] = charger_util[charger.charger_no - 1] / charger.available_time
        for cargo in cargos:
            cargo_util[cargo.cargo_no - 1] = cargo_util[cargo.cargo_no - 1] / cargo.available_time

        average_waiting_time_for_charger = total_charger_waiting_time / total_driver_count
        average_waiting_time_for_cargo = total_cargo_waiting_time / total_driver_count
        probability_of_waiting_charger = charger_queue_counter / total_driver_count
        probability_of_waiting_cargo = cargo_queue_counter / total_driver_count

        result = {"Driver Count": [total_driver_count, ],
                  "Average Waiting Time for Charger": [average_waiting_time_for_charger, ],
                  "Probability of waiting for Charger": [probability_of_waiting_charger, ],
                  "Average Waiting Time for Cargo": [average_waiting_time_for_cargo, ],
                  "Probability of waiting for Cargo": [probability_of_waiting_cargo, ]}
        for i in chargers:
            key1 = "Charger " + str(i.charger_no) + " Utilization"
            result[key1] = [charger_util[i.charger_no - 1], ]
        for i in cargos:
            key1 = "Cargo " + str(i.cargo_no) + " Utilization"
            result[key1] = [cargo_util[i.cargo_no - 1], ]
        return result

    def export_report(self, drivers, chargers, cargos):
        result_page2 = self.export_report_page2(drivers, chargers, cargos)
        result = {"Driver No": list(), "Charger No": list(), "Random Digit For Arrival": list(),
                  "Time Between Arrivals": list(), "Arrival time": list(), "Random Digit For Charging Time": list()}

        # Creating multi cargo and charger
        for i in chargers:
            key1 = "Charger " + str(i.charger_no) + " Start charging"
            key2 = "Charger " + str(i.charger_no) + "  Charging Time"
            key3 = "Charger " + str(i.charger_no) + " End charging"
            result[key1] = list()
            result[key2] = list()
            result[key3] = list()

        result["Random Digit For Cargo Take or Delivery Time"] = list()

        for i in cargos:
            key1 = "Cargo " + str(i.cargo_no) + " Start cargo TorD time"
            key2 = "Cargo " + str(i.cargo_no) + "  cargo TorD time"
            key3 = "Cargo " + str(i.cargo_no) + " End cargo TorD time"
            result[key1] = list()
            result[key2] = list()
            result[key3] = list()

        result["Cargo Queue"] = list()
        result["Charger Queue"] = list()

        for driver in drivers:
            result["Driver No"].append(driver.driver_no)
            result["Charger No"].append(driver.charger_no)
            result["Random Digit For Arrival"].append(driver.arrival_RD)
            result["Time Between Arrivals"].append(driver.time_between_arrivals)
            result["Arrival time"].append(driver.arrival_time)
            result["Random Digit For Charging Time"].append(driver.charging_RD)
            # result["Charging Time"].append(driver.charging_time)
            result["Random Digit For Cargo Take or Delivery Time"].append(driver.cargo_RD)
            # result["Cargo DorT Time"].append(driver.cargo_TorD_Time)
            result["Cargo Queue"].append(driver.cargo_queue_time)
            result["Charger Queue"].append(driver.queue_time)

            for charger in chargers:
                key1 = "Charger " + str(charger.charger_no) + " Start charging"
                key2 = "Charger " + str(charger.charger_no) + "  Charging Time"
                key3 = "Charger " + str(charger.charger_no) + " End charging"
                if charger.charger_no == driver.charger_no:
                    result[key1].append(driver.start_charging_time)
                    result[key2].append(driver.charging_time)
                    result[key3].append(driver.end_charging_time)
                else:
                    result[key1].append(" ")
                    result[key2].append(" ")
                    result[key3].append(" ")

            for cargo in cargos:
                key1 = "Cargo " + str(cargo.cargo_no) + " Start cargo TorD time"
                key2 = "Cargo " + str(cargo.cargo_no) + "  cargo TorD time"
                key3 = "Cargo " + str(cargo.cargo_no) + " End cargo TorD time"
                if cargo.cargo_no == driver.cargo_no:
                    result[key1].append(driver.start_cargo_TorD_Time)
                    result[key2].append(driver.cargo_TorD_Time)
                    result[key3].append(driver.end_cargo_TorD_Time)
                else:
                    result[key1].append(" ")
                    result[key2].append(" ")
                    result[key3].append(" ")
        result = pd.DataFrame(result)
        result_page2 = pd.DataFrame(result_page2)
        writer = pd.ExcelWriter("report.xlsx")
        result.to_excel(writer, sheet_name="Data")
        result_page2.to_excel(writer, sheet_name="Analyze")
        writer.save()


if __name__ == "__main__":
    a = ExcelIO().get_arrival_RD()
    b = ExcelIO().get_charge_RD()
    c = ExcelIO().get_cargo_RD()
    print(c)
