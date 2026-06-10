flights = {
    "AI101": {"source": "Delhi", "dest": "Mumbai", "seats": 5, "price": 5500},
    "AI102": {"source": "Mumbai", "dest": "Delhi", "seats": 8, "price": 5200},
    "6E201": {"source": "Bangalore", "dest": "Chennai", "seats": 3, "price": 3200},
    "6E202": {"source": "Chennai", "dest": "Bangalore", "seats": 4, "price": 3100}
}

source = input("Enter source: ")
dest = input("Enter destination: ")

found = False

for flight_no in flights:

    if flights[flight_no]["source"] == source and flights[flight_no]["dest"] == dest:

        found = True

        print("\nFlight Found")
        print("Flight No:", flight_no)
        print("Seats Available:", flights[flight_no]["seats"])
        print("Price:", flights[flight_no]["price"])

        seats_needed = int(input("\nHow many seats do you want? "))

        if seats_needed <= flights[flight_no]["seats"]:

            flights[flight_no]["seats"] = flights[flight_no]["seats"] - seats_needed

            print("Booking Confirmed")
            print("Seats Booked:", seats_needed)
            print("Remaining Seats:", flights[flight_no]["seats"])

        else:
            print("Not enough seats available")

if found == False:
    print("No flight available")

#output
Enter source: Delhi
Enter destination: Mumbai

Flight Found
Flight No: AI101
Seats Available: 3
Price: 5500

How many seats do you want? 2

Booking Confirmed
Seats Booked: 2
Remaining Seats: 3
