import csv
import json

from selenium import webdriver

# TODO: Make this not safari
driver = webdriver.Safari()

driver.get("https://marybrowns.com/locations/")

locations = driver.execute_script("return _locations")

with open("locations.csv", "w") as f:
    writer = csv.writer(f)

    for location in locations:
        writer.writerow([location["lat"], location["lng"]])
