"""
User can:

View All records
Search an entry
Add entry
Update entry
Delete
Close
Open RDP
Get IP and device info
Mark row as done
"""

from tkinter import *
import backend
import os
import winrm
from datetime import date
window = Tk()

window.wm_title("Bios Update Manager")
window.geometry("+100+300")

#p1 = PhotoImage(file='Assets/motherboard.png')
#window.iconphoto(False, p1)

backend.connect()


def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
        e5.delete(0, END)
        e5.insert(END, selected_tuple[5])
        e6.delete(0, END)
        e6.insert(END, selected_tuple[6])
        e7.delete(0, END)
        e7.insert(END, selected_tuple[7])
        e8.delete(0, END)
        e8.insert(END, selected_tuple[8])
        e9.delete(0, END)
        e9.insert(END, selected_tuple[9])
        e10.delete(0, END)
        e10.insert(END, selected_tuple[10])
    except IndexError:
        pass


#    print(selected_tople)


def view_command():
    list1.delete(0, END)
    for row in backend.view():
        # row = str(row).replace(" ","NA")
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    # print(Number_text.get())
    for row in backend.search(Name_text.get(), Number_text.get(),CurrentIP_text.get(), Type_text.get(),
                              Manufacturer_text.get(), Model_text.get(), BiosVersion_text.get(), LastUser_text.get(),
                              UpdatedDate_text.get(), Done_text.get()):
        list1.insert(END, row)


def add_command():
    backend.insert(Name_text.get(), Number_text.get(),CurrentIP_text.get(), Type_text.get(),
                   Manufacturer_text.get(), Model_text.get(), BiosVersion_text.get(), LastUser_text.get(),
                   UpdatedDate_text.get(), Done_text.get())
    list1.delete(0, END)
    list1.insert(END, (Name_text.get(), Number_text.get(),CurrentIP_text.get(), Type_text.get(),
                       Manufacturer_text.get(), Model_text.get(), BiosVersion_text.get(), LastUser_text.get(),
                       UpdatedDate_text.get(), Done_text.get()))


def delete_command():
    backend.delete(selected_tuple[0])
    view_command()


def update_command():
    backend.update(selected_tuple[0], Name_text.get(), Number_text.get(),CurrentIP_text.get(), Type_text.get(),
                   Manufacturer_text.get(), Model_text.get(), BiosVersion_text.get(), LastUser_text.get(),
                   UpdatedDate_text.get(), Done_text.get())
    view_command()


def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)
    view_command()


def RDPcommand():
    username = UserName_text.get()
    password = Password_text.get()
    target = Name_text.get()
    if target == False:
        print("No target for operation try again")
    else:

        comend = 'cmdkey /generic:"' + target + '" /user:"' + username + '" /pass:"' + password + '"'
        # print (comend)
        os.system(comend)
        thetarget = ' /v:' + target + ' /f'
        comend = "mstsc" + thetarget
        os.system(comend)
        # print("RDP for " + target + " done")


def IPcommand():
    getmodel = Session.run_cmd('wmic nicconfig where "IPEnabled  = True" get ipaddress')
    model = list(getmodel.std_out.decode().strip("\r\r\n ").split("\r\r\n"))
    ip = model[1].split('"')
    ip = str(ip[1])
    # print(ip)
    e3.insert(0, ip)


def getmanudacturer():
    getmanudacturer = Session.run_cmd('wmic computersystem get manufacturer')
    manufacturer = list(getmanudacturer.std_out.decode().strip("\r\r\n ").split("\r\r\n"))
    e5.insert(0, manufacturer[1])


def getmodel():
    getmodel = Session.run_cmd('wmic computersystem get model')
    model = list(getmodel.std_out.decode().strip("\r\r\n ").split("\r\r\n"))
    e6.insert(0, model[1])


def getbiosversion():
    getmodel = Session.run_cmd('wmic bios get smbiosbiosversion')
    model = list(getmodel.std_out.decode().strip("\r\r\n ").split("\r\r\n"))
    e7.insert(0, model[1])


def Today_command():
    today = date.today()
    e9.insert(0,today)


def Done_command():
    e10.insert(0,"V")

def All_command():
    IPcommand()
    getmanudacturer()
    getmodel()
    getbiosversion()

l1 = Label(window, text="Name")
l1.grid(row=0, column=6)

l2 = Label(window, text="Current IP")
l2.grid(row=2, column=6)

l3 = Label(window, text="Number")
l3.grid(row=1, column=6)

