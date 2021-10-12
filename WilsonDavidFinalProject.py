## Course: sdev 140
## Author: wilson, d
## Date: 2021-9-28
## Program: M08 Final Project
## Purpose: GUI Final Project

## Import Modules
from tkinter import *


## Variables
windowBanner = "Fur-Get Me Not Charity Drive - David Wilson"

#### Functions
## Main Window Buttons
# Item Buttons
# Items background colors will change between Green for selected and White for unselected
def funcButtonFood():
    if buttonFood.config('bg')[-1] == '#006400':
        buttonFood.config(bg="white")
    else:
        buttonFood.config(bg="#006400")


def funcButtonToys():
    if buttonToys.config('bg')[-1] == '#006400':
        buttonToys.config(bg="white")
    else:
        buttonToys.config(bg="#006400")


def funcButtonBlankets():
    if buttonBlankets.config('bg')[-1] == '#006400':
        buttonBlankets.config(bg="white")
    else:
        buttonBlankets.config(bg="#006400")


def funcButtonMedicine():
    if buttonMedicine.config('bg')[-1] == '#006400':
        buttonMedicine.config(bg="white")
    else:
        buttonMedicine.config(bg="#006400")


def funcButtonServices():
    if buttonServices.config('bg')[-1] == '#006400':
        buttonServices.config(bg="white")
    else:
        buttonServices.config(bg="#006400")


# Organization Buttons
# Organization background colors will change between #006400 for selected and White for unselected
def funcButtonOrgA():
    if buttonOrgA.config('bg')[-1] == '#006400':
        buttonOrgA.config(bg="white")
    else:
        buttonOrgA.config(bg="#006400")


def funcButtonOrgB():
    if buttonOrgB.config('bg')[-1] == '#006400':
        buttonOrgB.config(bg="white")
    else:
        buttonOrgB.config(bg="#006400")


def funcButtonOrgC():
    if buttonOrgC.config('bg')[-1] == '#006400':
        buttonOrgC.config(bg="white")
    else:
        buttonOrgC.config(bg="#006400")


def funcButtonOrgD():
    if buttonOrgD.config('bg')[-1] == '#006400':
        buttonOrgD.config(bg="white")
    else:
        buttonOrgD.config(bg="#006400")


def funcButtonOrgE():
    if buttonOrgE.config('bg')[-1] == '#006400':
        buttonOrgE.config(bg="white")
    else:
        buttonOrgE.config(bg="#006400")


# Main Window Clear All
def funcMainWindowClearAll():
    # Reset all buttons and text entry boxes
    labelNotification.config(text="Form Cleared")
    entryName.delete(0,END)
    entryEmail.delete(0,END)
    entryAddress.delete(0,END)
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
    # Delay to clear "Form Cleared" message after pressing
    mainWindow.update_idletasks()
    mainWindow.after(1000, labelNotification.config(text=""))


def funcCalculation():
    # Variables Used for Total Cost Calculation
    priceSubtotal = 0
    orgCount = 0
    priceTotal = 0
    # Assess price and counts based on button color attribute
    if buttonFood.config('bg')[-1] == '#006400':
        priceSubtotal += 10
    if buttonToys.config('bg')[-1] == '#006400':
        priceSubtotal += 15
    if buttonBlankets.config('bg')[-1] == '#006400':
        priceSubtotal += 20
    if buttonMedicine.config('bg')[-1] == '#006400':
        priceSubtotal += 30
    if buttonServices.config('bg')[-1] == '#006400':
        priceSubtotal += 50
    if buttonOrgA.config('bg')[-1] == "#006400":
        orgCount += 1
    if buttonOrgB.config('bg')[-1] == "#006400":
        orgCount += 1
    if buttonOrgC.config('bg')[-1] == "#006400":
        orgCount += 1
    if buttonOrgD.config('bg')[-1] == "#006400":
        orgCount += 1
    if buttonOrgE.config('bg')[-1] == "#006400":
        orgCount += 1
    #priceTotal = priceSubtotal * orgCount
    #print(priceSubtotal)
    #print(orgCount)
    #print(priceTotal)
    return priceSubtotal, orgCount


def nameCheck():
    # Check for first and last name
    import re
    regex = '[A-Za-z]+ [A-Za-z]+'
    if entryName.get() == "":
        labelNotification.config(text="Name is missing")
        return
    elif re.fullmatch(regex, entryName.get()) == None:
        labelNotification.config(text="Invalid name entry. Requires First and Last name only.")
        return
    else:
        return True


