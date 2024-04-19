"""
Module description: This script implements a GUI application for a courier service.
"""

import tkinter as tk
from tkinter import messagebox, ttk
import random
import datetime
import sqlite3

# Initialize global variables starting with "ENTRY_"
ENTRY_DATE = None
ENTRY_CONSIGNMENT = None
ENTRY_RECEIVER_NAME = None
ENTRY_ADDRESS = None
ENTRY_ZIPCODE = None
ENTRY_PHONE = None
ENTRY_EMAIL = None
ENTRY_DISTANCE = None
ENTRY_WEIGHT = None
ENTRY_TOTAL = None
ENTRY_DELIVERY_DATE = None
ENTRY_NOTE = None
ENTRY_USERNAME = None
ENTRY_PASSWORD = None

# Establish database connection
conn = sqlite3.connect('entry.db')
cursor = conn.cursor()

# Create the addresses table if it doesn't exist
cursor.execute("""CREATE TABLE IF NOT EXISTS addresses(
    Date TEXT,
    Consignment INTEGER,
    First_name TEXT,
    Address TEXT,
    Zipcode INTEGER,
    Phone_number INTEGER,
    Email TEXT,
    Price INTEGER,
    Note TEXT
)""")
conn.commit()
conn.close()


def admin_login():
    """
    Admin Login.
    """
    global ENTRY_USERNAME
    global ENTRY_PASSWORD

    admin_window = tk.Toplevel(root)
    admin_window.geometry("300x200")
    admin_window.title("DYNAMO COURIERS")
    tk.Label(admin_window, text="LOGIN").grid(row=0, column=1)
    tk.Label(admin_window, text="Username ").grid(row=1, column=0)
    tk.Label(admin_window, text="Password").grid(row=2, column=0)

    ENTRY_USERNAME = tk.Entry(admin_window)
    ENTRY_USERNAME.grid(row=1, column=1)

    ENTRY_PASSWORD = tk.Entry(admin_window)
    ENTRY_PASSWORD.grid(row=2, column=1)
    ENTRY_PASSWORD.config(show="*")

    tk.Button(admin_window, text="Login", command=login_check,
              height=3, width=13).grid(row=3, column=1)


def track_consignment():
    """
    Tracks Shipment.
    """
    global ENTRY_CONSIGNMENT_NUMBER
    track_window = tk.Toplevel(root)
    track_window.geometry("400x200")
    track_window.title("DYNAMO COURIERS")

    tk.Label(track_window, text="Consignment Number:: ").grid(row=1, column=0)
    ENTRY_CONSIGNMENT_NUMBER = tk.Entry(track_window)
    ENTRY_CONSIGNMENT_NUMBER.grid(row=1, column=1)
    tk.Button(track_window, text="Track", command=shipment_status,
              height=3, width=13).grid(row=3, column=1)


def shipment_status():
    """
    Checks for Shipment Status.
    """
    shipment_window = tk.Toplevel(root)
    shipment_window.geometry("400x200")
    shipment_window.title("DYNAMO COURIERS")

    global ENTRY_CONSIGNMENT_NUMBER
    tk.Label(shipment_window, text=' Consignment Number:',
             font=('', 15), pady=5, padx=5).grid(row=2, column=0)
    tk.Label(shipment_window, text='Product Status: ', font=(
        '', 15), pady=5, padx=5).grid(row=3, column=0)
    tk.Label(shipment_window, text=ENTRY_CONSIGNMENT_NUMBER.get(),
             font=('', 15), pady=5, padx=5).grid(row=2, column=3)
    tk.Label(shipment_window, text=random.choice(("Pending", "Shipped",
             "Delivered")), font=('', 13), pady=5, padx=5).grid(row=3, column=3)
    tk.Label(shipment_window, font=('', 13),
             text='Thanks for Exploring!').grid(row=4, column=1)


def login_check():
    """
    Function to check for login.
    """
    global ENTRY_USERNAME
    global ENTRY_PASSWORD
    username = ENTRY_USERNAME.get()
    password = ENTRY_PASSWORD.get()

    if username == "" and password == "":
        messagebox.showinfo("", "All fields are Required")
    elif username == "Juhi" and password == "admin":
        consignment_entry()
    else:
        messagebox.showinfo("", "Incorrect Username and Password")


