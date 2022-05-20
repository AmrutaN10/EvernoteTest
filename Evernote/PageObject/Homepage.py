from selenium.webdriver.common.by import By
from Locators.locators import locators

# Homepage class
class homepage():
    def __init__(self, driver):
        self.driver = driver
        #Test is for already registered user
        self.reglogin_rx = locators.reglogin_rx
        self.mainlogin_rx = locators.mainlogin_rx

    def reglogin_click(self):
         self.driver.find_element(by=By.XPATH, value=self.reglogin_rx).click()

    def mainlogin_click(self):
         self.driver.find_element(by=By.XPATH, value=self.mainlogin_rx).click()

