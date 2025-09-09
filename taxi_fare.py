def calculate_fare(distance):
    base_fare = 50
    per_km = 10
    return base_fare + (distance * per_km)

def fare_summary(trips):
    total = 0
    for i, dist in enumerate(trips, start=1):
        fare = calculate_fare(dist)
        print(f"Trip {i}: ${fare}")
        total += fare
    print(f"Total Fare: ${total}")

trips = [5, 10, 3]
fare_summary(trips)
