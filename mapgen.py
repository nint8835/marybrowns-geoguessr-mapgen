import json

from selenium import webdriver

# TODO: Make this not safari
driver = webdriver.Safari()

driver.get("https://marybrowns.com/locations/")

locations = driver.execute_script("return _locations")

with open("locations.json", "w") as f:
    json.dump(locations, f, indent=4, sort_keys=True)
