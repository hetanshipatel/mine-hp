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
pylt.figure(figsize=(8,8))
pylt.plot(mname,Mbud, label ='Budget')
pylt.plot(mname, Musa, label = 'Gross USA')
pylt.plot(mname, Mww, label = 'Gross Worldwide')
pylt.legend()
pylt.xticks(rotation=80)
pylt.xlabel('Movie Name')
pylt.ylabel('values in billion')
pylt.show()

#To plot pie chart
car = pds.read_csv("car_data.csv")
hpower = car["horsepower"]
cname = car["car name"]
pylt.figure()
pylt.pie(hpower, labels=cname, autopct='%1.1f%%')
pylt.title("Horsepower of cars")
pylt.show()

#To plot histogram
stp= pds.read_csv("StudentsPerformance.csv")
pylt.figure(1)
pylt.hist(stp["reading score"],density=True,  label="reading score")
pylt.hist(stp["writing score"], density=True, alpha=0.7, label="writing score")
pylt.legend()
pylt.xlabel('Score')
pylt.ylabel('Frequency')
pylt.show()

