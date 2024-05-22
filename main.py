from selenium import webdriver
from pages.chat_page import ChatPage
from utils.voice_recognition import VoiceRecognition
import time

def main():
    driver = webdriver.Chrome()
    chat_page = ChatPage(driver)
    voice_recognition = VoiceRecognition()

    # Open the chat page
    chat_url = 'https://example.com/chat'  # Replace with the actual chat URL
    chat_page.open_chat(chat_url)

    try:
        while True:
            # Listen for a voice command
            command = voice_recognition.listen()
            if command:
                # Send the command as a message in the chat
                chat_page.send_message(command)

                # Wait for the response (implement the waiting logic)
                chat_page.wait_for_response()
                time.sleep(5)  # Adjust based on the response time
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
