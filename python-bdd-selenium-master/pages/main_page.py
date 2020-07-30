from core.base_page import BasePage
from resources.pages import mainpage


class MainPage(BasePage):
    """
    Main Github page representation.
    Class for UI actions related to this page
    """

    def __init__(self, browser):
        """
        :type locators_path: str - path to *.def.csv file with locators for this page
        :type browser: selenium.webdriver.*
        """
        super(MainPage, self).__init__(browser)

    def submit_search(self, text):
        self.type(mainpage.search_field, text)
        self.send_enter(mainpage.search_field)

    def click_button_login(self):
        self.click(mainpage.search_b_login)

    def submit_login(self, text):
        self.type(mainpage.search_field_l, text)
        self.send_enter(mainpage.search_field_l)

    def submit_password(self, text):
        self.type(mainpage.search_field_p, text)
        self.send_enter(mainpage.search_field_p)

    def click_login(self):
        self.click(mainpage.button_login)

    def click_button_account(self):
        self.click(mainpage.button_account)

    def account_name(self):
        self.get_text(mainpage.search_name_account)

    def click_admin_page(self):
        self.click(mainpage.search_admin_page)

    def click_dialogs_page(self):
        self.click(mainpage.search_dialogs_page)

    def click_search(self):
        self.click(mainpage.search_site)

    def enter_text(self, text):
        self.type(mainpage.search_site_field, text)
        self.send_enter(mainpage.search_site_field)

    def click_notifications(self):
        self.click(mainpage.search_button_notifi)

    def click_write_button(self):
        self.click(mainpage.search_write_button)

    def click_my_lenta_page(self):
        self.click(mainpage.search_my_lenta_page)

    def click_write(self):
        self.click(mainpage.search_write)

    def click_dev_page(self):
        self.click(mainpage.search_dev_page)

    def click_page_streams(self):
        self.click(mainpage.search_page_streams)

    def click_page_hab(self):
        self.click(mainpage.search_page_hab)

    def click_page_infb(self):
        self.click(mainpage.search_infb_page)

    def click_logout(self):
        self.click(mainpage.search_logout_button)



