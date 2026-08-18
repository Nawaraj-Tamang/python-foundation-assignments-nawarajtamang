"""
Exercise: Shared Booking Counter (Scope & the global keyword)
Student: Nawaraj Tamang
Day: 3
"""

#Calculation of shared booking counter using global keyword

total_seats_booked = 0

def book_seats(n):
    global total_seats_booked
    #update the global counter
    total_seats_booked += n
    print(f"Booked {n} seat(s). Total booked so far: {total_seats_booked}")

def reset_bookings():
    global total_seats_booked
    #reset the global counter
    total_seats_booked = 0


# output
book_seats(3)
book_seats(5)
reset_bookings()
book_seats(2)