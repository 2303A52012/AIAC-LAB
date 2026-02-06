class TaxiRide:
    def __init__(self,ride_id,driver_name,distance_km, waiting_time_minutes):
        self.ride_id = ride_id
        self.driver_name = driver_name
        self.distance_km = distance_km
        self.duration_minutes = waiting_time_minutes
    def display_details(self):
        print(f"Ride ID: {self.ride_id}")
        print(f"Driver Name: {self.driver_name}")
        print(f"Distance (km): {self.distance_km}")
        print(f"Waiting Time (minutes): {self.duration_minutes}")
    def calculate_fare(self):
        if self.distance_km<=10:
            fare = self.distance_km * 10
        elif self.distance_km<=20:
            fare = 10*10 + (self.distance_km-10)*12
        else:
            fare = 10*10 + 10*12 + (self.distance_km-20)*10
        fare += self.duration_minutes * 2
        return fare
# Example usage
if __name__ == "__main__":
    ride1 = TaxiRide("R001", "Alice", 8, 5)
    ride2 = TaxiRide("R002", "Bob", 15, 10)
    ride3 = TaxiRide("R003", "Charlie", 25, 15)

    for ride in [ride1, ride2, ride3]:
        ride.display_details()
        fare = ride.calculate_fare()
        print(f"Total Fare: ${fare}\n")

'''
Ride ID: R001
Driver Name: Alice
Distance (km): 8
Waiting Time (minutes): 5
Total Fare: $90

Ride ID: R002
Driver Name: Bob
Distance (km): 15
Waiting Time (minutes): 10
Total Fare: $180

Ride ID: R003
Driver Name: Charlie
Distance (km): 25
Waiting Time (minutes): 15
Total Fare: $300
'''