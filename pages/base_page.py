# encoding:utf8

class BasePage():
    '''
    第一层：对Selenium 进行二次封装，定义一个所有页面都继承的 BasePage ，
    封装 Selenium 基本方法 例如：元素定位，元素等待，导航页面 ，
    不需要全部封装，用到多少方法就封装多少方法。
    '''

    def __init__(self, driver, path=None):
        '''
        :param driver: Webdriver实例对象
        :param path:   传入URI
        '''
        self.driver = driver
        self.url = 'https://www.tapd.cn'

        # 设置全局元素定位等待时间 10 秒
        self.driver.implicitly_wait(10)

        # 打开页面
        self.load_page(path)

    def by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def load_page(self, path=None):
        # 如果不传入path,则不打开浏览器
        if path == None:
            url = None
        else:
            url = self.url + path
        if url != None:
            self.driver.get(url)
