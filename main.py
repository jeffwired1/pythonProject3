import requests
from bs4 import BeautifulSoup
# page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
page = requests.get("https://www.wunderground.com/dashboard/pws/KCALAGUN69/table/2021-12-31/2021-12-31/daily")
print(page)
print(page.status_code)

# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
a = str(soup)

print(soup)

# print(soup.prettify())

# Find current temperature
b = a.find("TEMPERATURE")
c = a.find("color", b)
d = a.find(">", c)
e = a.find("<", d)
g = a[d+2:e-2]
current_temperature = g
print(b, c, d, e, g)

# Find current pressure
b = a.find("test-false wu-unit wu-unit-pressure ng-star-inserted")
c = a.find("wu-value wu-value-to", b)
d = a.find(">", c)
e = a.find("<", d)
g = a[d+1:e]
current_pressure = g

print(current_temperature, current_pressure)










# wu-value.wu-value-to