l4 = Label(window, text="Type")
l4.grid(row=3, column=6)

l5 = Label(window, text="Manufacturer")
l5.grid(row=4, column=6)

l6 = Label(window, text="Model")
l6.grid(row=5, column=6)

l7 = Label(window, text="Bios Version")
l7.grid(row=6, column=6)

l8 = Label(window, text="User")
l8.grid(row=7, column=6)

l9 = Label(window, text="Updated Date")
l9.grid(row=8, column=6)

l10 = Label(window, text="Done")
l10.grid(row=9, column=6)

l11 = Label(window, text="User Name")
l11.grid(row=11, column=1)

l12 = Label(window, text="Password")
l12.grid(row=11, column=3)

Name_text = StringVar()
e1 = Entry(window, textvariable=Name_text)
e1.grid(row=0, column=7)
e1.insert(0, 'PC Name')

Number_text = StringVar()
e2 = Entry(window, textvariable=Number_text)
e2.grid(row=1, column=7)

CurrentIP_text = StringVar()
e3 = Entry(window, textvariable=CurrentIP_text)
e3.grid(row=2, column=7)

Type_text = StringVar()
e4 = Entry(window, textvariable=Type_text)
e4.grid(row=3, column=7)

Manufacturer_text = StringVar()
e5 = Entry(window, textvariable=Manufacturer_text)
e5.grid(row=4, column=7)

Model_text = StringVar()
e6 = Entry(window, textvariable=Model_text)
e6.grid(row=5, column=7)

BiosVersion_text = StringVar()
e7 = Entry(window, textvariable=BiosVersion_text)
e7.grid(row=6, column=7)

LastUser_text = StringVar()
e8 = Entry(window, textvariable=LastUser_text)
e8.grid(row=7, column=7)

UpdatedDate_text = StringVar()
e9 = Entry(window, textvariable=UpdatedDate_text)
e9.grid(row=8, column=7)

Done_text = StringVar()
e10 = Entry(window, textvariable=Done_text)
e10.grid(row=9, column=7)

UserName_text = StringVar()
e11 = Entry(window, textvariable=UserName_text, width=15)
e11.grid(row=11, column=2)
e11.insert(0, 'User')

Password_text = StringVar()
e12 = Entry(window, textvariable=Password_text, width=15, show="*")
e12.grid(row=11, column=4)
e12.insert(0, "1234")

list1 = Listbox(window, height=16, width=100)
list1.grid(row=1, column=1, rowspan=10, columnspan=5)

list1.bind('<<ListboxSelect>>', get_selected_row)

sb1 = Scrollbar(window)
sb1.grid(row=0, column=0, rowspan=10, sticky='ns')

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview())

b1 = Button(window, text="View All", width=15, command=view_command)
b1.grid(row=0, column=1)

b2 = Button(window, text="Search", width=15, command=search_command)
b2.grid(row=0, column=2)

b3 = Button(window, text="Add", width=15, command=add_command)
b3.grid(row=0, column=3)

b4 = Button(window, text="Update", width=15, command=update_command)
b4.grid(row=0, column=4)

b5 = Button(window, text="Delete", width=15, command=delete_command)
b5.grid(row=0, column=5)

b6 = Button(window, text="Close", width=15, command=window.destroy)
b6.grid(row=11, column=8)

b7 = Button(window, text="Clear", width=15, command=clear)
b7.grid(row=11, column=7)

b8 = Button(window, text="RDP", width=15, command=RDPcommand)
b8.grid(row=0, column=8)

b9 = Button(window, text="Get IP", width=15, command=IPcommand)
b9.grid(row=2, column=8)

b10 = Button(window, text="Get Manufacturer", width=15, command=getmanudacturer)
b10.grid(row=4, column=8)

b11 = Button(window, text="Get Model", width=15, command=getmodel)
b11.grid(row=5, column=8)

b12 = Button(window, text="Get Version", width=15, command=getbiosversion)
b12.grid(row=6, column=8)

b13 = Button(window, text="Today", width=15, command=Today_command)
b13.grid(row=8, column=8)

b14 = Button(window, text="Yes", width=15, command=Done_command)
b14.grid(row=9, column=8)

b15 = Button(window, text="Get All", width=15, command=All_command)
b15.grid(row=11, column=6)

username = UserName_text.get()
password = Password_text.get()
target = Name_text.get()
Session = winrm.Session(target, auth=(username, password))

window.resizable(False, False)

window.mainloop()
