# ------------------------------------------------------
# Name: David Prochaska
# Course: DSE 502
# Project 1 - Airplane Seat Reseravation Program
# AI assistance: ChatGPT used as a resource to help understand concepts
# such as file reading, lists, and function structure.

# Description:
# This program allows a user to view airplane seating,
# reserve a seat, and compute seating statistics.
# Seat data is loaded from a file and updated when
# reservations are made.
# ------------------------------------------------------


ROWS = 10	# total number of seat rows
COLS = 4	# total number of seat columns

# ------------------------------------------------------
# Load seats from file
# Reads the seat layout from seats.txt and stores it
# in a 2D list.
# ------------------------------------------------------

def load_seats():

	seats = []	# list that will store seating chart

	file = open("seats.txt", "r")

	# PROCESSING: read each line of the file

	for line in file:
		line = line.strip()		# remove newline character
		seats.append(list(line))	# converyt row into list of seats

	file.close()

	return seats

# -----------------------------------------------------
# Save seats back to file
# Writes the updated seat chart to seats.txt
# -----------------------------------------------------

def save_seats(seats):

	file = open("seats.txt", "w")

	# PROCESSING: write each row of seats to the file
	for row in seats:
		file.write("".join(row) + "\n")

	file.close()

# ------------------------------------------------------
# Display seating chart
# Shows the airplane seating layout to the user
# ------------------------------------------------------

def display(seats):

	#OUTPUT: display seating chart header
	print("\nSeating chart:\n")
	print("  AB CD")

	# Processing: loop through each row and display seats
	for i in range(len(seats)):

		row = "".join(seats[i])	# convert list row to string

		left = row[:2]		# first two seats
		right = row[2:]		# last two seats

		# OUTPUT: print row number and seat layout
		print(f"{i+1:2} {left} {right}")

# -------------------------------------------------------
# Assign seat
# Checks if a seat is available and reserves it
# -------------------------------------------------------

def assign_seats(seats, row, column):

	row_index = row -1			# convert user row to list index
	col_index = ord(column) - ord('A')	# convert column letter to index

	# PROCESSING: check if seat is available
	if seats[row_index][col_index] == '.':
		seats[row_index][col_index] = 'X'	# mark seat as taken
		save_seats(seats)			# update file
		return True
	else:
		return False

# -------------------------------------------------------
# Purchase seat
# Gets seat selection from the user and attempts to
# reserve it.
# -------------------------------------------------------

def purchase(seats):

	# INPUT: get seat selection from user
	seat = input("Enter your row number and column letter (ex. 1A):")

	try:

		#PROCESSING: extract row and column
		row = int(seat[:-1])
		column = seat[-1].upper()

		# ERROR CHECK: validate row number
		if row < 1 or row > ROWS:
			print("Invalid row - please try again")
			return

		# ERROR CHECK: validate column letter
		if column not in ['A', 'B', 'C', 'D']:
			print("Invalid column - please try again")
			return

		# PROCESSING: attmept seat reservation
		success = assign_seats(seats, row, column)

		# OUTPUT: display result
		if success:
			print("Seat", seat.upper(), "reserved!")
		else:
			print("Seat", seat.upper(), "is not available.")

	except:
		print("Invalid input format.")

# ------------------------------------------------------------
# Statistics
# Computes and displays airlplane occupancy percentage
# ------------------------------------------------------------

def statistics(seats):

	total = ROWS * COLS	# total number of seats
	taken = 0 		# number of occupied seats

	# PROCESSING: count seats that are taken
	for row in seats:
		for seat in row:
			if seat == 'X':
				taken += 1

	percent = (taken / total) * 100

	# OUTPUT: display occupancy percentage
	print("\nPlane occupancy:", round(percent,1), "%")

# -------------------------------------------------------------
# Menu
# Display program options
# -------------------------------------------------------------

def menu():

	# OUPUT: show meny choices
	print("\nSelect choice from menu:")
	print("D to display seat chart")
	print("P to purchase a seat")
	print("S to compute statistics")
	print("Q to quit")

# --------------------------------------------------------------
# Main program
# Controls the program loop and user choices
# --------------------------------------------------------------

if __name__ == "__main__":

	seats = load_seats()	# load seat data from file

	while True:

		menu()

		# INPUT: get user menu choice
		choice = input("choice: ").upper()

		# PROCESSING: perform selected action
		if choice == 'D':
			display(seats)

		elif choice == 'P':
			purchase(seats)

		elif choice == 'S':
			statistics(seats)

		elif choice == 'Q':
			print("Program ended.")
			break

		else:
			print("Invalid choice.")
