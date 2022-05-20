from selenium.webdriver.common.by import By
from Locators.locators import locators

# wrapper class
class wrapper():
    def __init__(self, driver):
        self.driver = driver
        self.emailid_text_id = locators.emailid_text_id
        self.continue_button_id = locators.continue_button_id
        self.passwrd_text_id = locators.passwrd_text_id
        self.signin_button_id = locators.signin_button_id

    def enter_emailid(self,email):
        self.driver.find_element(by=By.ID, value=self.emailid_text_id).send_keys(email)

    def continue_button_click(self):
        self.driver.find_element(by=By.ID, value=self.continue_button_id).click()

    def enter_passwrd(self,pswd):
        self.driver.find_element(by=By.ID, value=self.passwrd_text_id).send_keys(pswd)

    def signin_button_click(self):
        self.driver.find_element(by=By.ID, value=self.signin_button_id).click()
