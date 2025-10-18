"""A carpool can have a booking list for a shared ride. Each booking
holds the number of passengers, the estimated pickup time and the
estimated dropoff time. We need to check that the number of passengers
does not exceed the number of seats in the car at any point in
time.

Below is one list that will fail booking as the number of passengers
at one point exceeds the number of seats in the car. And another
list that has fewer passengers than the number of seats at all times.
"""

bl1 = [
    {
        "Passengers": 3,
        "Estimated_pickup_time": 100,
        "Estimated_dropoff_time": 190,
    },
    {
        "Passengers": 3,
        "Estimated_pickup_time": 150,
        "Estimated_dropoff_time": 190,
    },
    {
        "Passengers": 3,
        "Estimated_pickup_time": 180,
        "Estimated_dropoff_time": 220,
    },
]
bl2 = [
    {
        "Passengers": 3,
        "Estimated_pickup_time": 100,
        "Estimated_dropoff_time": 120,
    },
    {
        "Passengers": 3,
        "Estimated_pickup_time": 150,
        "Estimated_dropoff_time": 190,
    },
    {
        "Passengers": 3,
        "Estimated_pickup_time": 180,
        "Estimated_dropoff_time": 220,
    },
]

def is_booking_possible(seats, booking_list):
    current = 0
    history = [{"Passengers": 0, "dropoff_time": 0}]
    for booking in booking_list:
        for record in history:
            if record["dropoff_time"] < booking["Estimated_pickup_time"]:
                current -= record["Passengers"]
                record["Passengers"] = 0
        current += booking["Passengers"]
        if current > seats:
            return False
        history.append(
            {
                "Passengers": booking["Passengers"],
                "dropoff_time": booking["Estimated_dropoff_time"],
            }
        )
    return True


print(is_booking_possible(6, bl1))
print(is_booking_possible(6, bl2))
