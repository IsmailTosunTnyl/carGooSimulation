class Driver:
    def __init__(self, customer_no, charger_no
                 , arrival_RD, time_between_arrivals, charging_RD
                 , charging_time, start_charging_time, cargo_RD, cargo_TorD_Time
                 , start_cargo_TorD_Time):
        self.customer_no = customer_no
        self.charger_no = charger_no
        self.queue_time = 0

        self.arrival_RD = arrival_RD
        self.arrival_time = 0
        self.time_between_arrivals = time_between_arrivals

        self.charging_RD = charging_RD
        self.charging_time = charging_time
        self.start_charging_time = start_charging_time
        self.end_charging_time = self.start_charging_time + self.charging_time

        self.cargo_RD = cargo_RD
        self.cargo_TorD_Time = cargo_TorD_Time
        self.start_cargo_TorD_Time = start_cargo_TorD_Time
        self.end_cargo_TorD_Time = self.start_cargo_TorD_Time + self.cargo_TorD_Time
