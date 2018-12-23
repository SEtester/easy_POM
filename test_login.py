# encoding:utf8
from selenium import webdriver
from pages.login_page import LoginPage
import unittest


class LoginCase(unittest.TestCase):
    '''
    第三层
    使用单元测试框架对业务逻辑进行测试
    '''

    def setUp(self):
        # 实例化webdriver , 俗称：“打开浏览器”
        self.dr = webdriver.Chrome()

    def tearDown(self):
        # 关闭浏览器
        self.dr.quit()

    def test_login_success(self):
        username = '请输入你的TAPD账号'
        password = '请输入你的TAPD密码'
        # 调用封装好的登陆方法
        login_page = LoginPage(driver=self.dr, path='/cloud_logins/login')
        work_page = login_page.login(username, password)

        # 获取 工作台 “我的待办” 文本信息
        text_worktable_undo = work_page.worktable_undo_text()
        print(text_worktable_undo)
        # # 判断是否登陆成功
        # # 预期结果：’我的代办‘  ， 实际结果（运行代码获取的文本信息）：text_worktable_undo
        # # 单元测试框架里面自带断言方法，assertEqual（’预期结果‘，’实际结果‘）
        self.assertEqual('我的待办', text_worktable_undo)


if __name__ == '__main__':
    unittest.main()
