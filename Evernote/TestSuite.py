import time
from selenium import webdriver
import unittest
from PageObject.Homepage import homepage
from PageObject.wrapper import wrapper
from PageObject.Dashboard import dashboard
from PageObject.Notes import Notes

import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


class loginfun(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get("https://evernote.com/")

    # TestCase for already registered user
    def test_01_validLogin(self):
        driver = self.driver
        # create homepage class object
        Login = homepage(driver)
        Login.reglogin_click()
        # create wrapper class object
        credentials = wrapper(driver)
        credentials.enter_emailid("naikamruta43@gmail.com")
        time.sleep(2)
        credentials.continue_button_click()
        time.sleep(2)
        credentials.enter_passwrd("123456")
        credentials.signin_button_click()
        time.sleep(15)
        # create dashboard class object
        accountpage = dashboard(driver)
        assert accountpage
        accountpage.account_dropdown_click()
        time.sleep(2)
        accountpage.signout_menu_click()
        time.sleep(2)
        print("Evernote login has been successfully completed")

        # TestCase for already registered user
    def test_02_validLoginNoteLogout(self):
        driver = self.driver
        # create homepage class object
        main_Login = homepage(driver)
        time.sleep(10)
        main_Login.mainlogin_click()
        # create wrapper class object
        credentialsTC03 = wrapper(driver)
        credentialsTC03.enter_emailid("naikamruta43@gmail.com")
        time.sleep(2)
        credentialsTC03.continue_button_click()
        time.sleep(2)
        credentialsTC03.enter_passwrd("123456")
        credentialsTC03.signin_button_click()
        time.sleep(15)
        # create dashboard class object
        create_new_notes = dashboard(driver)
        create_new_notes.Home_click()
        create_new_notes.Notebutton_click()
        time.sleep(5)
        # create notes page class object
        page_notes = Notes(driver)
        driver.switch_to.frame("qa-COMMON_EDITOR_IFRAME")
        page_notes.edit_NotesTitle("TestCase03")
        page_notes.edit_NotesBody("Hellooooo, this is to test valid login create note and logout")
        driver.switch_to.default_content()
        create_new_notes.Home_click()
        time.sleep(15)
        create_new_notes.account_dropdown_click()
        time.sleep(2)
        create_new_notes.signout_menu_click()
        print("Evernote Valid login created note and log out successfully completed")

    # TestCase for already registered user
    def test_03_validLoginOpenNoteLogout(self):
        driver = self.driver
        # create homepage class object
        main04_Login = homepage(driver)
        time.sleep(10)
        main04_Login.mainlogin_click()
        # create wrapper class object
        credentialsTC04 = wrapper(driver)
        credentialsTC04.enter_emailid("naikamruta43@gmail.com")
        time.sleep(2)
        credentialsTC04.continue_button_click()
        time.sleep(2)
        credentialsTC04.enter_passwrd("123456")
        credentialsTC04.signin_button_click()
        time.sleep(15)
        # create dashboard class object
        create_new_notes04 = dashboard(driver)
        create_new_notes04.Home_click()
        # create notes page class object
        page_notes04 = Notes(driver)
        page_notes04.creatednote_click()
        create_new_notes04.note_action()
        create_new_notes04.delete_action()
        time.sleep(15)
        create_new_notes04.account_dropdown_click()
        time.sleep(2)
        create_new_notes04.signout_menu_click()
        print("Evernote Valid login open created note and log out successfully completed")

   # TestCase for already registered user
    def test_04_InvalidLogin(self):
        driver = self.driver
        # create homepage class object
        main01_Login = homepage(driver)
        time.sleep(10)
        main01_Login.mainlogin_click()
        # create wrapper class object
        credentialsTC01 = wrapper(driver)
        #enter valid username
        credentialsTC01.enter_emailid("namruta43@gmail.com")
        time.sleep(2)
        credentialsTC01.continue_button_click()
        time.sleep(2)
        #enter invalid password
        #credentialsTC01.enter_passwrd("12456")
        #credentialsTC01.signin_button_click()
        print("Evernote InValid login has been successfully completed")

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        driver.close()
        driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
