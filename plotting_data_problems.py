# Coded by Nathan Satterfield
# 11th grade at Francis W. Parker School

import csv
import matplotlib.pyplot as plt

# MATPLOTLIB PROBLEM # 1
# Chicago Public Library Computer Usage (15pts)
# open and read in the "Libraries_-_2017_Visitors_by_Location.csv" file into a list (use file located in the file folder, read in using csv library).
# calculate (and make a list of) the total visitors to Chicago libraries each month.  
# Do not plot every library individually.  Instead, find the total for all libraries each month and plot that.
# Make a BAR GRAPH with the total visitors on the y and month on the x.  
# label the x with the month.  Rotate the text so we can read it.  (see example problem).  Use the tight_fit command to show all text.
# label axes, title the graph as necessary.

with open("files/Libraries_-_2017_Visitors_by_Location.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)


month_names = data[0][1:-1]
print(month_names)

jan = [x[1] for x in data]
jan.pop(0)
jan = sum([int(x) for x in jan])
print(jan)

feb = [x[2] for x in data]
feb.pop(0)
feb = sum([int(x) for x in feb])
print(feb)

mar = [x[3] for x in data]
mar.pop(0)
mar = sum([int(x) for x in mar])
print(mar)

april = [x[4] for x in data]
april.pop(0)
april = sum([int(x) for x in april])
print(april)

may = [x[5] for x in data]
may.pop(0)
may = sum([int(x) for x in may])
print(may)


june = [x[6] for x in data]
june.pop(0)
june = sum([int(x) for x in june])
print(june)


july = [x[7] for x in data]
july.pop(0)
july = sum([int(x) for x in july])
print(july)


aug = [x[8] for x in data]
aug.pop(0)
aug = sum([int(x) for x in aug])
print(aug)


sept = [x[9] for x in data]
sept.pop(0)
sept = sum([int(x) for x in sept])
print(sept)


oct = [x[10] for x in data]
oct.pop(0)
oct = sum([int(x) for x in oct])
print(oct)


nov = [x[11] for x in data]
nov.pop(0)
nov = sum([int(x) for x in nov])
print(nov)


dec = [x[12] for x in data]
dec.pop(0)
dec = sum([int(x) for x in dec])
print(dec)

month_numbers = [x for x in range(12)]
print(month_numbers)

visitors = [jan, feb, mar, april, may, june, july, aug, sept, oct, nov, dec]

plt.figure(1, facecolor='lightblue', tight_layout=True)
plt.bar(month_numbers, visitors, color='darkblue')
plt.xticks(month_numbers, month_names, rotation=45)

plt.title("Chicago Library Monthly Usage - 2017")
plt.ylabel("Number of Visitors")

plt.show()


# MATPLOTLIB PROBLEM # 2
# Chicago Public Transit Usership Graph (20pts)
# go to https://data.cityofchicago.org/Transportation/CTA-Ridership-Annual-Boarding-Totals/w8km-9pzd
# download the CTA ridership data as a csv.
# Read the data into a list using the csv library.
# Make a plot of paratransit, bus, rail, and total numbers by year (all on the same graph).
# Make each line, points, and color different for the four graphs.
# Make a legend to identify each line.
# Label axes and give your graph a title.  Change it in any other way you see necessary to give it a clean look.

