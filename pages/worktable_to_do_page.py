# encoding:utf8

from .base_page import BasePage


class WorkToDo(BasePage):
    '''
    第二层：
    页面元素进行分离，每个元素只定位一次，隔离定位，如果页面改变，只需要改变相应的元素定位；
    业务逻辑分离 或 操作元素动作分离
    '''

    # 我的待办定位 （定位分离）
    def worktable_undo(self):
        return self.by_xpath('//*[@id="new_worktable_nav"] //li[1]/a')

    # 获取我的待办文本信息 （操作元素动作分离）
    def worktable_undo_text(self):
        return self.worktable_undo().text
