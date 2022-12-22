from tkinter import *
root=Tk()
def getvals():
    print("submiting the form")

    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), addressvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}")




    with open("records.txt" , "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), addressvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n")





root.geometry("456x243")
#headings
Label(root, text="welcome to harry Travels " , font= "comicsansms 13 bold ").grid(row=0, column=3)
#text values
name=Label(root , text= "Name").grid(row=1, column=2)
phone=Label(root , text= "phone").grid(row=2, column=2)
gender=Label(root , text= "gender").grid(row=3, column=2)
address=Label(root , text= "address").grid(row=4, column=2)
paymentmode=Label(root , text= "paymentmode").grid(row=5, column=2)


#tkinter values

namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
addressvalue = StringVar()
paymentmodevalue  = StringVar()
foodservicevalue = IntVar()


#tkinter entry for a form

nameentry = Entry(root , textvariable=namevalue)
phoneentry = Entry(root,textvariable = phonevalue)
genderntry = Entry(root,textvariable= gendervalue)
addressentry = Entry(root , textvariable= addressvalue)
paymentmodeentry = Entry(root , textvariable= paymentmodevalue)

#packing the entry
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderntry.grid(row=3, column=3)
addressentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)



#check box
foodservice = Checkbutton(text="want to prebook your meals" , variable=foodservicevalue)
foodservice.grid(row=6 , column=3)

#button &packing it
Button(text="submit to harry travel" , command=getvals).grid(row=7, column=3)
root.mainloop()