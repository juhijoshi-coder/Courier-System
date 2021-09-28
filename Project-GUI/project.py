from tkinter import *
from math import *
from tkinter import messagebox
from tkinter import ttk
import random
import datetime
import smtplib
import sqlite3
import string
from tkinter.ttk import Treeview


conn=sqlite3.connect('entry.db')
c=conn.cursor()
#c.execute("""CREATE TABLE addresses(
#    Date integer,
#    Consignment integer,
#    First_name text,
#    Address text,
#    Zipcode integer,
#    Phone_number integer,
#    Email text,
#    Price integer,
#    Note text
#    )""")

conn.commit()
conn.close()

def admin():
    global e1
    global e2

    admin_window=Toplevel(root)
    admin_window.geometry("300x200")
    admin_window.title("DYNAMO COURIERS")
    Label(admin_window,text="LOGIN").grid(row=0, column=1)
    Label(admin_window, text="Username ").grid(row=1, column=0)
    Label(admin_window, text="Password").grid(row=2,column=0)

    e1 = Entry(admin_window)
    e1.grid(row=1, column=1)

    e2 = Entry(admin_window)
    e2.grid(row=2, column=1)
    e2.config(show="*")


    Button(admin_window, text="Login", command=Ok ,height = 3, width = 13).grid(row=3, column=1)

def track():
    global c1
    track_window=Toplevel(root)
    track_window.geometry("400x200")
    track_window.title("DYNAMO COURIERS")

    Label(track_window, text="Consignment Number:: ").grid(row=1, column=0)
    c1 = Entry(track_window)
    c1.grid(row=1, column=1)
    Button(track_window, text="Track", command=shipment1 ,height = 3, width = 13).grid(row=3, column=1)
''' TO BE WORKED ON
def shipment():
    conn=sqlite3.connect('entry.db')
    c1=conn.cursor()  
    find_rname = ('SELECT * FROM rname WHERE consig= ?')
    c1.execute(find_rname,[(c.consig.get())])
    result = c1.fetchall()
    if result:
        c1.cursor.execute(shipment1)
    else:
        messagebox.showerror('Oops!','Consignment Not Found.')
'''
def shipment1():
    shipment1_window=Toplevel(root)
    shipment1_window.geometry("400x200")
    shipment1_window.title("DYNAMO COURIERS")

    Label(shipment1_window,text = ' Consignment Number:',font = ('',15),pady=5,padx=5).grid(row=2,column=0)
    Label(shipment1_window,text = 'Product Status: ',font = ('',15),pady=5,padx=5).grid(row=3,column=0)
    Label(shipment1_window,text = c1.get(), font = ('',15),pady=5,padx=5).grid(row=2,column=3)
    Label(shipment1_window,text =random.choice(("Pending","Shipped","Delivered")) ,font = ('',13),pady=5,padx=5).grid(row=3,column=3)
    Label(shipment1_window,font = ('',13), text = 'Thanks for Exploring!').grid(row = 4, column = 1)



def Ok():
    uname = e1.get()
    password = e2.get()

    if(uname == "" and password == "") :
        messagebox.showinfo("", "All fields are Required")


    elif(uname == "Juhi" and password == "admin"):
        cons()

    else :
        messagebox.showinfo("","Incorrent Username and Password")


def dt_ins():
    date.delete(0,END)
    date.insert(0, str(datetime.datetime.now()))
    consig.insert(0,str(random.randint(1,1000000)))

def receipt():
    global t 

    dist=int(a.get())
    weight=int(a1.get())

    if(dist == "" and weight == "") :
        messagebox.showinfo("", "All fields are Required")
    else :
        total=(dist*weight)+250
        t.insert(0,str(total))

    b1.insert(0,str(datetime.date.today() + datetime.timedelta(days=5)))

def entries():
    conss_window=Toplevel(root)
    conss_window.geometry('1500x450')
    conss_window.title("DYNAMO COURIERS")
    
    conn=sqlite3.connect('entry.db')
    c=conn.cursor()  
    c.execute("SELECT*, oid FROM addresses")
    records=c.fetchall()
    #print(records)
    print_records=''
    for record in records:
        print_records += str(record)+"\n"+"\n"
    Label(conss_window,text="ENTRIES").grid(row=1)
    Label(conss_window,text="---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------").grid(row=2)
    query_label=Label(conss_window,text=print_records)
    query_label.grid(row=3,column=0,columnspan=2)
    
    conn.commit()
    conn.close()

