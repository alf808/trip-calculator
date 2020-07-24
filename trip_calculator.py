'''
Receive the following arguments from the user:

kilometers to drive
liters-per-kilometer usage of the car
price per liter of fuel

Calculate the cost of the trip and display it to the user in the console.
'''
print("This application will calculate the cost of your trip.")
distance = float(input("Please enter the distance in kilometers: "))
fuel_price_liter = float(input("Please enter the fuel price per liter: "))
usage_per_km_in_liters = float(input("Please enter liters-per-kilometer usage of car: "))
trip_cost = distance * fuel_price_liter * usage_per_km_in_liters
print(f"The total trip cost is {trip_cost}")