def insert_date_consignment():
    """
    Inserts Date and Time for the consignment.
    """
    ENTRY_DATE.delete(0, tk.END)
    ENTRY_DATE.insert(0, str(datetime.datetime.now()))
    ENTRY_CONSIGNMENT.delete(0, tk.END)
    ENTRY_CONSIGNMENT.insert(0, str(random.randint(1, 1000000)))


def calculate_receipt():
    """
   Calculates the prices.
    """
    total_distance = int(ENTRY_DISTANCE.get())
    total_weight = int(ENTRY_WEIGHT.get())

    if total_distance == "" and total_weight == "":
        messagebox.showinfo("", "All fields are Required")
    else:
        total_cost = (total_distance * total_weight) + 250
        ENTRY_TOTAL.delete(0, tk.END)
        ENTRY_TOTAL.insert(0, str(total_cost))

    ENTRY_DELIVERY_DATE.delete(0, tk.END)
    ENTRY_DELIVERY_DATE.insert(
        0, str(datetime.date.today() + datetime.timedelta(days=5)))


def show_entries():
    """
   Shows Entries.
    """
    entries_window = tk.Toplevel(root)
    entries_window.geometry('1500x450')
    entries_window.title("DYNAMO COURIERS")

    conn = sqlite3.connect('entry.db')  # Renamed variable to "conn"
    cursor = conn.cursor()  # Renamed variable to "cursor"
    cursor.execute("SELECT *, oid FROM addresses")
    records = cursor.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record) + "\n" + "\n"
    tk.Label(entries_window, text="ENTRIES").grid(row=1)
    tk.Label(entries_window, text="---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------").grid(row=2)
    query_label = tk.Label(entries_window, text=print_records)
    query_label.grid(row=3, column=0, columnspan=2)

    conn.commit()
    conn.close()


def close_window():
    """
    Closes a window.
    """
    conn = sqlite3.connect('entry.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO addresses VALUES (:date,:consig,:rname,:add2,:add3,:num2,:mail2,:price,:note)", {
        'date': ENTRY_DATE.get(),
        'consig': ENTRY_CONSIGNMENT.get(),
        'rname': ENTRY_RECEIVER_NAME.get(),
        'add2': ENTRY_ADDRESS.get(),
        'add3': ENTRY_ZIPCODE.get(),
        'num2': ENTRY_PHONE.get(),
        'mail2': ENTRY_EMAIL.get(),
        'price': ENTRY_TOTAL.get(),
        'note': ENTRY_NOTE.get()
    })
    conn.commit()
    conn.close()

    ENTRY_DATE.delete(0, tk.END)
    ENTRY_CONSIGNMENT.delete(0, tk.END)
    ENTRY_RECEIVER_NAME.delete(0, tk.END)
    ENTRY_ADDRESS.delete(0, tk.END)
    ENTRY_ZIPCODE.delete(0, tk.END)
    ENTRY_PHONE.delete(0, tk.END)
    ENTRY_EMAIL.delete(0, tk.END)
    ENTRY_DISTANCE.delete(0, tk.END)
    ENTRY_WEIGHT.delete(0, tk.END)
    ENTRY_TOTAL.delete(0, tk.END)
    ENTRY_NOTE.delete(0, tk.END)


