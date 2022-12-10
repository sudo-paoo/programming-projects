import customtkinter
import time
from datetime import datetime
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("600x550")
root.title("Payment System")
def regular_fare(destination):
    destination_dictionary = {
        "SM Tarlac to Gerona" : 30,
        "SM Tarlac to Paniqui" : 40,
        "SM Tarlac to Moncada" : 50
    }
    if destination in destination_dictionary:
        return destination_dictionary.get(destination)


def student_fare(destination):
    destination_dictionary = {
        "SM Tarlac to Gerona" : 26,
        "SM Tarlac to Paniqui" : 36,
        "SM Tarlac to Moncada" : 46
    }
    if destination in destination_dictionary:
        return destination_dictionary.get(destination)


def senior_fare(destination):
    destination_dictionary = {
        "SM Tarlac to Gerona" : 25,
        "SM Tarlac to Paniqui" : 35,
        "SM Tarlac to Moncada" : 45
    }
    if destination in destination_dictionary:
        return destination_dictionary.get(destination)


def recreate_frame():
    global frame
    frame.destroy()
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label_type = customtkinter.CTkLabel(master=frame, text="Passenger Type")
    label_type.pack(pady=12, padx=10)

    option_type = customtkinter.CTkOptionMenu(master=frame, values=["Regular", "Student", "Senior Citizen"], command=callback_type)
    option_type.pack(pady=12,padx=10)
    option_type.set("None")

    label_destination = customtkinter.CTkLabel(master=frame, text="Destination")
    label_destination.pack(pady=12, padx=10)

    option_destination = customtkinter.CTkOptionMenu(master=frame, values=["SM Tarlac to Gerona", "SM Tarlac to Paniqui"], command=callback_dest)
    option_destination.pack(pady=12,padx=10)
    option_destination.set("None")

    submit_button = customtkinter.CTkButton(master=frame, text="Submit", command=lambda: [label_type.pack_forget(), option_type.pack_forget(), label_destination.pack_forget(), option_destination.pack_forget(), submit_button.pack_forget(), payment()])
    submit_button.pack(pady=10, padx=10)
def payment():
    global passenger_destination
    global passenger_type
    global pack
    global frame
    if passenger_type == "Regular":
        fare = regular_fare(passenger_destination)
    elif passenger_type == "Student":
        fare = student_fare(passenger_destination)
    elif passenger_type == "Senior Citizen":
        fare = senior_fare(passenger_destination)
    label_fare = customtkinter.CTkLabel(master=frame, text=f"Total Fare: {fare}")
    label_fare.pack(pady=12, padx=10)

    entry_fare = customtkinter.CTkEntry(master=frame)
    entry_fare.pack(pady=12, padx=10)
    button_fare = customtkinter.CTkButton(master=frame, text="Pay", command=lambda: [passenger_info(fare, int(entry_fare.get())), button_fare.pack_forget(), entry_fare.pack_forget(), label_fare.pack_forget()])
    button_fare.pack(pady=12, padx=10)

def passenger_info(fare, paid):
    global frame
    global passenger_type
    global passenger_destination
    global num
    global passenger_dict 
    while True:
        num += 1
        change = paid - fare
        label_passenger_number = customtkinter.CTkLabel(master=frame, text=f"Passenger #{num}")
        label_passenger_number.pack(pady=12, padx=10)
        label_passenger_type = customtkinter.CTkLabel(master=frame, text=f"Passenger Type: {passenger_type}")
        label_passenger_type.pack(pady=12, padx=10)
        label_passenger_detination = customtkinter.CTkLabel(master=frame, text=f"Detination: {passenger_destination}")
        label_passenger_detination.pack(pady=12, padx=10)
        label_passenger_fare = customtkinter.CTkLabel(master=frame, text=f"Total Fare: {fare}")
        label_passenger_fare.pack(pady=12, padx=10)
        label_passenger_paid = customtkinter.CTkLabel(master=frame, text=f"Total Amount: {paid}")
        label_passenger_paid.pack(pady=12, padx=10)
        label_passenger_change = customtkinter.CTkLabel(master=frame, text=f"Passenger Change: {change}")
        label_passenger_change.pack(pady=12, padx=10)
        button_add = customtkinter.CTkButton(master=frame, text=f"Add Passenger", command=lambda:[recreate_frame()])
        button_add.pack(pady=12, padx=10)
        button_print = customtkinter.CTkButton(master=frame, text=f"Print Receipt", command=lambda: [print_receipt()])
        button_print.pack(pady=12, padx=10)
        now = datetime.now()
        dt = now.strftime("%d/%m/%Y %H:%M:%S")
        passenger_dict[f'Passenger #{num}'] = {'Passenger Type': passenger_type, 'Destination': passenger_destination, 'Total Fare' : fare, 'Payment Amount': paid, 'Change Amount': change, 'Payment Date': dt}


        break
def callback_type(Ptype):
    global passenger_type
    passenger_type = Ptype

def callback_dest(dest):
    global passenger_destination
    passenger_destination = dest

def print_receipt():
    global passenger_dict
    global frame
    frame.destroy()
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    print_textbox = customtkinter.CTkTextbox(master=frame, width=300)
    print_textbox.pack(padx=20, pady=20)
    
    for key, value in passenger_dict.items():
        print_textbox.insert("end -1 chars", f"""
        PGT BUS TRANSPORTATION

        {key}
        
        Passenger Type: {value['Passenger Type']}
        Destination: {value['Destination']}
        Total Fare: {value['Total Fare']}
        Payment Amount: {value['Payment Amount']}
        Change Amount: {value['Change Amount']}
        Payment Date: {value['Payment Date']}
        """)
    print_textbox.configure(state='disabled')
    button_add_passenger = customtkinter.CTkButton(master=frame, text=f"Add Passenger", command=lambda: recreate_frame())
    button_add_passenger.pack(pady=12, padx=10)

passenger_type = ""
passenger_destination = ""
passenger_dict = {}
num =0
pack = True


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label_type = customtkinter.CTkLabel(master=frame, text="Passenger Type")
label_type.pack(pady=12, padx=10)

option_type = customtkinter.CTkOptionMenu(master=frame, values=["Regular", "Student", "Senior Citizen"], command=callback_type)
option_type.pack(pady=12,padx=10)
option_type.set("=============")

label_destination = customtkinter.CTkLabel(master=frame, text="Destination")
label_destination.pack(pady=12, padx=10)

option_destination = customtkinter.CTkOptionMenu(master=frame, values=["SM Tarlac to Gerona", "SM Tarlac to Paniqui", "SM Tarlac to Moncada"], command=callback_dest)
option_destination.pack(pady=12,padx=10)
option_destination.set("=============")

submit_button = customtkinter.CTkButton(master=frame, text="Submit", command=lambda: [label_type.pack_forget(), option_type.pack_forget(), label_destination.pack_forget(), option_destination.pack_forget(), submit_button.pack_forget(), payment()])
submit_button.pack(pady=10, padx=10)

root.mainloop()
