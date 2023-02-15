from selenium import webdriver

# add options to chromedriver
options = webdriver.ChromeOptions()
# tell chromedriver to work in the background
options.add_argument("headless")
# define chromedriver
driver = webdriver.Chrome(executable_path="C:/windows/chromedriver.exe", chrome_options=options)


def get_current_readings():
    driver.implicitly_wait(0.5)
    driver.get("https://tempestwx.com/station/84479/")
    # access HTML source code with page_source method
    a = driver.page_source

    # text_file = open("sample.txt", "w")
    # text_file.write(a)
    # text_file.close()

    # print(a)

    # Find current temperature
    b = a.find("forecast-view")
    c = a.find("air_temperature", b)
    d = a.find(">", c)
    e = a.find("<", d)
    g = a[d+1:e]
    current_temperature = g
    current_temperature_out = "Temperature " + g + " F"

    # Find current feels-like temperature
    b = a.find("forecast-view")
    c = a.find("cc-feels-like-temp", b)
    d = a.find(">", c)
    e = a.find("<", d)
    g = a[d+1:e-1]
    current_feels_like_temperature = g
    current_feels_like_temperature_out = "Feels Like Temperature " + g + " F"

    # Find current pressure
    b = a.find("forecast-view")
    c = a.find("sea_level_pressure", b)
    d = a.find(">", c)
    e = a.find("<", d)
    g = a[d+1:e]
    current_pressure = g
    current_pressure_out = "Pressure " + g + " in/hg"

    # Find current humidity
    b = a.find("forecast-view")
    c = a.find("relative_humidity", b)
    d = a.find(">", c)
    e = a.find("%", d)
    g = a[d+1:e]
    current_humidity = g
    current_humidity_out = "Humidity " + g + " %"

    # Find current wind speed
    b = a.find("forecast-view")
    c = a.find("wind_avg", b)
    d = a.find(">", c)
    e = a.find("<", d)
    g = a[d+1:e]
    current_wind_speed = g
    current_wind_speed_out = "Wind Speed " + g + " MPH"

    # Find current wind gust
    b = a.find("list-summary-view")
    c = a.find("wind_gust", b)
    d = a.find(">", c)
    e = a.find(" ", d)
    g = a[d+1:e]
    current_wind_gust = g
    current_wind_gust_out = "Wind Gust " + g + " MPH"

    # Find current total precipitation
    b = a.find("history-view-target")
    c = a.find("Total - in", b)
    c = a.find("value", c)
    d = a.find(">", c)
    e = a.find("<", d)
    g = a[d+1:e]
    current_total_precipitation = g
    current_total_precipitation_out = "Total Precipitation " + g + " in"

    # Find current total precipitation rate
    b = a.find("list-summary-view")
    c = a.find("Rain Intensity", b)
    c = a.find("precip", c)
    d = a.find("(", c)
    e = a.find(" ", d)
    g = a[d+1:e]
    current_total_precipitation_rate = g
    current_total_precipitation_rate_out = "Precipitation Rate " + g + " in/hr"

    # Find current dewpoint
    b = a.find("list-summary-view")
    c = a.find("dew_point", b)
    d = a.find(">", c)
    e = a.find(" ", d)
    g = a[d+1:e]
    current_dewpoint = g
    current_dewpoint_out = "Dewpoint " + g + "F"

    # Find current wind direction
    b = a.find("forecast-view")
    c = a.find("wind_direction", b)
    d = a.find(">", c)
    e = a.find("<", d)
    g = a[d+1:e]
    current_wind_direction = g
    current_wind_direction_out = "Wind Direction " + g

    # Find current solar radiation
    b = a.find("list-summary-view")
    c = a.find("Solar Radiation", b)
    c = a.find("solar_radiation", c)
    d = a.find(">", c)
    e = a.find(" ", d)
    g = a[d+1:e]
    current_solar_radiation = g
    current_solar_radiation_out = "Solar Radiation " + g + " w/m²"

    print(current_temperature_out)
    print(current_feels_like_temperature_out)
    print(current_dewpoint_out)
    print(current_pressure_out)
    print(current_humidity_out)
    print(current_wind_speed_out)
    print(current_wind_gust_out)
    print(current_wind_direction_out)
    print(current_total_precipitation_out)
    print(current_total_precipitation_rate_out)
    print(current_solar_radiation_out)

    return


