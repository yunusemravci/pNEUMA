# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 16:19:32 2020

@author: Yunus
"""

import pNeuma
import tkinter as tk
from tkinter import ttk 

def test(e,chosenType,savecond,chosenType_data,plotinfo,plot_ID):
    pn.load(e)
    if not chosenType:
        print("*\tplease choose a vehicle type to get count of it")
    else:
        vehiclenumber = pn.vehicle_type_number(chosenType)
        vehicle_count_label = tk.Label(screen,text="Number of " + chosenType + ": " +
                                       str(vehiclenumber)).grid(row = 4,column=3)
    
    if not chosenType_data:
        print("*\t to get required data, choose a vehicle type\n")
    else:
        data = pn.vehicle_type_data(chosenType_data)
        data.to_csv(str(chosenType_data+".csv"),sep=';')
        vehicle_data_label = tk.Label(screen,text="Saved as " + chosenType_data + ".csv ").grid(row = 5,column=3)

    if savecond == "Yes":
        pn.savetomatlab()
        tk.Label(screen,text="Saved as pneuma_sample_dataset.mat ").grid(row = 6,column=3)
    else:
        print("*\tTo save data into .mat choose Yes option")
    
    if not plotinfo:
        print("*\tChoose a column to draw frequency of a specified vehicle")
    else:
        if int(plot_ID) < 1 or int(plot_ID) > 2348:
            print("*\tTrack id should be btw 1 - 2348\n")
        else:
            select_track = pn.df.iloc[int(plot_ID)] #should be fixed plot_id value cause plot value is more than 1,
                                                        #value entered in the interface.
            print(select_track[" lon"])
            pn.plot_(plotinfo,select_track)
        
    print("\n----\n")
    return
# =============================================================================
# MAIN    
# =============================================================================
pn = pNeuma.pNeuma()
screen = tk.Tk()
screen.title("pNEUMA")

screen.geometry("800x400+400+300") 


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
label2 = tk.Label(screen,text="Vehicle Type for Data",padx=10,pady=10).grid(row = 5)
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
# Count of vehicle in a way
# =============================================================================
tk.Label(screen,text="One way vehicle count btw coords, (X1,Y1)-(X1,Y2)\n Entries X1 Y1 Y2 respectively ").grid(row = 7)

lat = tk.Entry(screen)
lat.grid(row = 7, column = 1)
lot1 = tk.Entry(screen)
lot1.grid(row = 7, column = 2)
lot2 = tk.Entry(screen)
lot2.grid(row = 7, column = 3)
# =============================================================================
# Count of vehicle in an area
# =============================================================================
tk.Label(screen,text="Area vehicle count btw specified coords\n Entries X1 X2 Y1 Y2 respectively ").grid(row = 9)
number= tk.StringVar()

lat = tk.Entry(screen)
lat.grid(row = 9, column = 1)
lat2 = tk.Entry(screen)
lat2.grid(row = 9, column = 2)
lot1 = tk.Entry(screen)
lot1.grid(row = 9, column = 3)
lot2 = tk.Entry(screen)
lot2.grid(row = 9, column = 4)
# =============================================================================
# PLOT
# =============================================================================
tk.Label(screen,text="Plot for a vehicle",padx=10,pady=10).grid(row = 11)
plot_column = tk.StringVar()

plot_combobox= ttk.Combobox(screen, width=18, textvariable=plot_column)
plot_combobox['values']=("lat","lon","speed","tan_accel","lat_accel")
plot_combobox.grid(column=1,row=11)

label3 = tk.Label(screen,text="Vehicle ID ").grid(row = 11, column = 2)
vehicle_ID = tk.Entry(screen)
vehicle_ID.grid(column=3,row=11)

# =============================================================================
# Ok and quit buttons
# =============================================================================

button_Write = tk.Button(screen, text = "OK", command = lambda: test(e.get(),
                                                                     vehicleChosen.get(),
                                                                     numberChosen.get(),
                                                                     vehicleChosen_data.get(),
                                                                     plot_combobox.get(),
                                                                     vehicle_ID.get())).grid(row=12, column=1)

def quit_():
    screen.quit()
    screen.destroy()

button_ = tk.Button(master=screen, text="Quit", command= quit_)
button_.grid(row=12, column=2)

screen.mainloop() 
