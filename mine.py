import tkinter as tk
from datetime import datetime
import sqlite3
database = sqlite3.connect("stocks.db")
cursor = database.cursor()


frame = tk.Tk()
frame.title("app")
""" THIS FUNCTION CONTAINS CODE
FOR SECOND WINDOW FOR UPDATING STOCK"""

def update():
    frame.destroy()
    frame2 = tk.Tk()
    frame2.title("app2")
    labelname = tk.Label( frame2, text = " Enter Product Name To Be Updated")
    updateProductName = tk.Entry(frame2)
    labelname.pack()
    updateProductName.pack()
    labelname = tk.Label( frame2, text = " Enter Quantity To Be Updated")
    updateProductQuantity = tk.Entry(frame2)
    labelname.pack()
    updateProductQuantity.pack()
    labelname =  tk.Label( frame2, text = " Enter Price  To Be Updated")
    labelname = tk.Label( frame2, text = " Where ID  Is") 
    updateProductId = tk.Entry(frame2)
    labelname.pack()
    updateProductId.pack()   
    frame2.mainloop()
    
  
def delete():
     frame.destroy()  

def inputs(): #code to insert values in the table
    productN = productname.get()
    productID = productid.get()
    productQ = productquantity.get()
    productP = productPrice.get()
    productP2 = float(productP) * float( productQ)
    productD = str(datetime.now())
    lbl.config(text="you have added" + productN + " with ID"+ productID + " of quantity " + productQ  + " on " + productD )
    cursor.execute("""INSERT INTO stocksDetails (productsName, id, quantity, price ,priceQuantity, date) values (?,?,?,?,?,?) """, (productN,productID, productQ,productP,productP2 , productD ))
    database.commit()
    database.close()
"""THIS CODE IS FOR THE FIRST WINDOW"""
labelname = tk.Label( frame, text = " Enter Product Name")
productname = tk.Entry(frame)
labelname.pack()
productname.pack()
labelname = tk.Label(frame , text = " Enter Product ID")
productid = tk.Entry(frame)
labelname.pack()
productid.pack()
labelname = tk.Label(frame, text = " Enter Product Quantity")
productquantity = tk.Entry(frame)
labelname.pack()
productquantity.pack()
labelname = tk.Label(frame, text = " Enter Product Price")
productPrice = tk.Entry(frame)
labelname.pack()
productPrice.pack()
Button = tk.Button(frame, text = "Add to stock", command = inputs)
Button.pack()
Button2 = tk.Button(frame, text = "Update", command = update )
Button2.pack()
Button3 = tk.Button(frame, text = "Delete" ,command = delete)
Button3.pack()
exitButton = tk.Button(frame, text = "Exit", command = frame.destroy)
exitButton.pack()
lbl = tk.Label(frame, text= "")
lbl.pack()
""" THIS CODE IS FOR THE UPDATE WINDOW"""

frame.mainloop()
