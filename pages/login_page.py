# encoding:utf8

from .base_page import BasePage
from .worktable_to_do_page import WorkToDo


class LoginPage(BasePage):
    url = None

    # 登陆输入框定位
    def form_username(self):
        return self.by_id('username')

    # 密码输入框定位
    def form_password(self):
        return self.by_id('password_input')

    # 登陆按钮定位
    def login_button(self):
        return self.by_id('tcloud_login_button')

    # 登陆错误信息定位
    def login_error_msg(self):
        return self.by_id('error-tips')

    # 实际操作里，尽量不要写断言，除非是页面的跳转
    def login(self, username, password):
        # 参数化输入账号
        self.form_username().send_keys(username)

        # 参数化输入密码
        self.form_password().send_keys(password)

        # 定位登陆按钮，点击登陆按钮
        self.login_button().click()

        # 返回实例页面对象 （实现页面跳转）
        return WorkToDo(self.driver)