def consignment_entry():
    """
    Opens a window for consignment entry.
    """
    cons_window = tk.Toplevel(root)
    cons_window.geometry('850x400')
    cons_window.title("DYNAMO COURIERS")

    tk.Label(cons_window, text="CONSIGNMENT", font=(
        'Courier', 15)).grid(row=0, sticky="n", column=2)
    tk.Button(cons_window, text="#", command=insert_date_consignment).grid(
        row=0, column=0)

    global ENTRY_DATE, ENTRY_CONSIGNMENT, ENTRY_RECEIVER_NAME, ENTRY_ADDRESS, ENTRY_ZIPCODE, ENTRY_PHONE, ENTRY_EMAIL, ENTRY_DISTANCE, ENTRY_WEIGHT, ENTRY_TOTAL, ENTRY_DELIVERY_DATE, ENTRY_NOTE

    tk.Label(cons_window, text="DATE:").grid(row=1, column=0)
    ENTRY_DATE = tk.Entry(cons_window, width="25")
    ENTRY_DATE.grid(row=1, column=1)

    tk.Label(cons_window, text="CONSIGNMENT NUMBER:").grid(row=1, column=2)
    ENTRY_CONSIGNMENT = tk.Entry(cons_window)
    ENTRY_CONSIGNMENT.grid(row=1, column=3)

    tk.Label(cons_window, text="RECEIVERS DETAILS:").grid(row=2, column=0)

    tk.Label(cons_window, text="NAME:").grid(row=3, column=0)
    ENTRY_RECEIVER_NAME = tk.Entry(cons_window)
    ENTRY_RECEIVER_NAME.grid(row=3, column=1)

    tk.Label(cons_window, text="Choose your Destination").grid(row=4, column=0)
    entry_destination = ttk.Combobox(cons_window, values=[
        "Andhra Pradesh 1387",
        "Andaman and Nicobar Islands 2389",
        "Arunachal Pradesh 2752",
        "Assam 2501",
        "Bihar 1483",
        "Chandigarh 736",
        "Chattisgarh 1063",
        "Dadra and Nagar Haveli and Daman & Diu 252",
        "Delhi 1006",
        "Goa 966",
        "Gujrat 132",
        "Haryana 1241",
        "Himachal 1338",
        "Jammu & Kashmir 1760",
        "Jharkhand 1549",
        "Karnataka 1377",
        "Kerela 2066",
        "Ladakh 1957",
        "Madhya Pradesh 537",
        "Maharastra 418",
        "Manipur 2977",
        "Meghalaya 2590",
        "Mizoram	2961",
        "Nagaland 2843",
        "Odisha 1641",
        "Puducherry 1740",
        "Punjab 1241",
        "Rajasthan 736",
        "Sikkim 2137",
        "Tamil Nadu 1730",
        "Telangana 1105",
        "Tripura 3036",
        "Uttrakhand 1250",
        "Uttar Pradesh 1138",
        "West Bengal 1915",])

    entry_destination.grid(row=4, column=1)

    tk.Label(cons_window, text="ADDRESS::").grid(row=5, column=0)
    ENTRY_ADDRESS = tk.Entry(cons_window)
    ENTRY_ADDRESS.grid(row=5, column=1)

    tk.Label(cons_window, text="Zipcode::").grid(row=6, column=0)
    ENTRY_ZIPCODE = tk.Entry(cons_window)
    ENTRY_ZIPCODE.grid(row=6, column=1)

    tk.Label(cons_window, text="PHONE NUMBER::").grid(row=7, column=0)
    ENTRY_PHONE = tk.Entry(cons_window)
    ENTRY_PHONE.grid(row=7, column=1)

    tk.Label(cons_window, text="EMAIL:").grid(row=8, column=0)
    ENTRY_EMAIL = tk.Entry(cons_window)
    ENTRY_EMAIL.grid(row=8, column=1)

    tk.Label(cons_window, text="Note(if any)::").grid(row=3, column=2)
    ENTRY_NOTE = tk.Entry(cons_window)
    ENTRY_NOTE.grid(row=3, column=3)

    tk.Label(cons_window, text="Distance(in kms)::").grid(row=4, column=2)
    ENTRY_DISTANCE = tk.Entry(cons_window)
    ENTRY_DISTANCE.grid(row=4, column=3)

    tk.Label(cons_window, text="Weight(in kgs)::").grid(row=5, column=2)
    ENTRY_WEIGHT = tk.Entry(cons_window)
    ENTRY_WEIGHT.grid(row=5, column=3)

    tk.Label(cons_window, text="Total::").grid(row=6, column=2)
    ENTRY_TOTAL = tk.Entry(cons_window)
    ENTRY_TOTAL.grid(row=6, column=3)

    tk.Label(cons_window, text="Delivery-Date::").grid(row=7, column=2)
    ENTRY_DELIVERY_DATE = tk.Entry(cons_window)
    ENTRY_DELIVERY_DATE.grid(row=7, column=3)

    tk.Button(cons_window, text="Calculate",
              command=calculate_receipt).grid(row=12, column=2)
    tk.Button(cons_window, text="DONE",
              command=close_window).grid(row=13, column=2)
    tk.Button(cons_window, text="Show Entries",
              command=show_entries).grid(row=14, column=2)


root = tk.Tk()
root.title("Dynamo Couriers")
root.geometry("200x100")
root.configure(bg="white")  # Set the background color to white
tk.Button(root, text="Admin Login", command=admin_login).grid(row=4, column=5)
tk.Button(root, text="Track Consignment",
          command=track_consignment).grid(row=5, column=5)

root.mainloop()  # Add this line to start the Tkinter event loop
