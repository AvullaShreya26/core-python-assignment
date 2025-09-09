# ticket_booking.py

def book_seat(booked_seats, seat_number, total_seats):
    if seat_number < 1 or seat_number > total_seats:
        print(f"Seat {seat_number} is invalid.")
    elif seat_number in booked_seats:
        print(f"Seat {seat_number} is already booked.")
    else:
        booked_seats.append(seat_number)
        print(f"Seat {seat_number} booked successfully.")

def cancel_seat(booked_seats, seat_number):
    if seat_number in booked_seats:
        booked_seats.remove(seat_number)
        print(f"Seat {seat_number} cancelled successfully.")
    else:
        print(f"Seat {seat_number} is not booked.")

def get_available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]

if __name__ == "__main__":
    total_seats = 10
    booked_seats = [2, 5, 7]

    book_seat_number = 3
    cancel_seat_number = 5

    book_seat(booked_seats, book_seat_number, total_seats)
    cancel_seat(booked_seats, cancel_seat_number)

    available = get_available_seats(total_seats, booked_seats)
    print("Available seats:", available)
