# silver_service_taxi_test.py
from silver_service_taxi import SilverServiceTaxi

# Create a SilverServiceTaxi object with name "Hummer", 200 units of fuel, and fanciness of 4
my_silver_taxi = SilverServiceTaxi("Hummer", 200, 4)

# Drive the taxi 18 km
my_silver_taxi.drive(18)

# Print the taxi's details and the current fare
print("SilverServiceTaxi details:", my_silver_taxi)
print("Current fare:", my_silver_taxi.get_fare())
