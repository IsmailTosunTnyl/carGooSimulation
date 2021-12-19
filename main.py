from excel_IO import ExcelIO
from driver import Driver
from charger import Charger
import random

arrival_RD = ExcelIO().get_arrival_RD()
charger_RD = ExcelIO().get_charge_RD()
cargo_RD = ExcelIO().get_cargo_RD()


def random_to_data(dictionary, random_num):
    for i in range(len(dictionary[list(dictionary.keys())[0]])):

        if dictionary[list(dictionary.keys())[1]][i][0] <= random_num <= dictionary[list(dictionary.keys())[1]][i][1]:
            return dictionary[list(dictionary.keys())[0]][i]


def check_charger(chargers, current_time):
    for j in chargers:
        if j.available_time <= current_time:
            return True
    return False


def get_nearest_charger(chargers):
    index = 0
    charger = chargers[0]
    for i in range(len(chargers)):
        if charger.available_time >= chargers[i].available_time:
            index = i

    return index


drivers = list()
chargers = list()

for i in range(3):
    chargers.append(Charger((i + 1)))

arrival_r = random.randint(1, 100)
charger_r = random.randint(1, 100)
cargo_r = random.randint(1, 100)

# initializing first driver
drivers.append(
    Driver(0, 0, 0, charger_r, random_to_data(charger_RD, charger_r),
           cargo_r, random_to_data(cargo_RD, cargo_r), 0))
drivers[0].end_charging_time = drivers[0].charging_time

timer = 0
driver_no = 1
# Driver random datas
while timer < 1000:
    arrival_r = random.randint(1, 100)
    charger_r = random.randint(1, 100)
    cargo_r = random.randint(1, 100)

    arrival_timer = random_to_data(arrival_RD, arrival_r)
    drivers.append(
        Driver(driver_no, arrival_r, arrival_timer, charger_r,
               random_to_data(charger_RD, charger_r),
               cargo_r, random_to_data(cargo_RD, cargo_r), arrival_time=timer + arrival_timer))
    timer += drivers[len(drivers) - 1].time_between_arrivals
    print("T", timer, drivers[len(drivers) - 1].time_between_arrivals)
    driver_no += 1

current_time = 0
# drivers charging data
for driver in drivers:
    charger = get_nearest_charger(chargers)
    if driver.arrival_time < chargers[charger].available_time:
        driver.queue_time = chargers[charger].available_time - driver.arrival_time

    charge_end = chargers[charger].available_time + driver.charging_time
    charge_start = chargers[charger].available_time
    chargers[charger].available_time = charge_end

    driver.end_charging_time = charge_end
    driver.start_charging_time = charge_start
    driver.charger_no = chargers[charger].charger_no

for i in drivers:
    print("d_no", i.driver_no, "ch_no", i.charger_no, "queue", i.queue_time, "a_time", i.arrival_time, "a_bet",
          i.time_between_arrivals, "ch_time", i.charging_time, "enc_ch", i.end_charging_time)
