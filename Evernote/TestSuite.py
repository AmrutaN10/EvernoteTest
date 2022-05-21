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

driver = webdriver.Firefox()
# create homepage class object
Login = homepage(driver)
# create wrapper class object
credentials = wrapper(driver)
# create dashboard class object
accountpage = dashboard(driver)
# create Notes class object
page_notes = Notes(driver)


class loginfun(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # below commented lines can be uncommented for headless execution
        # cls.options = webdriver.FirefoxOptions()
        # cls.options.headless = True
        # driver = webdriver.Firefox(options=cls.options)
        driver.maximize_window()
        driver.get("https://evernote.com/")

    # TestCase for already registered user
    def test_01_validLogin(self):
        Login.reglogin_click()
        credentials.enter_emailid("naikamruta43@gmail.com")
        time.sleep(2)
        credentials.continue_button_click()
        time.sleep(2)
        credentials.enter_passwrd("123456")
        credentials.signin_button_click()
        time.sleep(15)
        try:
            text = accountpage.hometext()
        except:
            print("test failed")
        if bool(text) == True:
            print("Sucessful login")

        accountpage.account_dropdown_click()
        time.sleep(2)
        accountpage.signout_menu_click()
        time.sleep(2)
        print("Evernote login has been successfully completed")

    # TestCase for already registered user
    def test_02_validLoginNoteLogout(self):
        time.sleep(10)
        Login.mainlogin_click()
        credentials.enter_emailid("naikamruta43@gmail.com")
        time.sleep(2)
        credentials.continue_button_click()
        time.sleep(2)
        credentials.enter_passwrd("123456")
        credentials.signin_button_click()
        time.sleep(25)
        accountpage.Home_click()
        accountpage.Notebutton_click()
        time.sleep(5)
        driver.switch_to.frame("qa-COMMON_EDITOR_IFRAME")
        page_notes.edit_NotesTitle("TestCase03")
        page_notes.edit_NotesBody("Hellooooo, this is to test valid login create note and logout")
        driver.switch_to.default_content()
        accountpage.Home_click()
        time.sleep(15)
        accountpage.account_dropdown_click()
        time.sleep(2)
        accountpage.signout_menu_click()
        print("Evernote Valid login created note and log out successfully completed")

    # TestCase for already registered user
    def test_03_validLoginOpenNoteLogout(self):
        time.sleep(10)
        Login.mainlogin_click()
        credentials.enter_emailid("naikamruta43@gmail.com")
        time.sleep(2)
        credentials.continue_button_click()
        time.sleep(2)
        credentials.enter_passwrd("123456")
        credentials.signin_button_click()
        time.sleep(15)
        accountpage.Home_click()
        page_notes.creatednote_click()
        accountpage.note_action()
        accountpage.delete_action()
        time.sleep(15)
        accountpage.account_dropdown_click()
        time.sleep(2)
        accountpage.signout_menu_click()
        print("Evernote Valid login open created note and log out successfully completed")

    # TestCase for not registered user
    def test_04_InvalidLogin(self):
        time.sleep(10)
        Login.mainlogin_click()
        credentials.enter_emailid("namruta43@gmail.com")
        time.sleep(2)
        credentials.continue_button_click()
        time.sleep(2)
        time.sleep(2)
        try:
            text = credentials.errortext()
        except:
            print("test failed")
        if bool(text) == True:
            print("UnSucessful login")

    @classmethod
    def tearDownClass(cls):
        driver.close()
        driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
