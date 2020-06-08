# -*- coding: utf-8 -*-
"""
Created on Thu May 14 22:53:54 2020

@author: Yunus
"""
import pandas as pd
import numpy as np
import os
import csv
import scipy.io as sio

# =============================================================================
# pNEUMA 
# =============================================================================

class pNeuma:
    
    path = os.getcwd() + '/pneuma_sample_dataset/pneuma_piece.csv'
    
    df=pd.DataFrame()
    
    def load(self):

        headers = pd.read_csv(self.path, nrows=0).columns.tolist()
        word = headers[0]

        splitted = word.split(';')
        #print(splitted[0])
        self.df = pd.read_csv(self.path,delimiter=';')

        #print(df[splitted[1]])
        return splitted
# =============================================================================
# saves the dataframe into matlab    
# =============================================================================
    def savetomatlab(self):
#        truncDataFrame.rename(columns=lambda x:'col_' + x.replace(' ', '_'), inplace=True)  
#        scipy.io.savemat('EEGdata2.mat', {'struct2':truncDataFrame.to_dict("list")})
        sio.savemat('pneuma_sample_dataset.mat', self.df)
        
# =============================================================================
# finds and returns count of vehicle type
# =============================================================================
    def vehicle_type_number(self,vehicle_type,dff):
        
        counter = 0        
        allvehicle_types = self.df[dff[1]]

        for i in range(len(allvehicle_types)):
            
            vehicle = allvehicle_types[i]
            if vehicle.replace(' ', '') == vehicle_type:
                counter += 1
        
        return counter
# =============================================================================
# returns all data of specified vehicle type e.g. car 
#         
# =============================================================================
    def vehicle_type_data(self,vehicle_type):
        
        typed_data = pd.DataFrame()
        
        for i in range(len(self.df)):
           allvehicle_types = self.df[dff[1]]  
           vehicle = allvehicle_types[i]
           if vehicle.replace(' ', '') == vehicle_type: 
               typed_data = typed_data.append(self.df.iloc[i, :])
        
        print(typed_data)
        return typed_data

# =============================================================================
# counts the number of vehicle in specified area which coord specified by 
# latitude and longitude    
# =============================================================================
    def vehicle_count_in_area(self,lat,lon):
        
        return
    
        
    
    def plot_():
        
        return
# =============================================================================
# MAIN    
# =============================================================================
pn = pNeuma()
dff = pn.load()
print(pn.vehicle_type_number("Car",dff))
pn.vehicle_type_data("Motorcycle")


