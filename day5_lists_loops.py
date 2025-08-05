# Day 5 - Loops and Lists: Guest List Tracker

guest_list = []

num_guests = int(input("How many guests are attending? "))

for i in range(num_guests):
    name = input(f"Enter the name of guest #{i+1}: ")
    guest_list.append(name)

print("\nGuest List:")
for guest in guest_list:
    print(f"- {guest}")
