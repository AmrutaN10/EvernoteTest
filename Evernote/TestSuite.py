import time
from selenium import webdriver
# below commented line can be uncommented for headless execution
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
import unittest
from PageObject.Homepage import homepage
from PageObject.wrapper import wrapper
from PageObject.Dashboard import dashboard
from PageObject.Notes import Notes
import HtmlTestRunner
from testdata import *

class loginfun(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # below commented lines can be uncommented for headless execution
        # cls.options = webdriver.FirefoxOptions()
        # cls.options.headless = True
        # driver = webdriver.Firefox(options=cls.options)

        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(25)
        cls.driver.maximize_window()
        cls.driver.get(evernote_Url)
        # create homepage class object
        cls.Login = homepage(cls.driver)
        # create wrapper class object
        cls.credentials = wrapper(cls.driver)
        # create dashboard class object
        cls.accountpage = dashboard(cls.driver)
        # create Notes class object
        cls.page_notes = Notes(cls.driver)

    # TestCase for already registered user
    def test_01_validLogin(self):
        self.Login = homepage(self.driver)
        self.Login.reglogin_click()
        self.credentials = wrapper(self.driver)
        self.credentials.enter_emailid(valid_email)
        time.sleep(2)
        self.credentials.continue_button_click()
        time.sleep(2)
        self.credentials.enter_passwrd(valid_password)
        self.credentials.signin_button_click()
        time.sleep(15)
        self.accountpage = dashboard(self.driver)
        try:
            text = self.accountpage.hometext()
        except:
            print("test failed")
        if bool(text) == True:
            print("Sucessful login")

        self.accountpage.account_dropdown_click()
        time.sleep(2)
        self.accountpage.signout_menu_click()
        time.sleep(2)
        print("Evernote login has been successfully completed")
        self.driver.close()

    # TestCase for already registered user
    def test_02_validLoginNoteLogout(self):
        self.driver = webdriver.Firefox()
        # create homepage class object
        self.Login = homepage(self.driver)
        # create wrapper class object
        self.credentials = wrapper(self.driver)
        # create dashboard class object
        self.accountpage = dashboard(self.driver)
        # create Notes class object
        self.page_notes = Notes(self.driver)
        self.driver.implicitly_wait(25)
        self.driver.maximize_window()
        self.driver.get(evernote_Url)
        time.sleep(10)
        self.Login.reglogin_click()
        self.credentials.enter_emailid(valid_email)
        time.sleep(2)
        self.credentials.continue_button_click()
        time.sleep(2)
        self.credentials.enter_passwrd(valid_password)
        self.credentials.signin_button_click()
        time.sleep(25)
        self.accountpage.Home_click()
        self.accountpage.Notebutton_click()
        time.sleep(5)
        self.driver.switch_to.frame("qa-COMMON_EDITOR_IFRAME")
        self.page_notes.edit_NotesTitle(NotesTitle)
        self.page_notes.edit_NotesBody(NotesBody)
        self.driver.switch_to.default_content()
        self.accountpage.Home_click()
        time.sleep(15)
        self.accountpage.account_dropdown_click()
        time.sleep(2)
        self.accountpage.signout_menu_click()
        print("Evernote Valid login created note and log out successfully completed")
        self.driver.close()

    # TestCase for already registered user
    def test_03_validLoginOpenNoteLogout(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(25)
        # create homepage class object
        self.Login = homepage(self.driver)
        # create wrapper class object
        self.credentials = wrapper(self.driver)
        # create dashboard class object
        self.accountpage = dashboard(self.driver)
        # create Notes class object
        self.page_notes = Notes(self.driver)
        self.driver.maximize_window()
        self.driver.get(evernote_Url)
        time.sleep(10)
        self.Login.reglogin_click()
        time.sleep(2)
        self.credentials.enter_emailid(valid_email)
        time.sleep(2)
        self.credentials.continue_button_click()
        time.sleep(2)
        self.credentials.enter_passwrd(valid_password)
        self.credentials.signin_button_click()
        time.sleep(15)
        self.accountpage.Home_click()
        self.page_notes.creatednote_click()
        self.accountpage.note_action()
        self.accountpage.delete_action()
        time.sleep(15)
        self.accountpage.account_dropdown_click()
        time.sleep(2)
        self.accountpage.signout_menu_click()
        print("Evernote Valid login open created note and log out successfully completed")
        self.driver.close()

    # TestCase for not registered user
    def test_04_InvalidLogin(self):
        self.driver = webdriver.Firefox()
        # create homepage class object
        self.Login = homepage(self.driver)
        # create wrapper class object
        self.credentials = wrapper(self.driver)
        # create dashboard class object
        self.accountpage = dashboard(self.driver)
        # create Notes class object
        self.page_notes = Notes(self.driver)
        self.driver.implicitly_wait(25)
        self.driver.maximize_window()
        self.driver.get(evernote_Url)
        time.sleep(10)
        self.Login.reglogin_click()
        time.sleep(2)
        self.credentials.enter_emailid(invalid_email)
        time.sleep(2)
        self.credentials.continue_button_click()
        time.sleep(2)
        try:
            text = self.credentials.errortext()
        except:
            print("test failed")
        if bool(text) == True:
            print("UnSucessful login")
        self.driver.close()



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
