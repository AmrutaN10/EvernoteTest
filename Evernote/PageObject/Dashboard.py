from Helper.helper import *

# Dashboard class
class dashboard():
    def __init__(self, driver):
        self.driver = driver
        self.account_dropdown_rx = locators.account_dropdown_rx
        self.signout_menu_rx = locators.signout_menu_rx
        self.New_note_dropdown_rx = locators.New_note_dropdown_rx
        self.Notebutton_rx = locators.Notebutton_rx
        self.create_newnote_rx = locators.create_newnote_rx
        self.Home_rx = locators.Home_rx
        self.create_notebook_rx = locators.create_notebook_rx
        self.notebook_name_rx = locators.notebook_name_rx
        self.create_button_rx = locators.create_button_rx
        self.filter_notebook_rx = locators.filter_notebook_rx
        self.expand_notebook_rx = locators.expand_notebook_rx
        self.open_note_rx = locators.open_note_rx
        self.note_action_button_rx = locators.note_action_button_rx
        self.delete_action_button_rx = locators.delete_action_button_rx

    def hometext(self):
        home_text = self.driver.find_element(by=By.XPATH, value=self.Home_rx).text
        return home_text

    def account_dropdown_click(self):
        self.driver.find_element(by=By.XPATH, value=self.account_dropdown_rx).click()

    def signout_menu_click(self):
        self.driver.find_element(by=By.XPATH, value=self.signout_menu_rx).click()

    def New_note_dropdown_click(self):
        self.driver.find_element(by=By.XPATH, value=self.New_note_dropdown_rx).click()

    def Notebutton_click(self):
        self.driver.find_element(by=By.XPATH, value=self.Notebutton_rx).click()

    def Home_click(self):
        self.driver.find_element(by=By.XPATH, value=self.Home_rx).click()

    def create_notebook_click(self):
        self.driver.find_element(by=By.XPATH, value=self.create_notebook_rx).click()

    def notebook_name_enter(self, notebook):
        self.driver.find_element(by=By.XPATH, value=self.notebook_name_rx).send_keys(notebook)

    def create_button_submit(self):
        self.driver.find_element(by=By.XPATH, value=self.create_button_rx).click()

    def filter_notebook(self, filter1):
        self.driver.find_element(by=By.XPATH, value=self.filter_notebook_rx).send_keys(filter1)

    def expand_notebook(self):
        self.driver.find_element(by=By.XPATH, value=self.expand_notebook_rx).click()

    def open_note(self):
        self.driver.find_element(by=By.XPATH, value=self.open_note_rx).click()

    def note_action(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                               self.note_action_button_rx))).click()

        # self.driver.find_element(by=By.XPATH, value=self.note_action_button_rx).click()

    def delete_action(self):
        self.driver.find_element(by=By.XPATH, value=self.delete_action_button_rx).click()
