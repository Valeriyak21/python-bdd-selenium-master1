from core.base_page import BasePage
from resources.pages import searchpage


class SearchPage(BasePage):
    """
    Search page representation.
    Class for UI actions related to this page
    """

    def __init__(self, browser):
        """
        :type locators_path: str - path to *.def.csv file with locators for this page
        :type browser: selenium.webdriver.firefox.webdriver.WebDriver
        """
        super(SearchPage, self).__init__(browser)

    def get_repositories(self):
        return self.get_elements(searchpage.repository_title)


