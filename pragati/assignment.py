# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:12:15 2022

@author: hk22abk
"""

#import numpy as npy
import pandas as pds
import matplotlib.pyplot as pylt #mathematics function


# To read csv file
movie = pds.read_csv("movies_marvel_dc.csv", encoding = 'latin1')

# To assign variable
mname = movie["Original Title"]
Mbud = movie["Budget"]
Musa = movie["Gross USA"]
Mww = movie["Gross Worldwide"]


# to plot line graph 
pylt.figure(figsize=(10,10))
pylt.plot(mname,Mbud, label ='Budget')
pylt.plot(mname, Musa, label = 'Gross USA')
pylt.plot(mname, Mww, label = 'Gross Worldwide')
pylt.legend()
pylt.xlabel('Movie Name')
pylt.ylabel('values in billion')
pylt.show()

mscore = movie["Gross Worldwide"]
Movies = movie["Original Title"]
pylt.figure()
pylt.pie(mscore, labels=Movies, autopct='%1.1f%%')
pylt.title("Gross Worldwide percentage")
pylt.show()

car = pds.read_csv("car_data.csv")
for i in range(4):
    pylt.figure(1)
    # IMPORTANT range and bins setting need to be identical
    pylt.hist(car["mpg"],density=True,  label= car['car name'])
    pylt.hist(car["mpg"],density=True,  label= car['car name'])
    pylt.legend()
    pylt.show()

