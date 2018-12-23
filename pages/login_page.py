# encoding:utf8
from .base_page import BasePage
from .worktable_to_do_page import WorkToDo

class LoginPage(BasePage):
    '''
    第二层：
    - 页面元素进行分离，每个元素只定位一次，
    隔离定位，如果页面改变，只需要改变相应的元素定位；
    每当页面发生变化的时候，只需要在用例中寻找变动的部分进行修改
    - 业务逻辑分离 或 操作元素动作分离

    注意：
    - 不要在page页面对象外做元素定位 ,
    - 不在page页面对象里面写断言，除非是页面是否成功加载断言
    - 需要多少个元素就定位多少个，不需要对整个页面的元素进行定位
    - 当你的用例设计页面跳转时，例如登陆操作，登陆完成后跳转首页，
    当页面发生“跳转”，封装的业务逻辑需要返回（return）对应的页面对象的实例
    '''
    # 登陆输入框定位（定位分离）
    def form_username(self):
        return self.by_xpath('//input[@id="username"]')

    # 密码输入框定位（定位分离）
    def form_password(self):
        return self.by_xpath('//input[@id="password_input"]')

    # 登陆按钮定位  （定位分离）
    def login_button(self):
        return self.by_xpath('//input[@id="tcloud_login_button"]')

    # 登陆错误信息定位
    def login_error_msg(self):
        return self.by_xpath('//span[@id="error-tips"]')

    # 登陆操作（业务逻辑分离）
    def login(self, username, password):
        # 输入账号
        self.form_username().send_keys(username)
        # 输入密码
        self.form_password().send_keys(password)
        # 点击登陆按钮
        self.login_button().click()
        # 当你的用例设计页面跳转时，例如登陆操作，登陆完成后跳转首页，
        # 当页面发生“跳转”，封装的业务逻辑需要返回（return）对应的页面对象的实例
        # 返回页面对象实例 （实现页面跳转）
        return WorkToDo(self.driver)


