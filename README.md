# Voicer

## Overview

This project uses Selenium to automate interactions with Character AI, including maintaining a logged-in session using cookies. The script opens the Character AI website, loads cookies from a JSON file, and interacts with the site while bypassing the login step.

## Requirements

- Python 3.x
- Selenium
- Edge WebDriver
- `python-dotenv` for environment variable management

## Setup

### 1. Install Dependencies

Install the necessary Python packages:

```bash
pip install selenium python-dotenv
```

### 2. Install Edge WebDriver

Download and install the Edge WebDriver from the [Microsoft Edge Driver download page](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).

Ensure the Edge WebDriver is in your system's PATH.

### 3. Set Up Environment Variables

Create a `.env` file in the root directory of your project with the following content:

```env
URL=https://www.character.ai  # Replace with the actual URL of the Character AI site
COOKIES_FILE=cookies.json  # Path to your cookies file
```

### 4. Save Cookies

1. Open a browser, manually log in to your Character AI account.
2. Use a browser extension like "EditThisCookie" to export cookies to a `cookies.json` file.
3. Place the `cookies.json` file in the root directory of your project.

### How Often to Update `cookies.json`

The frequency with which you need to update your `cookies.json` file depends on several factors:

1. **Check the Expiry Date of Cookies**:

   - Inspect your `cookies.json` file to see the expiry dates of your cookies.
   - Plan to update the cookies before they expire.

2. **Session Cookies**:

   - If Character AI uses session cookies, you will need to update `cookies.json` every time you start a new browser session.

3. **Website Security Measures**:

   - Some websites have security measures that invalidate cookies after a certain period or due to changes in the client's IP address or user-agent string.
   - In such cases, you may need to update your cookies more frequently.

4. **Login Activity**:
   - Regularly check your login activity. If you notice that your session is frequently being logged out or invalidated, you may need to update your cookies more often.

### Practical Tips for Updating Cookies

1. **Automatic Check**:

   - Implement a check in your script to detect when the cookies are no longer valid and prompt you to update them.

2. **Manual Update**:

   - Log in manually to Character AI, export the cookies using a browser extension like "EditThisCookie", and replace the `cookies.json` file in your project.

3. **Scripted Update** (Advanced):
   - Create a separate script to automate the process of logging in and updating the `cookies.json` file.

## License

This project is licensed under the MIT License.

```

This `README.md` file provides a comprehensive guide on setting up and maintaining the project, including how to manage cookies for the Character AI site.
```
