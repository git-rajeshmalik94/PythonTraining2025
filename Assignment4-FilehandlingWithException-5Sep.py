# Assignment :
 
# Problem Statement

# You are asked to design a Flight Management System in Python using exception handling.
 
# The system should:

# - Read flight information from a file called flights.txt.

# - Each line has: flight_number available_seats price_per_ticket

#   Example: AI101 50 6000
 
# Ask the user for:

# - Flight number

# - Number of tickets to book
 
# Implement the following exception rules: (Questions below)
 
# (a) Raise FlightNotFoundError (custom) if the entered flight number does not exist.
 
# (b) Raise SeatsUnavailableError (custom) if requested tickets exceed available seats.
 
# (c) Handle ValueError if user enters invalid input (like string instead of integer).
 
# (d) Handle ZeroDivisionError if user enters 0 tickets (while calculating discount per ticket).
 
# (e) Always close the file using finally.
 
# The program should print:

# - Flight details

# - Total booking cost

# - Discount per ticket (total / tickets)
 
# Note**:

# Use nested try-except:
 
# Inner block for booking operations.
 
# Outer block for file handling & re-raised exceptions

class FlightNotFoundError(Exception):
    pass

class SeatsUnavailableError(Exception):
    pass

with open("ExceptionHandling\\flight.txt", 'r') as f:
    try:
        recordlist = []
        lines = f.readlines()
        for line in lines:
            templist = line.split()
            recordlist.append(templist)
        print(recordlist)
        
        try:
            flightnumber = input("Flight Number:")
            entryfoundIdx = -1
            for record in recordlist:
                if flightnumber == record[0]:
                    entryfoundIdx = recordlist.index(record)
                    break
            if entryfoundIdx == -1:
                raise FlightNotFoundError("Entered flight number does not exist")

            nooftickets = int(input("Numbers of tickets to book:"))
            if(nooftickets > int(recordlist[entryfoundIdx][1])):
                raise SeatsUnavailableError('Requested tickets exceed available seats')

            totalbookingcost = nooftickets * int(recordlist[entryfoundIdx][2])
            discountperticket = totalbookingcost / nooftickets

            print(f"Flight Number: {flightnumber}\nNo. of Tickets: {nooftickets}\nTotal booking cost: {totalbookingcost}\nDiscount per ticket: {discountperticket}")


        except FlightNotFoundError as e:
            print("Exception Occurred:", e)
        except SeatsUnavailableError as e:
            print("Exception Occurred: ", e)

    except ValueError as e:
        print("Invalid input (like string instead of integer): ", e)
    except ZeroDivisionError as e:
        print("User entered 0 tickets: ", e)
    except Exception as e:
        print("Generic Exception", e)
    finally:
        f.close()