def emailCheck():
    # Check for email formatted to email@domain.tld
    import re
    regex = '[0-9A-Za-z]+@[0-9A-Za-z]+\.[A-Za-z]+'
    if entryEmail.get() == "":
        labelNotification.config(text="Email is missing.")
        return
    elif re.fullmatch(regex, entryEmail.get()) == None:
        labelNotification.config(text="Invalid email entry. Format: email@domain.tld")
        return
    else:
        return True


def addressCheck():
    # Check for three part mailing address
    import re
    regex = '[0-9]+ [A-Za-z]+ [A-Za-z]+'
    if entryAddress.get() == "":
        labelNotification.config(text="Address is missing.")
        return
    elif re.fullmatch(regex, entryAddress.get()) == None:
        labelNotification.config(text="Invalid address entry. Format: ### ABC ABC")
        return
    else:
        return True


def funcContinueMain():
    #priceTotal = 0
    #orgCount = 0
    priceSubtotal, orgCount = funcCalculation()
    #print(priceSubtotal)
    #print(orgCount)
    passName = nameCheck()
    passEmail = emailCheck()
    passAddress = addressCheck()
    if priceSubtotal <= 0:
        labelNotification.config(text="Please make a donation item selection.")
    if orgCount <= 0:
        labelNotification.config(text="Please make an organization  selection.")
    if passName == True and passEmail == True and passAddress == True and priceSubtotal > 0 and orgCount > 0:
        labelNotification.config(text="Form Completed. Opening confirmation window.")
        confirmWindow()


## Main GUI
mainWindow = Tk(className=" "+windowBanner)
mainWindow.config(bg="#AEC6CF")
mainWindow.geometry("800x400")

## Main Window - Title & Pictures
# Listing
labelTitle          = Label(mainWindow, text="Fur-Get Me Not Charity Drive",font=150,bg="#AEC6CF",fg="#006400")
icon1 = PhotoImage(file="icon1.png")
labelIcon1 = Label(mainWindow,image=icon1)
donateIcon = PhotoImage(file="donate.png")
labelDonateIcon = Label(mainWindow,image=donateIcon)

# Display
labelTitle.place(x=275,y=10)
labelIcon1.place(x=150,y=20)
labelDonateIcon.place(x=150, y=220)


## Main Window - Field Entry
# Listing
labelName   = Label(mainWindow, text="Full Name:",bg="#AEC6CF",fg="#006400",font=15)
entryName    = Entry(mainWindow, width=30)
labelEmail  = Label(mainWindow, text="Email:",bg="#AEC6CF",fg="#006400",font=15)
entryEmail    = Entry(mainWindow, width=30)
labelAddress= Label(mainWindow, text="Address:",bg="#AEC6CF",fg="#006400",font=15)
entryAddress    = Entry(mainWindow, width=30)

# Display
labelName.place(x=10,y=100)
entryName.place(x=120,y=100)
labelEmail.place(x=10,y=140)
entryEmail.place(x=120,y=140)
labelAddress.place(x=10,y=180)
entryAddress.place(x=120,y=180)

## Main Window - Item Selection
# Listing
labelDonationsTitle = Label(mainWindow, text="Donation Item Options",bg="#AEC6CF",fg="white")
buttonFood          = Button(mainWindow, text="Pet Food ($10)",width=20,bg="white",command=funcButtonFood)
buttonToys          = Button(mainWindow, text="Pet Toys ($15)",width=20,bg="white",command=funcButtonToys)
buttonBlankets      = Button(mainWindow, text="Pet Blankets ($20)",bg="white",width=20,command=funcButtonBlankets)
buttonMedicine      = Button(mainWindow, text="Medication ($30)",bg="white",width=20,command=funcButtonMedicine)
buttonServices      = Button(mainWindow, text="Medical Services ($50)",bg="white",width=20,command=funcButtonServices)
# Display
labelDonationsTitle.place(x=415,y=60)
buttonFood.place(x=400,y=100)
buttonToys.place(x=400,y=140)
buttonBlankets.place(x=400,y=180)
buttonMedicine.place(x=400,y=220)
buttonServices.place(x=400,y=260)

