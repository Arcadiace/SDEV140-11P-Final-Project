## Course: sdev 140
## Author: wilson, d
## Date: 2021-9-28
## Program: M08 Final Project
## Purpose: GUI Final Project

## Import Modules
from tkinter import *

## Variables
windowBanner = "David Wilson - Animal Donations - Basic GUI"

#### Functions
## Main Window Buttons
# Item Buttons
# Items background colors will change between Green for selected and White for unselected
def funcButtonFood():
    if buttonFood.config('bg')[-1] == 'green':
        buttonFood.config(bg="white")
    else:
        buttonFood.config(bg="green")


def funcButtonToys():
    if buttonToys.config('bg')[-1] == 'green':
        buttonToys.config(bg="white")
    else:
        buttonToys.config(bg="green")


def funcButtonBlankets():
    if buttonBlankets.config('bg')[-1] == 'green':
        buttonBlankets.config(bg="white")
    else:
        buttonBlankets.config(bg="green")


def funcButtonMedicine():
    if buttonMedicine.config('bg')[-1] == 'green':
        buttonMedicine.config(bg="white")
    else:
        buttonMedicine.config(bg="green")


def funcButtonServices():
    if buttonServices.config('bg')[-1] == 'green':
        buttonServices.config(bg="white")
    else:
        buttonServices.config(bg="green")


# Organization Buttons
# Organization background colors will change between Green for selected and White for unselected
def funcButtonOrgA():
    if buttonOrgA.config('bg')[-1] == 'green':
        buttonOrgA.config(bg="white")
    else:
        buttonOrgA.config(bg="green")


def funcButtonOrgB():
    if buttonOrgB.config('bg')[-1] == 'green':
        buttonOrgB.config(bg="white")
    else:
        buttonOrgB.config(bg="green")


def funcButtonOrgC():
    if buttonOrgC.config('bg')[-1] == 'green':
        buttonOrgC.config(bg="white")
    else:
        buttonOrgC.config(bg="green")


def funcButtonOrgD():
    if buttonOrgD.config('bg')[-1] == 'green':
        buttonOrgD.config(bg="white")
    else:
        buttonOrgD.config(bg="green")


def funcButtonOrgE():
    if buttonOrgE.config('bg')[-1] == 'green':
        buttonOrgE.config(bg="white")
    else:
        buttonOrgE.config(bg="green")


# Main Window Clear All
def funcMainWindowClearAll():
    labelFormCleared.config(text="Form Cleared")
    buttonFood.config(bg="white")
    buttonToys.config(bg="white")
    buttonBlankets.config(bg="white")
    buttonMedicine.config(bg="white")
    buttonServices.config(bg="white")
    buttonOrgA.config(bg="white")
    buttonOrgB.config(bg="white")
    buttonOrgC.config(bg="white")
    buttonOrgD.config(bg="white")
    buttonOrgE.config(bg="white")
    mainWindow.update_idletasks()
    mainWindow.after(1000, labelFormCleared.config(text=""))

def funcContinueMain():
    priceSubtotal = 0
    orgCount = 0
    priceTotal = 0
    if buttonFood.config('bg')[-1] == 'green':
        priceSubtotal += 10
    if buttonToys.config('bg')[-1] == 'green':
        priceSubtotal += 15
    if buttonBlankets.config('bg')[-1] == 'green':
        priceSubtotal += 20
    if buttonMedicine.config('bg')[-1] == 'green':
        priceSubtotal += 30
    if buttonServices.config('bg')[-1] == 'green':
        priceSubtotal += 50
    if buttonOrgA.config('bg')[-1] == "green":
        orgCount += 1
    if buttonOrgB.config('bg')[-1] == "green":
        orgCount += 1
    if buttonOrgC.config('bg')[-1] == "green":
        orgCount += 1
    if buttonOrgD.config('bg')[-1] == "green":
        orgCount += 1
    if buttonOrgE.config('bg')[-1] == "green":
        orgCount += 1
    priceTotal = priceSubtotal * orgCount
    print(priceSubtotal)
    print(orgCount)
    print(priceTotal)


## Main GUI
mainWindow = Tk(className=" "+windowBanner)
mainWindow.config(bg="blue")


## Main Window - Item Selection - Left Column
# Listing
labelDonationsTitle = Label(mainWindow, text="Donation Item Options",bg="blue",fg="white")
buttonFood          = Button(mainWindow, text="Pet Food ($10)",width=20,bg="white",command=funcButtonFood)
buttonToys          = Button(mainWindow, text="Pet Toys ($15)",width=20,bg="white",command=funcButtonToys)
buttonBlankets      = Button(mainWindow, text="Pet Blankets ($20)",bg="white",width=20,command=funcButtonBlankets)
buttonMedicine      = Button(mainWindow, text="Medication ($30)",bg="white",width=20,command=funcButtonMedicine)
buttonServices      = Button(mainWindow, text="Medical Services ($50)",bg="white",width=20,command=funcButtonServices)
# Display
labelDonationsTitle.grid(row=1,column=0)
buttonFood.grid(row=2,column=0)
buttonToys.grid(row=3,column=0)
buttonBlankets.grid(row=4,column=0)
buttonMedicine.grid(row=5,column=0)
buttonServices.grid(row=6,column=0)

## Main Window - Organization Select - Right Column
# Listing
labelOrganizationTitle = Label(mainWindow, text="Organization Options",bg="blue",fg="white")
buttonOrgA             = Button(mainWindow, text="Organization A",width=20,bg="white",command=funcButtonOrgA)
buttonOrgB             = Button(mainWindow, text="Organization B",width=20,bg="white",command=funcButtonOrgB)
buttonOrgC             = Button(mainWindow, text="Organization C",width=20,bg="white",command=funcButtonOrgC)
buttonOrgD             = Button(mainWindow, text="Organization D",width=20,bg="white",command=funcButtonOrgD)
buttonOrgE             = Button(mainWindow, text="Organization E",width=20,bg="white",command=funcButtonOrgE)
# Display
labelOrganizationTitle.grid(row=1,column=2)
buttonOrgA.grid(row=2,column=2)
buttonOrgB.grid(row=3,column=2)
buttonOrgC.grid(row=4,column=2)
buttonOrgD.grid(row=5,column=2)
buttonOrgE.grid(row=6,column=2)

## Main Window - Spacers
# Listing
labelMainWindowColumnSpacer = Label(mainWindow, text="",width=2,bg="blue")
labelClearMainSpacer        = Label(mainWindow, text="",width=20,bg="blue")
# Display
# Between "Pet Food" and "Organization A" buttons
labelMainWindowColumnSpacer.grid(row=0,column=1)
# Between "Clear All" and "Continue" buttons
labelClearMainSpacer.grid(row=7,column=0)

## Clear & Confirm Footer
# Listing
buttonClearMain      = Button(mainWindow, text="Clear All",width=20,bg="white",command=funcMainWindowClearAll)
buttonContinueMain   = Button(mainWindow, text="Confirm Selections",width=20,command=funcContinueMain)
labelFormCleared     = Label(mainWindow, text=" ",width=20,bg="blue",fg="white")

# Display
buttonClearMain.grid(row=8,column=0)
buttonContinueMain.grid(row=8,column=2)
labelFormCleared.grid(row=9,column=0)

## Main Loop
mainWindow.mainloop()
