
This repository is for my IT scripts and projects.

# Projects list

## Folder Sync

Simple folder sync using dirsync and tkinter librarys graphical interface

### dependencies

- pip install tk

- pip install dirsync

## Bios Update Manager

### Introduction

The task I was given at work to Update the BIOS on all DELL Computers in the office.

[As shown in the Elysium article there are 2 vulnerabilities in the Connect BIOS feature in 129 models. DELL recommend](https://eclypsium.com/2021/06/24/biosdisconnect/)

DELL REMOTE OS RECOVERY disable do or, latest BIOS version

### Features and actions

 - Connect to base data or create a new one if not

 - Search by first data (in all data)

 - View all records

 - Create a record

 - Update record

 - Delete a record

 - Fill in a given information (manufacturer, model, BIOS version, IP address (by computer name)

 - Fill in all the details of the record

 - Update login information in RDP file

 - RDP button to connect to the computer

### Code. Protocol and commands

The code is divided to frontend and backend.

frontend - deals with GUI and the logic of button operations

backend - SQL commands and information management

For operations on the host I use the os.python directory to run CMD commands `cmdkey / generic: target / user: username / pass: password`

    mstsc "the_target"

For remote computer operations I use the PyWinrm library in the Winrm protocol to send

CMD commands

    wmic nicconfig where "IPEnabled = True" get ipaddress

    wmic computer system get manufacturer

    wmic computer system get model

    wmic computer system get model

WINRM protocol is a protocol built into the operating system and no installation is required

But it is necessary to enable this protocol at the Example Policy Group level

Bios Update Manager Programmed

post Scriptum. Ansible can be used for authentication

### Libraries

 - tkinter for the interface

 - os for host commands

 - PyWinrm for remote computer commands

 - Datetime saving of dates, etc.

 - database for sqlite3

### Format and usage

The software needs a DB file in the appropriate format to work with an existing list, for which I created a DB file

With all 450 computers from the consolidated registry I made, if there is no such file in the shared folder

(For code files), the software will create a new one.

**Database format**
- id INTEGER PRIMARY KEY
- Name TEXT
- Number INTEGER
- CurrentIP INTEGER
- Type INTEGER
- Manufacturer TEXT
- Model TEXT
- BiosVersion TEXT
- LastUser TEXT
- UpdatedDate INTEGER
- Done TEXT

The software will open with an empty list to see the list should click "All View." You can select

Record and edit it, in order for the changes to be saved, click "Update." In addition, you can add an "Add," record.

Delete "Delete" entry, clear all "Clear" entry content

In order to use GET or RDP you need to enter a username, password and computer name. In addition can be done

"All Get" for IP, manufacturer, model, and BIOS data installed on the target computer.
### Improvements for next version
- The software is written (at this stage) without Try-Except This means that the software only works if the user Do everything correctly and if there is a malfunction or incorrect data was entered, there is no indication to the user dont know where it fail, and an error Python is obtained
- Logic of registration marking as performed, by checking the model against the list of Elysium models
- "Computer is at risk" alert (from the list)
- PLAY button that runs the fabric on a list of computers one after the other
- GET USER button
- Web based GUI

## Mailbox folder permission scripts generator

For adding permissions to mailboxes folders like calender, contacts, etc. between multiple users. in Exchange Shell without using Active Directory.