## Main Window - Organization Selection
# Listing
labelOrganizationTitle = Label(mainWindow, text="Organization Options",bg="#AEC6CF",fg="white")
buttonOrgA             = Button(mainWindow, text="Organization A",width=20,bg="white",command=funcButtonOrgA)
buttonOrgB             = Button(mainWindow, text="Organization B",width=20,bg="white",command=funcButtonOrgB)
buttonOrgC             = Button(mainWindow, text="Organization C",width=20,bg="white",command=funcButtonOrgC)
buttonOrgD             = Button(mainWindow, text="Organization D",width=20,bg="white",command=funcButtonOrgD)
buttonOrgE             = Button(mainWindow, text="Organization E",width=20,bg="white",command=funcButtonOrgE)
# Display
labelOrganizationTitle.place(x=615,y=60)
buttonOrgA.place(x=600,y=100)
buttonOrgB.place(x=600,y=140)
buttonOrgC.place(x=600,y=180)
buttonOrgD.place(x=600,y=220)
buttonOrgE.place(x=600,y=260)


## Clear & Confirm Footer
# Listing
buttonClearMain      = Button(mainWindow, text="Clear All",width=20,bg="white",command=funcMainWindowClearAll)
buttonContinueMain   = Button(mainWindow, text="Confirm Selections",width=20,bg="white",command=funcContinueMain)
labelNotification    = Label(mainWindow, text=" ",bg="#AEC6CF",fg="white")

# Display
buttonClearMain.place(x=400,y=320)
buttonContinueMain.place(x=600,y=320)
labelNotification.place(x=400,y=360)



###############################


