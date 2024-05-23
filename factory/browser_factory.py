from selenium import webdriver
import os
from dotenv import load_dotenv
from utils.cookies import load_cookies

class BrowserFactory:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()
        self.url = os.getenv('URL')
        self.cookies_file = os.getenv('COOKIES_FILE')

        # Debugging: Print the environment variables
        print(f"URL: {self.url}")
        print(f"COOKIES_FILE: {self.cookies_file}")

        if not self.url or not self.cookies_file:
            raise ValueError("Environment variables URL or COOKIES_FILE are not set correctly.")

        # Ensure the cookies file exists
        if not os.path.exists(self.cookies_file):
            raise FileNotFoundError(f"Cookies file does not exist: {self.cookies_file}")

    def create_driver(self):
        # Set up the Edge web driver (ensure you have EdgeDriver installed and in your PATH)
        driver = webdriver.Edge()

        # Open the specified URL
        driver.get(self.url)

        # Load cookies
        load_cookies(driver, self.cookies_file)

        # Refresh the page to apply cookies
        driver.refresh()

        return driver
