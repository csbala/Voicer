from selenium.webdriver.common.by import By

class ChatPage:
    def __init__(self, driver):
        self.driver = driver
        self.chatbox_locator = (By.ID, 'chatbox')  # Adjust the locator
        self.send_button_locator = (By.ID, 'send_button')  # Adjust the locator

    def open_chat(self, url):
        self.driver.get(url)

    def send_message(self, message):
        chatbox = self.driver.find_element(*self.chatbox_locator)
        send_button = self.driver.find_element(*self.send_button_locator)
        chatbox.clear()
        chatbox.send_keys(message)
        send_button.click()

    def wait_for_response(self):
        # Implement logic to wait for the chat response
        pass
