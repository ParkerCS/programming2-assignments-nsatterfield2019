# Coded by Nathan Satterfield
# 11th grade at Francis W. Parker School

# In 2013, an interesting dataset was released for Chicago which identified a number of food deserts.
# In many areas of the city, there were no suitable grocery stores with adequate produce, meats, refrigerated, and frozen food sections
# Many areas were only served by corner stores and convenience stores.

# Using gmplot and the chicago grocery csv, which contains updated grocery store data, 
# create a map with the following characteristics.
# - Map is centered on Chicago at a zoom level that shows all stores (5pts)
# - All adequate grocery stores are plotted (could be scatterplot, circles, or markers) (use the one looks best to you) (10pts)
#   Inadequate grocery stores are NOT plotted (you decide what inadequate means)
# - Shows a heatmap which helps to visualize the greatest concentration of adequate stores. (10pts) 
#   Your heatmap should be optimized for the city level view.  Tweak the radius and maxIntensity to adjust blob.


# Challenges:  
# Instead of a heatmap, make each store a circle with varying size based on square footage of the store.  
# Filter out all liquor stores, drug stores, and convenience stores.
# Place markers or other indicators where you still see inadequate food access.
from gmplot import *
import csv

apikey = "AIzaSyD65be4pywe7-y4GjMmzZMidOpdmu2lkXo"


mymap = GoogleMapPlotter(41.878100, -87.629800, 11, apikey=apikey)

with open("files/Grocery_Stores_-_2013.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    data_length = list(reader)

data.pop(0)

index = 0
while index < len(data):
    if "LIQUOR" in data[index][0] or "WALGREEN" in data[index][0] or "Liquor" in data[index][0]:
        del data[index]
    index += 1

print(data)

lats = [float(x[-3]) for x in data]
longs = [float(x[-2]) for x in data]

#mymap.scatter(lats, longs, color="green", marker=True, size=1, opacity=1)
mymap.heatmap(lats, longs, maxIntensity=5, radius=25, dissipating=True)







mymap.draw("grocerymap.html")