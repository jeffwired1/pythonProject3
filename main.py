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



print(b, c, d, e, g)

print(current_temperature, current_pressure, current_humidity, current_wind_speed, current_wind_gust)



