from pages.base_page import BasePage
from pages.location import Location
import pytest
import time



search_list = [
        # it is possible to add some points with format:
        # [<point name>, <max zoom (4 - for country, 10 - for city, 16 - for street>, <latitude>, <longitude>]

        ["Russia","4","64.6863136","97.7453061"],
        ["Canada","4","61.0666922","-107.991707"],
        ["Pretoria","10","-25.7459277","28.1879101"],
        ["Beijing","10","39.906217","116.3912757"],
        ["Hagegata","16","59.9148058","10.7739557"],
        ["Staffordshire Moorlands","10","35.1234567","45.1234567"] #wrong point

        ]

@pytest.mark.parametrize('point',search_list)
def test_find_coords_by_adress(browser,point): 
        name = point[0]
        lat = point[2]
        lon = point[3]
        link = "https://nominatim.openstreetmap.org/ui/search.html"
        page = BasePage(browser, link)
        page.open()
        time.sleep(2)
        location = Location(browser, browser.current_url)
        location.search_input(name, lat, lon)


@pytest.mark.parametrize('point',search_list)
def test_find_adress_by_coords(browser,point):
        name = point[0]
        zoom = point[1]
        lat = point[2]
        lon = point[3]
        link = "https://nominatim.openstreetmap.org/ui/search.html"
        page = BasePage(browser, link)
        page.open()
        time.sleep(2)
        location = Location(browser, browser.current_url)
        location.input_lan_and_lon(name, zoom, lat, lon)
