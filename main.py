# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 16:19:32 2020

@author: Yunus
"""

import pNeuma
import tkinter as tk
from tkinter import ttk 

def test(e,chosenType,savecond,chosenType_data):
    pn.load(e)
    if not chosenType:
        print("please choose a vehicle type to get count of it")
    else:
        vehiclenumber = pn.vehicle_type_number(chosenType)
        vehicle_count_label = tk.Label(screen,text="Number of " + chosenType + ": " +
                                       str(vehiclenumber)).grid(row = 4,column=3)
    
    if not chosenType_data:
        print("to get required data, choose a vehicle type\n")
    else:
        data = pn.vehicle_type_data(chosenType_data)
        data.to_csv(str(chosenType_data+".csv"),sep=',',header=pn.splitted)
        vehicle_data_label = tk.Label(screen,text="Saved as " + chosenType_data + ".csv ").grid(row = 5,column=3)

    if savecond == "Yes":
        pn.savetomatlab()
    
    return
# =============================================================================
# MAIN    
# =============================================================================
pn = pNeuma.pNeuma()
screen = tk.Tk()
screen.title("pNEUMA")

screen.geometry("500x200+400+300") 


tk.Label(screen,text="File Name",padx=40,pady=30).grid(row = 3)
e = tk.Entry(screen)
e.grid(row=3,column = 1)

# =============================================================================
# Getting Vehicle Number
# =============================================================================

label1 = tk.Label(screen,text="Vehicle Type ").grid(row = 4)

number= tk.StringVar()  
vehicleChosen= ttk.Combobox(screen, width=18, textvariable=number)  
#Adding Values  
vehicleChosen['values']=("Car","Motorcycle","Bus","Taxi","Medium Vehicle", "Heavy Vehicle")  
vehicleChosen.grid(column=1,row=4) 
# =============================================================================
# desired data for type of vehicle
# =============================================================================
label2 = tk.Label(screen,text="Vehicle Type for Data").grid(row = 5)
vtype = tk.StringVar() 
vehicleChosen_data= ttk.Combobox(screen, width=18, textvariable=vtype)
vehicleChosen_data['values']=("Car","Motorcycle","Bus","Taxi","Medium Vehicle", "Heavy Vehicle")  
vehicleChosen_data.grid(column=1,row=5) 
# =============================================================================
# save to matlab
# =============================================================================
tk.Label(screen,text="Save as Mat File",padx=40,pady=10).grid(row = 6)
number= tk.StringVar()  
numberChosen= ttk.Combobox(screen, width=18, textvariable=number)  
#Adding Values  
numberChosen['values']=("Yes","No")
numberChosen.grid(column=1,row=6)

# =============================================================================
# Ok and quit buttons
# =============================================================================

button_Write = tk.Button(screen, text = "OK", command = lambda: test(e.get(),
                                                                     vehicleChosen.get(),
                                                                     numberChosen.get(),
                                                                     vehicleChosen_data.get())).grid(row=10, column=1)

def quit_():
    screen.quit()
    screen.destroy()

button_ = tk.Button(master=screen, text="Quit", command= quit_)
button_.grid(row=10, column=2)

screen.mainloop() 