def close():
    conn=sqlite3.connect('entry.db')
    c=conn.cursor()
    c.execute("INSERT INTO addresses VALUES (:date,:consig,:rname,:add2,:add3,:num2,:mail2,:price,:note)",
            {
                'date':date.get(),
                'consig':consig.get(),
                'rname':rname.get(),
                'add2':add2.get(),
                'add3':add3.get(),
                'num2':num2.get(),
                'mail2':mail2.get(),
                'price':t.get(),
                'note':n.get()
            })
    conn.commit()
    conn.close()

    date.delete(0,END)
    consig.delete(0,END)
    rname.delete(0,END)
    add2.delete(0,END)
    add3.delete(0,END)
    num2.delete(0,END)
    mail2.delete(0,END)
    a1.delete(0,END)
    a2.delete(0,END)
    b1.delete(0,END)
    t.delete(0,END)
    n.delete(0,END)
    

def cons():

    global date
    global consig
    global rname 
    global add2
    global add3
    global num2
    global mail2
    global c2
    global n
    global a
    global a1
    global a2
    global t
    global b
    global b1
    global c1

    date=StringVar()
    consig=StringVar()
    c1=StringVar()
    rname=StringVar()
    add2=StringVar()
    num2=StringVar()
    mail2=StringVar()
    t=StringVar()
    a=StringVar()
    a1=StringVar()
    a2=StringVar()
    c2=StringVar()
    b=StringVar()
    b1=StringVar()

    cons_window=Toplevel(root)
    cons_window.geometry('850x400')
    cons_window.title("DYNAMO COURIERS")

    Label(cons_window,text="CONSIGNMENT",font=('Courier',15)).grid(row=0,sticky=N,column=2)
    Button(cons_window, text="#", command=dt_ins).grid(row=0,column=0)

    Label(cons_window, text="DATE:",).grid(row=1, column=0)
    date=Entry(cons_window,width="25")
    date.grid(row=1, column=1)

    Label(cons_window, text="CONSIGNMENT NUMBER:",).grid(row=1, column=2)
    consig=Entry(cons_window)
    consig.grid(row=1, column=3)


    Label(cons_window, text="RECEIVERS DETAILS:",).grid(row=2, column=0)

    Label(cons_window, text="NAME:",).grid(row=3, column=0)
    rname=Entry(cons_window)
    rname.grid(row=3, column=1)

    Label(cons_window, text="Choose your Destination").grid(row=4, column=0)
    c1=ttk.Combobox(cons_window,values=[			
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
    c1.grid(row=4,column=1)

    Label(cons_window, text="ADDRESS::",).grid(row=5, column=0)
    add2=Entry(cons_window)
    add2.grid(row=5, column=1)

    Label(cons_window, text="Zipcode::",).grid(row=6, column=0)
    add3=Entry(cons_window)
    add3.grid(row=6, column=1)

    Label(cons_window, text="PHONE NUMBER::",).grid(row=7, column=0)
    num2=Entry(cons_window)
    num2.grid(row=7, column=1)

    Label(cons_window, text="EMAIL:",).grid(row=8, column=0)
    mail2=Entry(cons_window)
    mail2.grid(row=8, column=1)

    Label(cons_window,text="Note(if any)::").grid(row=3,column=2)
    n=Entry(cons_window)
    n.grid(row=3,column=3)

    Label(cons_window,text="Distance(in kms)::").grid(row=4,column=2)
    a=Entry(cons_window)
    a.grid(row=4,column=3)

    Label(cons_window,text="Weight(in kgs)::").grid(row=5,column=2)
    a1=Entry(cons_window)
    a1.grid(row=5,column=3)

    Label(cons_window,text="Total::").grid(row=6,column=2)
    t=Entry(cons_window)
    t.grid(row=6,column=3)

    Label(cons_window,text="Delivery-Date::").grid(row=7,column=2)
    b1=Entry(cons_window)
    b1.grid(row=7,column=3)


    Button(cons_window,text="Calculate",command=receipt).grid(row=12,column=2)
    Button(cons_window,text="DONE",command=close).grid(row=13,column=2)
    Button(cons_window,text="Show Entries",command=entries).grid(row=14,column=2)



root = Tk()
root.title("Dynamo Couriers")
root.geometry("200x100")
Button(root,text="Admin Login",command=admin).grid(row=4,column=5)
Button(root,text="Track Consignment",command=track).grid(row=5,column=5)

root.mainloop()
