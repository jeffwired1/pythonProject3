import requests
from bs4 import BeautifulSoup
# page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
page = requests.get("https://www.wunderground.com/dashboard/pws/KCALAGUN69/table/2021-12-31/2021-12-31/daily")
print(page)
print(page.status_code)

# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

a = soup.prettify()
print(a.find("test-false wu-unit wu-unit-pressure ng-star-inserted"))

