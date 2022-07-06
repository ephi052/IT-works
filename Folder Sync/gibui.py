import tkinter as tk
from tkinter import StringVar, ttk, filedialog as fd
from tkinter.messagebox import showinfo
from dirsync import sync

SorceFolder = ""
TargetFolder = ""

root = tk.Tk()  # create a window
root.title('DirSync')  # set title of window
root.resizable(False, False)  # disable resizing of window
root.eval('tk::PlaceWindow . center')  # center window


def select_file_ss():
    """Function to select source folder"""
    SF = fd.askdirectory()
    sorceFolderEntery.insert(0, SF)


def select_file_st():
    """Function to select target folder"""
    TF = fd.askdirectory()
    targetFolderEntery.insert(0, TF)


def check():
    """Function to check data in folders printout the different files and folders"""
    if not checkInputs() != True:
        sync(theSourceFolder.get(), theTargetFolder.get(), 'diff', )


def syncCommand():
    """Function to sync folders"""
    if not checkInputs() != True:
        sync(theSourceFolder.get(), theTargetFolder.get(), 'sync', )


def checkInputs():
    """Function to check if inputs are empty"""
    if theSourceFolder.get() == "" or theTargetFolder.get() == "":
        showinfo(title='Info', message='Select Folders Path')
        return False
    else:
        return True

# GUI
btSize = 30  # set buttons size
# sorceFolder button
sorceFolder = ttk.Button(root, text='Select Source', command=select_file_ss)
sorceFolder.grid(column=0, row=1, ipadx=btSize)

# targetFolder button
targetFolder = ttk.Button(root, text='Select Target', command=select_file_st)
targetFolder.grid(column=0, row=2, ipadx=btSize)

# check differences button
checkBt = ttk.Button(root, text='Check', command=check)
checkBt.grid(column=0, row=3, ipadx=btSize)

# backup button
backupBt = ttk.Button(root, text='sync', command=syncCommand)
backupBt.grid(column=1, row=3, ipadx=75, columnspan=2)

theSourceFolder = StringVar()  # create a string variable for sorceFolder entry
sorceFolderEntery = tk.Entry(root, textvariable=theSourceFolder)  # create sorceFolder entry
sorceFolderEntery.grid(column=1, row=1, ipadx=75, columnspan=2)

theTargetFolder = StringVar()
targetFolderEntery = tk.Entry(root, textvariable=theTargetFolder)
targetFolderEntery.grid(column=1, row=2, ipadx=75, columnspan=2)

root.mainloop()
