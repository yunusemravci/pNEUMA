# -*- coding: utf-8 -*-
"""
Created on Thu May 14 22:53:54 2020
@author: Yunus
"""
import pandas as pd
import numpy as np
import os
import scipy.io as sio

# =============================================================================
# pNEUMA 
# =============================================================================

class pNeuma:
    
    path = os.getcwd() + '/pneuma_sample_dataset/'
    
    df=pd.DataFrame()
    splitted = []
    
    def load(self,filename):
        
        headers = pd.read_csv(self.path + filename, nrows=0).columns.tolist()
        word = headers[0]

        self.splitted = word.split(';')
        #print(splitted[0])
        
        self.df = pd.read_csv(self.path + filename,delimiter=';',low_memory=False)
                
# =============================================================================
# saves the dataframe as .mat    
# =============================================================================
    def savetomatlab(self):

        sio.savemat('pneuma_sample_dataset.mat', self.df)
        print("Dataframe saved as mat file in working directory")
# =============================================================================
# finds and returns count of vehicle type
# =============================================================================
    def vehicle_type_number(self,vehicle_type):
        
        counter = 0        
        allvehicle_types = self.df[self.splitted[1]]

        for i in range(len(allvehicle_types)):
            
            vehicle = allvehicle_types[i]
            if vehicle.replace(' ', '') == vehicle_type:
                counter += 1
        #print(counter)
        return counter
# =============================================================================
# 
# =============================================================================
#def vehicle_type_number(self,vehicle_type,dff):
#    return

# =============================================================================
# returns all data of specified vehicle type e.g. car 
#         
# =============================================================================
    def vehicle_type_data(self,vehicle_type):
        
        typed_data = pd.DataFrame()
        
        allvehicle_types = self.df[self.splitted[1]]  
           
        
        for i in range(len(self.df)):
           vehicle = allvehicle_types[i]
           if vehicle.replace(' ', '') == vehicle_type: 
               typed_data = typed_data.append(self.df.iloc[i, :])
        
        
        return typed_data

# =============================================================================
# counts the number of vehicle in specified area which coord specified by 
# latitude and longitude    
# =============================================================================
    def vehicle_count_in_a_way(self,lat,lon,time):
        count = 0
        
        time_col = time / 400.0
        time_col = 10 + time_col * 6
        time_col_name = "Unnamed: " + str(time_col)
        time_lat_col = time_col - 5 
        time_lon_col = time_col - 4
        
        time_lat_name = "Unnamed: " + str(time_lat_col)
        time_lon_name = "Unnamed: " + str(time_lon_col)
        latitudes = self.df[time_lat_name]
        longitudes = self.df[time_lon_name]
        
        lat = lat.sort()
        lon = lon.sort()
        for i in range(len(self.df)):
            if latitudes[i] >= lat[0] and latitudes[i] <= lat[1]:
                if longitudes[i] >= lon[0] and longitudes[i] <= lon[1]:
                    count += 1
        
        return count
    
# =============================================================================
# counts the number of vehicle in specified area which coord specified by 
# latitude and longitude    
# =============================================================================
    def vehicle_count_in_area(self,lat,lon,time):


        return


# =============================================================================
#     
# =============================================================================
    def plot_():
        
        return

