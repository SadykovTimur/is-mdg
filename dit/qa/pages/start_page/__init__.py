from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.start_page.components.header import Header

__all__ = ['StartPage']


class StartPage(Page):
    header = Header(class_name="header")
    item = Components(css='[class*="nav-item"]')
    main = Component(id="main")
    footer = Component(tag='footer')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.img.visible
                assert self.header.lk_user.visible
                assert self.header.telegram.visible
                assert self.header.youtube.visible
                assert self.header.vk.visible
                assert self.header.ok.visible

                assert self.item[0].visible
                assert self.main.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
