from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.components.header import Header
from dit.qa.pages.main_page.components.content import Content
from dit.qa.pages.main_page.components.logout import Logout
from dit.qa.pages.main_page.components.user_nav import UserNav

__all__ = ['MainPage']


class MainPage(Page):
    header = Header(class_name="header")
    content = Content(class_name="content-wrapper")
    user_nav = UserNav(css='[class*="user__menu"]')
    logout_modal = Logout(id="modal-log-out")
    footer = Component(tag='footer')

    def logout(self) -> None:
        self.header.user_name.click()
        self.user_nav.exit.click()
        self.logout_modal.submit_yes.click()

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.logo.visible
                assert self.header.chat.visible
                assert self.header.main_menu.visible
                assert self.header.user_name.visible

                assert self.content.title.visible
                assert self.content.info.visible
                assert self.content.table.visible
                assert self.content.filter.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
