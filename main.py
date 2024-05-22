from selenium import webdriver
import time
from dotenv import load_dotenv
import os
from utils.cookies import load_cookies  # Import the utility function

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
