# Coded by Nathan Satterfield
# 11th grade at Francis W. Parker School

from bs4 import BeautifulSoup
import requests


# PROBLEM 1 (12pts)
# Go to your favorite follow on Twitter.  (not someone who posts explicit materials please)
# Inspect the twitter feed in Chrome.
# You'll notice that the tweets are stored in a ordered list <ol></ol>, and individual tweets are contained as list items <li></li>.
# Use BeautifulSoup and requests to grab the text contents of last 5 tweets located on the twitter page you chose.
# Print the tweets in a nicely formatted way.
# Have fun.  Again, nothing explicit.

url = 'https://twitter.com/LiveFTC'
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")
#print(soup.prettify())

tweet = soup.findAll("p", class_="tweet-text")
tweet = [x.text.strip() for x in tweet]
print(tweet)

for i in range(len(tweet)):
    print(tweet[i])
    print("\n")

# (20pts)
# Below is a link to a 10-day weather forecast at weather.com
# Use urllib and BeautifulSoup to scrape data from the weather table.
# Print a synopsis of the weather for the next 10 days.
# Include the day and date, description, high and low temp, chance of rain, and wind. (2pts each)
# Print the weather for each of the next 10 days to the user in a readable sentences.
# You can customize the text as you like, but it should be readable as a sentence without errors. (10pts)
# You will need to target specific classes or other attributes to pull some parts of the data.
# Sample sentence:  
# Wednesday, April 4 will be Partly Cloudy/Windy with a High of 37 degrees and a low of 25, humidity at 52%.  There is 0% chance of rain with winds out of the WNW at 22 mph.

url = "https://weather.com/weather/tenday/l/Chicago+IL+USIL0225:1:US"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")
#print(soup.prettify())

day_date = soup.findAll("td", class_="twc-sticky-col", headers="day")
day_date = [x.text.strip() for x in day_date]
#print(day_date)
day_date_new = [x.replace("\n", "") for x in day_date]
#print(day_date_new)




for j in range(len(day_date_new)):
    new_new_day_date = ""
    flag = False
    for i in range(len(day_date_new[j])):
        if day_date_new[j][i] == day_date_new[j][i].upper() and i > 0 and not flag:
            new_new_day_date += " "
            new_new_day_date += day_date_new[j][i]
            flag = True

        else:
            new_new_day_date += day_date_new[j][i]
    day_date_new[j] = new_new_day_date

print(day_date_new)


description = soup.findAll("td", class_="description")
description = [x.text.strip() for x in description]
print(description)

high_low = soup.findAll("td", class_="temp", headers="hi-lo")
high_low = [x.text.strip() for x in high_low]
print(high_low)

precip = soup.findAll("td", class_="precip", headers="precip")
precip = [x.text.strip() for x in precip]
print(precip)

wind = soup.findAll("td", class_="wind", headers="wind")
wind = [x.text.strip() for x in wind]
print(wind)

humid = soup.findAll("td", class_="humidity", headers="humidity")
humid = [x.text.strip() for x in humid]
print(humid)

zipped = zip(day_date_new, description, high_low, precip, wind, humid)
zipped = list(zipped)
print(zipped)

for item in zipped:
    print("{:<11}: Description: {:<17} High/Low: {:<7} Precipitation: {:<4} Wind: {:<10} Humidity: {:<3}".format(item[0], item[1], item[2], item[3], item[4], item[5]))

