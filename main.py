from selenium import webdriver
import time
import json
from dotenv import load_dotenv
import os

def load_cookies(driver, cookies_file):
    with open(cookies_file, 'r') as file:
        cookies = json.load(file)
        for cookie in cookies:
            # Ensure all required fields are present and valid
            if 'sameSite' not in cookie or cookie['sameSite'] not in ['Strict', 'Lax', 'None']:
                cookie['sameSite'] = 'None'
            if 'expiry' in cookie:
                cookie['expiry'] = int(cookie['expiry'])  # Ensure expiry is an integer
            driver.add_cookie(cookie)

def main():
    # Load environment variables from .env file
    load_dotenv()
    url = os.getenv('URL')
    cookies_file = os.getenv('COOKIES_FILE')

    # Set up the Edge web driver (ensure you have EdgeDriver installed and in your PATH)
    driver = webdriver.Edge()

    try:
        # Open the specified URL
        driver.get(url)

        # Load cookies
        load_cookies(driver, cookies_file)

        # Refresh the page to apply cookies
        driver.refresh()

        # Wait for some time to observe the result (optional)
        time.sleep(10)

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
