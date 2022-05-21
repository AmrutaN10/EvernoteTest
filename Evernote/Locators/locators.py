# locators class
class locators():
    # Homepage web elements
    reglogin_rx = "//a[contains(text(),'Already have an account? Log in')]"
    mainlogin_rx = "//nav[@class='utility-nav']//ul//li//a[contains(text(),'Log In')]"

    # Wrapper page web elements
    emailid_text_id = "username"
    continue_button_id = "loginButton"
    passwrd_text_id = "password"
    signin_button_id = "loginButton"
    errormessage_id = "responseMessage"

    # Dashboard web elements
    account_dropdown_rx = "//div[@class='PPxtw0kw4VI37OJ4B3Rm']"
    signout_menu_rx = "//span[@class='_MD_fSTtapAb30uIA9oC ATm3C3aUTlB1vovtP09c fqGPff50YEEMz7JBRAUX " \
                      "HUWoDG8e8KhEOGqVocpC']"
    New_note_dropdown_rx = "//button[@id='qa-CREATE_NOTE']"
    Notebutton_rx = "//*[@class='eS__h0j9YqpZ7rzWh1Qa']"
    create_newnote_rx = "//div[@id='qa-HOME_NOTE_WIDGET_CREATE_NOTE']"
    Home_rx = "//span[contains(text(),'Home')]"
    create_notebook_rx = "//button[@id='qa-NAVBAR_NOTEBOOK_ADD_BUTTON']"
    notebook_name_rx = "//input[@id='qa-DIALOG_INPUT_0']"
    create_button_rx = "//button[@id='qa-DIALOG_SUBMIT']"
    filter_notebook_rx = "//div[@id='qa-FILTER_INPUT']//input[@type='text']"
    expand_notebook_rx = "//*[@class='TMj2RLlBk1PZMykmhhIS _w1EW2j8Gs8yZoWDLfj8']"
    open_note_rx = "//span[@id='qa-SPACE_VIEW_NOTE_TITLE_d5c94658-0eb2-9297-fa2d-c36b31be929e']"
    note_action_button_rx = "//div[@aria-label='More actions']"
    delete_action_button_rx = "//span[contains(text(),'Move to Trash')]"

    # Notes page web elements
    NotesTitle = "//textarea[@class='dSbRl s9EjL']"
    NotesBody = "en-note"
    creatednote_rx = "//span[contains(text(),'TestCase03')]"
