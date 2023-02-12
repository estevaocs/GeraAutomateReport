from selenium.webdriver.common.by import By

class ButonElement:


    def __init__(self, driver):
        self.driver=driver
        self.buton

    def set_by_name(self, name):
        self.element=self.driver.find_element(By.NAME, name)

    def set_by_id(self, id):
        self.element = self.driver.find_element(By.ID, id)

    def set_by_xpath(self, linkText):
        self.element = self.driver.find_element(By.LINK_TEXT, linkText)

    def set_by_partial_link_text(self, partialLinkText):
        self.element = self.driver.find_element(By.PARTIAL_LINK_TEXT, partialLinkText)

    def set_by_tag_name(self, tagName):
        self.element = self.driver.find_element(By.TAG_NAME, tagName)

    def set_by_class_name(self, className):
        self.element=self.driver.find_element(By.CLASS_NAME, className)

    def set_by_css_selector(self, cssSelector):
        self.element=self.driver.find_element(By.CSS_SELECTOR, cssSelector)

    def click(self):
        self.element.click()