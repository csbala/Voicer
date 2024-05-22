import json

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
