from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from Locators.locators import locators
# note page class
class Notes():
    def __init__(self, driver):
        self.driver = driver
        self.NotesTitle = locators.NotesTitle
        self.NotesBody = locators.NotesBody
        self.creatednote_rx = locators.creatednote_rx

    def edit_NotesTitle(self, title):
        self.driver.find_element(by=By.XPATH, value=self.NotesTitle).send_keys(title)

    def edit_NotesBody(self, body):
        self.driver.find_element(by=By.ID, value=self.NotesBody).send_keys(body)

    def creatednote_click(self):
        self.driver.find_element(by=By.XPATH, value=self.creatednote_rx).click()

