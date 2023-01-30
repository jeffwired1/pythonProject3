from selenium import webdriver
# driver = webdriver.Chrome(executable_path="C:\windows\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(executable_path="C:/windows/chromedriver.exe", chrome_options=options)

driver.implicitly_wait(0.5)
driver.get("https://tempestwx.com/station/84479/")
# access HTML source code with page_source method
a = driver.page_source
# print(s)

# Find current temperature
b = a.find("list-summary-view")
c = a.find("air_temperature", b)
d = a.find(">", c)
e = a.find("<", d)
g = a[d+1:e]
current_temperature = g

# Find current pressure
b = a.find("list-summary-view")
c = a.find("barometric_pressure", b)
d = a.find(">", c)
e = a.find(" ", d)
g = a[d+1:e]
current_pressure = g

# Find current humidity
b = a.find("list-summary-view")
c = a.find("relative_humidity", b)
d = a.find(">", c)
e = a.find("%", d)
g = a[d+1:e]
current_humidity = g

# Find current wind speed
b = a.find("list-summary-view")
c = a.find("wind_avg", b)
d = a.find(">", c)
e = a.find("<", d)
g = a[d+1:e]
current_wind_speed = g

# Find current wind gust
b = a.find("list-summary-view")
c = a.find("wind_gust", b)
d = a.find(">", c)
e = a.find(" ", d)
g = a[d+1:e]
current_wind_gust = g

# Find current total precipitation
b = a.find("history-view-target")
c = a.find("Total - in", b)
c = a.find("value", c)
d = a.find(">", c)
e = a.find("<", d)
g = a[d+1:e]
current_total_precipitation = g

# Find current total precipitation rate
b = a.find("list-summary-view")
c = a.find("Rain Intensity", b)
c = a.find("precip", c)
d = a.find("(", c)
e = a.find(" ", d)
g = a[d+1:e]
current_total_precipitation_rate = g

# Find current dewpoint
b = a.find("list-summary-view")
c = a.find("dew_point", b)
d = a.find(">", c)
e = a.find(" ", d)
g = a[d+1:e]
current_dewpoint = g

# Find current wind direction
b = a.find("list-summary-view")
c = a.find("wind_direction", b)
d = a.find(">", c)
e = a.find("<", d)
g = a[d+1:e]
current_wind_direction = g

# Find current solar radiation
b = a.find("list-summary-view")
c = a.find("Solar Radiation", b)
c = a.find("solar_radiation", c)
d = a.find(">", c)
e = a.find(" ", d)
g = a[d+1:e]
current_solar_radiation = g

print('Current Temperature', current_temperature, 'F')
print('Current Dewpoint', current_dewpoint, 'F')
print('Current Pressure', current_pressure, 'in/hg')
print('Current Humidity', current_humidity, '%')
print('Current Wind Speed', current_wind_speed, 'MPH')
print('Current Wind Gust', current_wind_gust, 'MPH')
print('Current Wind Direction', current_wind_direction, '')
print('Current Total Precipitation', current_total_precipitation, 'in')
print('Current Total Precipitation Rate', current_total_precipitation_rate, 'in/hr')
print('Current Solar Radiation', current_solar_radiation, 'w/m²')

exit()


