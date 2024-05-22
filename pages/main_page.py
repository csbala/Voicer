from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.opening_pop_up_x = (By.CSS_SELECTOR, "button.")
        pass