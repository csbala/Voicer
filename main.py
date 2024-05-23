from selenium import webdriver
import time
from utils.speech_recognition import recognize_speech_from_mic  # Import the speech recognition function
from pages.chat_page import ChatPage  # Import the ChatPage class
from factory.browser_factory import BrowserFactory  # Import the BrowserFactory class

def main():
    try:
        # Initialize the browser using the factory
        browser_factory = BrowserFactory()
        driver = browser_factory.create_driver()

        # Open the chat page
        chat_page = ChatPage(driver)

        # Wait for some time to observe the result (optional)
        time.sleep(5)

        # Recognize speech and convert to text
        while True:
            print("Please speak into the microphone...")
            text = recognize_speech_from_mic()
            if text.lower() == "exit":
                print("Exiting...")
                break
            print(f"You said: {text}")

            # Send the message using the ChatPage class
            chat_page.send_message(text)

            # Wait for a short period before next input
            time.sleep(5)

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
