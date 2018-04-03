# Coded by Nathan Satterfield
# 11th grade at Francis W. Parker School

'''
Energy Efficiency of Chicago Schools (35pts)

https://data.cityofchicago.org/Environment-Sustainable-Development/Chicago-Energy-Benchmarking-2016-Data-Reported-in-/fpwt-snya\

Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
The dataset at the link above is that data from 2016 which was reported in 2017.

We will use this data to look at schools.  We will visualize the efficiency of schools by scatter plot.  
We expect that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
An efficient school would have a large ratio of sqft to ghg.  
It would also be interesting to know where Parker lies on this graph???  Let's find out.

Make a scatterplot which does the following:  
- Plots the Total Greenhouse gas (GHG) Emmissions (y-axis), versus building square footage (x-axis) (13pts)
- Includes ONLY data for K-12 Schools. (3pts)
- Labelled x and y axis and appropriate title (3pt)
- Annotated labels (school name) for the 5 highest and 5 lowest GHG Intensities. (3pts)
- Label Francis W. Parker. (3pts)
- Create a best fit line for schools shown. (5pts)
- Customize your graph in a discernable way using any technique discussed or one from the API (matplotlib.org). (5pts)


Challenge (for fun):
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intesity show in red.
- Add colleges and universities (use a different marker type)

'''

import csv
import matplotlib.pyplot as plt
import numpy as np

with open("files/Chicago_Energy_Benchmarking_-_2016_Data_Reported_in_2017.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

school_names = []
square_footage = []
greenhouse_gas = []

plotting_code = "K-12 School"

for i in range(len(data)):
    if data[i][6] == plotting_code:
        try:
            name = data[i][2]
            sqr_ft = float(data[i][7])
            gg = float(data[i][20])
            school_names.append(name)
            square_footage.append(sqr_ft)
            greenhouse_gas.append(gg)
        except:
            print(data[i][0], "has no data")

    else:
        continue


print(school_names)
print(square_footage)
print(greenhouse_gas)

plt.figure(1, figsize=(12,7))
plt.scatter(square_footage, greenhouse_gas, s=5, c='red')
plt.title("Energy Efficiency (or lack) of Chicago Schools")
plt.xlabel("Square Footage of Building")
plt.ylabel("Greenhouse Gas Emissions")

m, b = np.polyfit(square_footage, greenhouse_gas, 1) # 1 for linear, returns slipe and y intercept

x = [0, 700000]
y = [m * point + b for point in x]

plt.plot(x, y, color='green')

ghg_int = []
ghg_int = square_footage / greenhouse_gas

for i in range(len(square_footage)):
    ghg_int = square_footage[i] / greenhouse_gas[i]

#x for x in len(list) --> Above

zipped = zip(school_names, square_footage, greenhouse_gas)
zipped = list(zipped)
print(zipped)

zipped.sort(key= lambda x:x[2])
print(zipped)


for i in range(len(zipped)):
    if i < 5:
        plt.annotate(zipped[i][0], xy=(zipped[i][1], zipped[i][2]), fontsize=5)
    if i > len(zipped) - 6:
        plt.annotate(zipped[i][0], xy=(zipped[i][1], zipped[i][2]), fontsize=5)

plt.show()