def confirmWindow():

    def funcCloseWindow():
        # Exit button will close both windows
        confirmWindow.destroy()
        mainWindow.destroy()


    def funcPlaceOrder():
        # Null function
        pass


    priceSubtotal, orgCount = funcCalculation()
    ## Confirm GUI
    confirmWindow = Tk(className=" " + windowBanner)
    confirmWindow.config(bg="#AEC6CF")
    confirmWindow.geometry("800x400")

    ## Confirm Window - Title & Pictures
    # Listing
    labelTitle = Label(confirmWindow, text="Fur-Get Me Not Charity Drive - Confirmation", font=150, bg="#AEC6CF", fg="#006400")


    # Display
    labelTitle.place(x=275, y=10)


    ## Confirm Window - Field Labels
    # Listing
    labelName           = Label(confirmWindow, text="Full Name:", bg="#AEC6CF", fg="#006400", font=15)
    labelNameConfirm    = Label(confirmWindow, text=entryName.get(),bg="#AEC6CF", fg="#006400", font=15)
    labelEmail          = Label(confirmWindow, text="Email:", bg="#AEC6CF", fg="#006400", font=15)
    labelEmailConfirm   = Label(confirmWindow, text=entryEmail.get(),bg="#AEC6CF", fg="#006400", font=15)
    labelAddress        = Label(confirmWindow, text="Address:", bg="#AEC6CF", fg="#006400", font=15)
    labelAddressConfirm = Label(confirmWindow, text=entryAddress.get(),bg="#AEC6CF", fg="#006400", font=15)

    # Display
    labelName.place(x=10, y=100)
    labelNameConfirm.place(x=120, y=100)
    labelEmail.place(x=10, y=140)
    labelEmailConfirm.place(x=120, y=140)
    labelAddress.place(x=10, y=180)
    labelAddressConfirm.place(x=120, y=180)

    ## Confirm Window - Item Selections
    # Listing
    labelDonationsTitle  = Label(confirmWindow, text="Items Selected", bg="#AEC6CF", fg="white")
    labelFoodConfirm     = Label(confirmWindow, text="Pet Food ($10)", width=20, fg="#006400", bg="#AEC6CF")
    labelToysConfirm     = Label(confirmWindow, text="Pet Toys ($15)", width=20, fg="#006400", bg="#AEC6CF")
    labelBlanketsConfirm = Label(confirmWindow, text="Pet Blankets ($20)", width=20, fg="#006400", bg="#AEC6CF")
    labelMedicineConfirm = Label(confirmWindow, text="Medication ($30)", width=20, fg="#006400", bg="#AEC6CF")
    labelServicesConfirm = Label(confirmWindow, text="Medical Services ($50)", width=20, fg="#006400", bg="#AEC6CF")

    # Display - Labels will appear if selected on previous window by checking for color attribute
    labelDonationsTitle.place(x=420, y=60)
    if buttonFood.config('bg')[-1] == '#006400':
        labelFoodConfirm.place(x=400, y=100)
    if buttonToys.config('bg')[-1] == '#006400':
        labelToysConfirm.place(x=400, y=140)
    if buttonBlankets.config('bg')[-1] == '#006400':
        labelBlanketsConfirm.place(x=400, y=180)
    if buttonMedicine.config('bg')[-1] == '#006400':
        labelMedicineConfirm.place(x=400, y=220)
    if buttonServices.config('bg')[-1] == '#006400':
        labelServicesConfirm.place(x=400, y=260)

    ## Confirm Window - Organization Selections
    # Listing
    labelOrganizationTitle = Label(confirmWindow, text="Organizations Selected", bg="#AEC6CF", fg="white")
    labelOrgAConfirm = Label(confirmWindow, text="Organization A", width=20, fg="#006400", bg="#AEC6CF")
    labelOrgBConfirm = Label(confirmWindow, text="Organization B", width=20, fg="#006400", bg="#AEC6CF")
    labelOrgCConfirm = Label(confirmWindow, text="Organization C", width=20, fg="#006400", bg="#AEC6CF")
    labelOrgDConfirm = Label(confirmWindow, text="Organization D", width=20, fg="#006400", bg="#AEC6CF")
    labelOrgEConfirm = Label(confirmWindow, text="Organization E", width=20, fg="#006400", bg="#AEC6CF")

    # Display
    labelOrganizationTitle.place(x=610, y=60)
    if buttonOrgA.config('bg')[-1] == '#006400':
        labelOrgAConfirm.place(x=600, y=100)
    if buttonOrgB.config('bg')[-1] == '#006400':
        labelOrgBConfirm.place(x=600, y=140)
    if buttonOrgC.config('bg')[-1] == '#006400':
        labelOrgCConfirm.place(x=600, y=180)
    if buttonOrgD.config('bg')[-1] == '#006400':
        labelOrgDConfirm.place(x=600, y=220)
    if buttonOrgE.config('bg')[-1] == '#006400':
        labelOrgEConfirm.place(x=600, y=260)


    ## Confirmation Total
    # Listing
    labelPriceTotal       = Label(confirmWindow, fg="#006400", bg="#AEC6CF", font=10,text="  Item Total:")
    labelPriceTotalNumber = Label(confirmWindow, fg="#006400", bg="#AEC6CF", font=10,text="$" + str(priceSubtotal))
    labelOrgTotal         = Label(confirmWindow, fg="#006400", bg="#AEC6CF", font=10,text="x Organizations:")
    labelOrgTotalNumber   = Label(confirmWindow, fg="#006400", bg="#AEC6CF", font=10,text= str(orgCount))
    labelBar              = Label(confirmWindow, fg="#006400", bg="#AEC6CF", font=10,text="--------------------------")
    labelGrandTotal       = Label(confirmWindow, fg="#006400", bg="#AEC6CF", font=10,text="= Grand Total:")
    labelGrandTotalNumber = Label(confirmWindow, fg="#006400", bg="#AEC6CF", font=10,text="$" + str(priceSubtotal * orgCount))

    # Display
    labelPriceTotal.place(x=20, y=220)
    labelPriceTotalNumber.place(x=160, y=220)
    labelOrgTotal.place(x=20, y=260)
    labelOrgTotalNumber.place(x=160, y=260)
    labelBar.place(x=20, y=300)
    labelGrandTotal.place(x=20, y=340)
    labelGrandTotalNumber.place(x=160, y=340)

    ## Exit & Confirm Footer
    # Listing
    buttonCloseWindow  = Button(confirmWindow, text="Exit Confirmation", width=20, bg="white", command=funcCloseWindow)
    buttonConfirmOrder = Button(confirmWindow, text="Confirm Order", width=20, bg="white", command=funcPlaceOrder)
    labelNotification  = Label(confirmWindow, text=" ", bg="#AEC6CF", fg="white")

    # Display
    buttonCloseWindow.place(x=400, y=320)
    buttonConfirmOrder.place(x=600, y=320)
    labelNotification.place(x=400, y=360)


## Main Loop
mainWindow.mainloop()