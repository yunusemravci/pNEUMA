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
    
    path = os.getcwd() + '/pneuma_sample_dataset/pneuma_sample_dataset.csv'
    
    
    def load(self):
        df=pd.read_csv(self.path, header = None)
        #df = pd.read_csv(self.path)
        print(df.shape)
        print(df.columns.tolist())
        return df
# =============================================================================
# saves the dataframe into matlab    
# =============================================================================
    def savetomatlab(self,df):
#        truncDataFrame.rename(columns=lambda x:'col_' + x.replace(' ', '_'), inplace=True)  
#        scipy.io.savemat('EEGdata2.mat', {'struct2':truncDataFrame.to_dict("list")})
        sio.savemat('pneuma_sample_dataset.mat', df)
        
# =============================================================================
# finds and returns count of vehicle type
# =============================================================================
    def vehicle_type_number(self):
        
        
        return 
# =============================================================================
#  returns all data of specified vehicle type e.g. car   
# =============================================================================
    def vehicle_type_data(self,vehicle_type):
        
        return

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

print(dff.take([1],axis=1).head())


