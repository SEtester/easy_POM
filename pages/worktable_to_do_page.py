# encoding:utf8

from .base_page import BasePage


class WorkToDo(BasePage):

    def worktable_undo(self):
        return self.by_css('#new_worktable_nav li:nth-child(1) a')

    def worktable_undo_text(self):
        return self.worktable_undo().text
