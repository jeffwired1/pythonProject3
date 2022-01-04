import requests
from bs4 import BeautifulSoup
# page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
page = requests.get("https://www.wunderground.com/dashboard/pws/KCALAGUN69/table/2021-12-31/2021-12-31/daily")
print(page)
print(page.status_code)

# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
a = str(soup)

# print(a)

# print(soup.prettify())

# Find current temperature
b = a.find("test-true wu-unit wu-unit-temperature is-degree-visible ng-star-inserted")
c = a.find("wu-value wu-value-to", b)
d = a.find(">", c)
e = a.find("<", d)
g = a[d+1:e]
current_temperature = g

# Find current pressure
b = a.find("test-false wu-unit wu-unit-pressure ng-star-inserted")
c = a.find("wu-value wu-value-to", b)
d = a.find(">", c)
e = a.find("<", d)
g = a[d+1:e]
current_pressure = g

# Find current humidity
b = a.find("test-false wu-unit wu-unit-humidity ng-star-inserted")
c = a.find("wu-value wu-value-to", b)
d = a.find(">", c)
e = a.find("<", d)
g = a[d+1:e]
current_humidity = g

# Find current wind speed
b = a.find("test-false wu-unit ng-star-inserted")
c = a.find("wu-value wu-value-to", b)
d = a.find(">", c)
e = a.find("<", d)
g = a[d+1:e]
current_wind_speed = g

# Find current wind gust
b = a.find(">GUST<")
c = a.find("wu-value wu-value-to", b)
d = a.find(">", c)
e = a.find("<", d)
g = a[d+1:e]
current_wind_gust = g

# Find current total precipitation
b = a.find(">PRECIP ACCUM<")
c = a.find("wu-value wu-value-to", b)
d = a.find(">", c)
e = a.find("<", d)
g = a[d+1:e]
current_total_precipitation = g

# Find current total precipitation rate
b = a.find(">PRECIP RATE<")
c = a.find("wu-value wu-value-to", b)
d = a.find(">", c)
e = a.find("<", d)
g = a[d+1:e]
current_total_precipitation_rate = g

# Find current dewpoint
b = a.find(">DEWPOINT<")
c = a.find("wu-value wu-value-to", b)
d = a.find(">", c)
e = a.find("<", d)
g = a[d+1:e]
current_dewpoint = g
print(b, c, d, e, g)

print('Current Temperature', current_temperature, 'F')
print('Current Dewpoint', current_dewpoint, 'F')
print('Current Pressure', current_pressure, 'in/hg')
print('Current Humidity', current_humidity, '%')
print('Current Wind Speed', current_wind_speed, 'MPH')
print('Current Wind Gust', current_wind_gust, 'MPH')
print('Current Total Precipitation', current_total_precipitation, 'in')
print('Current Total Precipitation Rate', current_total_precipitation_rate, 'in/hr')






