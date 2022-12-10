from pick import pick 
from datetime import datetime
import os
import time
from alive_progress import alive_bar

def regular_fare(destination):
    destination_dictionary = {
        "SM Tarlac to Gerona" : 30,
        "SM Tarlac to Paniqui" : 40
    }
    if destination in destination_dictionary:
        return destination_dictionary.get(destination)


def student_fare(destination):
    destination_dictionary = {
        "SM Tarlac to Gerona" : 26,
        "SM Tarlac to Paniqui" : 36
    }
    if destination in destination_dictionary:
        return destination_dictionary.get(destination)


def senior_fare(destination):
    destination_dictionary = {
        "SM Tarlac to Gerona" : 25,
        "SM Tarlac to Paniqui" : 35
    }
    if destination in destination_dictionary:
        return destination_dictionary.get(destination)


num = 0
passenger_dictionary = {}
while True:
    passenger_title = "Passenger Type"
    choice_of_passenger = ["Regular", "Student", "Senior Citizen"]
    destination_title = "Destination"
    destination_choices = ["SM Tarlac to Gerona", "SM Tarlac to Paniqui"] 


    passenger_type, passenger_index = pick(choice_of_passenger, passenger_title, indicator=">>")
    print("================================================================")
    print(f"Passenger Type: {passenger_type}")

    destination_choice, destination_index = pick(destination_choices, destination_title, indicator=">>")


    print(f"Destination: {destination_choice}")


    if passenger_type == "Regular":
        fare = regular_fare(destination_choice)
    elif passenger_type == "Student":
        fare = student_fare(destination_choice)
    elif passenger_type == "Senior Citizen":
        fare = senior_fare(destination_choice)

    now = datetime.now()
    dt = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"Total Fare: {fare}")
    payment_amount = float(input("Payment of the Passenger: "))
    print(f"Payment Amount: {payment_amount}")
    change_amount = payment_amount - fare
    print(f"Change Amount: {change_amount}")
    print("================================================================")
    num += 1
    passenger_dictionary[f'Passenger # {num}'] = {'Passenger Type': passenger_type, 'Destination': destination_choice, 'Total Fare' : fare, 'Payment Amount': payment_amount, 'Change Amount': change_amount, 'Payment Date': dt}

    time.sleep(1)
    add_passenger_title = "Choose Next Option"
    add_passenger_choices = ['Add Passenger', 'Print Receipt', 'Exit']

    option, index = pick(add_passenger_choices, add_passenger_title, indicator='>>')

    if option == "Add Passenger":
        continue
    elif option == 'Print Receipt':
        os.system("cls")
        with alive_bar(num) as bar:
            for i in range(num):
                time.sleep(0.1)
                bar()

        for key, value in passenger_dictionary.items():
            passengerNumber = key
            print("================================================================")
            print()
            print("Bus Transportation")
            print()
            print(passengerNumber)
            print(f"Passenger Type: {value['Passenger Type']}")
            print(f"Destination: {value['Destination']}")
            print(f"Total Fare: {value['Total Fare']}")
            print(f"Payment Amount: {value['Payment Amount']}")
            print(f"Change Amount: {value['Change Amount']}")
            print(f"Payment Date: {value['Payment Date']}")
            print()
        break
    elif option == "Exit":
        break
