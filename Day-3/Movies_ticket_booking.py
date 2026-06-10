movies = {
    "M101": {"name": "Leo", "theatre": "PVR Chennai", "seats": 10, "price": 200},
    "M102": {"name": "Jailer", "theatre": "AGS Cinemas", "seats": 8, "price": 180},
    "M103": {"name": "Vikram", "theatre": "Cinepolis", "seats": 5, "price": 220},
    "M104": {"name": "Master", "theatre": "PVR Bangalore", "seats": 6, "price": 150}
}

movie_name = input("Enter movie name: ")
theatre_name = input("Enter theatre: ")

found = False

for movie_id in movies:

    if movies[movie_id]["name"].lower() == movie_name.lower() and \
       movies[movie_id]["theatre"].lower() == theatre_name.lower():

        found = True

        print("\nMovie Found")
        print("Movie ID:", movie_id)
        print("Available Seats:", movies[movie_id]["seats"])
        print("Ticket Price:", movies[movie_id]["price"])

        seats_needed = int(input("\nHow many tickets do you want? "))

        if seats_needed <= movies[movie_id]["seats"]:

            movies[movie_id]["seats"] -= seats_needed

            print("\nBooking Confirmed")
            print("Tickets Booked:", seats_needed)
            print("Remaining Seats:", movies[movie_id]["seats"])

        else:
            print("Not enough seats available")

if not found:
    print("\nNo movie available for your search")
