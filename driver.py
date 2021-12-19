class Driver:
    def __init__(self, driver_no
                 , arrival_RD, time_between_arrivals, charging_RD
                 , charging_time, cargo_RD, cargo_TorD_Time, arrival_time
                 ):
        self.driver_no = driver_no
        self.charger_no = 1
        self.queue_time = 0

        self.arrival_RD = arrival_RD
        self.arrival_time = arrival_time
        self.time_between_arrivals = time_between_arrivals

        self.charging_RD = charging_RD
        self.charging_time = charging_time
        self.start_charging_time = 0
        self.end_charging_time = 0

        self.cargo_RD = cargo_RD
        self.cargo_TorD_Time = cargo_TorD_Time
        self.start_cargo_TorD_Time = 0
        self.end_cargo_TorD_Time = self.start_cargo_TorD_Time + self.cargo_TorD_Time


