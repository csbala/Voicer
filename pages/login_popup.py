from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPopup:
    def __init__(self, driver):
        self.driver = driver
        self.continue_with_google_button = (By.CSS_SELECTOR, '.w-72 > .z-0:first-child')
        self.popup_id = (By.ID, 'radix-:r5:')  # The ID of the login popup

    def click_continue_with_google(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_with_google_button)
        ).click()

    def wait_until_popup_closed(self):
        WebDriverWait(self.driver, 30).until(
            EC.invisibility_of_element_located(self.popup_id)
        )
