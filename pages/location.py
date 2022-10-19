from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from pages.locators import LocationLocators
import time

class Location(BasePage):
    def search_input(self, name, lat, lon):
        print("trying to find " + name)
        self.browser.find_element(*LocationLocators.SEARCH_INPUT).send_keys(name)
        self.browser.find_element(*LocationLocators.SEARCH_BUTTON).click()
        coords = self.browser.find_element(*LocationLocators.COORDS_RESULT).get_attribute("innerHTML")
        point = self.browser.find_element(*LocationLocators.FOUNDED_POINT).text
        assert name in self.browser.find_element(*LocationLocators.FIRST_SEARCH_RESULT).text, "expected " + name + ", but founded " + point 
        assert lat + "," + lon == coords, "expected coords " + lat + "," + lon + ", but received " + coords 
        print("founded " + point + " by coords " + coords )


        time.sleep(2) 

    def input_lan_and_lon(self, name, zoom, lat, lon): 
        print("trying to find smth by coords " + lat + "," + lon)
        self.browser.find_element(*LocationLocators.REVERSE_PAGE).click()
        time.sleep(4)
        latitude = self.browser.find_element(*LocationLocators.LAT)
        latitude.clear()
        latitude.send_keys(lat)
        longitude = self.browser.find_element(*LocationLocators.LON)
        longitude.clear()
        longitude.send_keys(lon)
        select = Select(self.browser.find_element(*LocationLocators.ZOOM))
        select.select_by_value(zoom) 
        self.browser.find_element(*LocationLocators.REVERSE_SEARCH_BUTTON).click()
        time.sleep(2)
        result = self.browser.find_element(*LocationLocators.FIRST_SEARCH_RESULT).text
        assert name in result, "expected " + name + ", but received " + result
        print("founded " + result)

