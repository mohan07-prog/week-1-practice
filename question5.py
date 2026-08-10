seats = [
    "Available",
    "Booked",
    "Available",
    "Available",
    "Booked",
    "Available",
    "Booked",
    "Available"]
for i in range(len(seats)):
    print(f"seat {i+1}: {seats[i]}")
seat_number=int(input("enter seat number: "))
index=seat_number -1
if seats[index]=="available":
    print("seat booked successfully")
    seats[index]="booked"
else:
    print("seat already booked")
booked_seats=seats.count("booked")
available_seats=seats.count("available")
print("total seats:", len(seats))  
print("booked seats:", booked_seats)
print("available seats:", available_seats)
    
    
