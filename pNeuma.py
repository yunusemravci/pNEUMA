# -*- coding: utf-8 -*-
"""
Created on Thu May 14 22:53:54 2020
@author: Yunus
"""
import pandas as pd
import os
import scipy.io as sio
import csv
import matplotlib.pyplot as plt
import seaborn as sns
# =============================================================================
# pNEUMA 
# =============================================================================
#delimiter=';',low_memory=False , index_col = 0
class pNeuma:
    
    path = os.getcwd() + '/pneuma_sample_dataset/'
    
    df=pd.DataFrame()
    splitted = []
    
    def load(self,filename):
        
        headers = pd.read_csv(self.path + filename, nrows=0).columns.tolist()
        word = headers[0]
        #print(word)
        self.splitted = word.split(';')
        #print(self.splitted)
        
#        self.splitted.['unnamed: 10']
        self.df = pd.read_csv(self.path + filename,delimiter=';',index_col = 0,low_memory = False)
        
        #print(list(self.df.columns))

            
# =============================================================================
# saves the dataframe as .mat    
# =============================================================================
    def savetomatlab(self):

        sio.savemat('pneuma_sample_dataset.mat', self.df)
        print("*\tDataframe saved as mat file in working directory")
# =============================================================================
# finds and returns count of vehicle type
# =============================================================================
    def vehicle_type_number(self,vehicle_type):
        
        counter = 0
        track = self.splitted[1]
        #print(track)
        allvehicle_types = self.df[track]
        
        for i in range(len(allvehicle_types)):
            if  " ".join(self.df.iloc[i][0].split()) == " ".join(vehicle_type.split()):
                counter += 1
        #print(counter)
        return counter
# =============================================================================
# returns all data of specified vehicle type e.g. car  
# =============================================================================
    def vehicle_type_data(self,vehicle_type):
        
        select_track = self.df[self.df[self.splitted[1]].str.replace(" ","") == vehicle_type.replace(" ","")]
        
        #print(select_track)
        
        return select_track

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
        
#        lat = lat.sort()
        lon = lon.sort()
        for i in range(len(self.df)):
            if latitudes[i] >= lat and longitudes[i] <= lon[1] and longitudes[i] >= lon[0]:
                count += 1
        
        return count
    
# =============================================================================
# counts the number of vehicle in specified area which coord specified by 
# latitude and longitude    
# =============================================================================
    def vehicle_count_in_area(self,lat,lon,time):
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
            if latitudes[i] >= lat[0] and latitudes[i] <= lat[1] and longitudes[i] <= lon[1] and longitudes[i] >= lon[0]:
                count += 1


        return count
# =============================================================================
# plot column time based  
# =============================================================================
    def plot_(self,column_plot,track_info):
        time = []
        y_axis = []
        #print("---",column_plot)
        if column_plot == "speed":
            y = 6
        elif column_plot == "lat":
            y = 4
        elif column_plot == "lon":
            y = 5
        elif column_plot == "lat_accel":
            y = 8
        elif column_plot == "tan_accel":
            y = 7

        time.append(track_info[self.splitted[9]])
        y_axis.append(track_info[self.splitted[y]])
        i = 15
        y = y + 6
        while i  < len(self.splitted):
            if i < len(self.splitted):
                if self.splitted[i] == "":
                    col_name = "Unnamed: " + str(i)
                    y_col_name = "Unnamed: " + str(y)
                    if track_info[col_name] != 'nan':
                        time.append(track_info[col_name])
                        y_axis.append(track_info[y_col_name])
                
            i = i + 6
            y = y + 6
        
        cleaned_time = [x for x in time if x != 'nan']
        cleaned_y_axis = [x for x in y_axis if x != 'nan']
        
        #cleaned_time = list(map(float, cleaned_time))
        cleaned_y_axis = list(map(float, cleaned_y_axis))
        
        sns.set(rc={'figure.figsize':(11, 4)})
        plt.plot(cleaned_time, cleaned_y_axis)
        plt.xlabel('time')
        plt.ylabel(column_plot)
        plt.show()
        return
