# encoding:utf8


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def by_id(self, id):
        return self.driver.find_element_by_id(id)

    def by_css(self, css):
        return self.driver.find_element_by_id(css)
