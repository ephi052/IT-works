import sqlite3


def connect():
    conn = sqlite3.connect("Data.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Data (id INTEGER PRIMARY KEY, Name TEXT, Number INTEGER, CurrentIP INTEGER, "
        "Type INTEGER,Manufacturer TEXT, Model TEXT, BiosVersion TEXT, LastUser TEXT, UpdatedDate INTEGER, Done TEXT)")
    conn.commit()
    conn.close()


def insert(Name, CurrentIP, Number, Type, Manufacturer, Model, BiosVersion, LastUser, UpdatedDate, Done):
    conn = sqlite3.connect("Data.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Data VALUES(NULL,?,?,?,?,?,?,?,?,?,?)", (Name, CurrentIP, Number, Type, Manufacturer, Model, BiosVersion, LastUser, UpdatedDate, Done))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("Data.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM Data")
    rows = cursor.fetchall()
    conn.close()
    return rows


def search(Name="", CurrentIP="", Number="", Type="", Manufacturer="", Model="", BiosVersion="",LastUser="", UpdatedDate="", Done=""):
    conn = sqlite3.connect("Data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Data WHERE Name = ? OR CurrentIP = ? OR Number = ? OR Type = ? OR Manufacturer = ? OR Model = ? OR BiosVersion = ? OR LastUser = ? OR UpdatedDate = ? OR Done = ? ", (Name, CurrentIP, Number, Type, Manufacturer, Model, BiosVersion,LastUser, UpdatedDate, Done))
    #cursor.execute("SELECT * FROM Data WHERE Number = ?", (Number))
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("Data.db")
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM Data WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, Name, CurrentIP, Number, Type, Manufacturer, Model, BiosVersion, LastUser, UpdatedDate, Done):
    conn = sqlite3.connect("Data.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Data SET Name=?, CurrentIP=?,Number=?,Type=?, Manufacturer=?, Model=?, BiosVersion=?, LastUser=?, "
        "UpdatedDate=?, "
        "Done=? WHERE id=?", (Name, CurrentIP, Number, Type, Manufacturer, Model, BiosVersion, LastUser, UpdatedDate,
                              Done, id))
    conn.commit()
    conn.close()
