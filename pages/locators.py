from selenium.webdriver.common.by import By


class LocationLocators():
    SEARCH_INPUT = (By.XPATH, "/html/body/section[2]/div/div[1]/form/div/div[1]/input")
    SEARCH_BUTTON = (By.XPATH, "/html/body/section[2]/div/div[1]/form/div/div[2]/button")
    FIRST_SEARCH_RESULT = (By.XPATH, "/html/body/div[2]/div[1]/div/div[1]/span[1]")
    COORDS_RESULT = (By.XPATH, "/html/body/div[2]/div[1]/div/div[1]/p")
    FOUNDED_POINT = (By.XPATH, "/html/body/div[2]/div[1]/div/div[1]/span[1]")
    REVERSE_PAGE = (By.XPATH, "/html/body/header/nav/div/div[2]/ul/li[2]/a")
    LAT = (By.XPATH, "/html/body/section[2]/form/div/div[2]/input")
    LON = (By.XPATH, "/html/body/section[2]/form/div/div[5]/input")
    ZOOM = (By.XPATH, "/html/body/section[2]/form/div/div[7]/select")
    REVERSE_SEARCH_BUTTON = (By.XPATH, "/html/body/section[2]/form/div/div[8]/button")
