from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.components.header import Header

__all__ = ['AuthPage']


class AuthPage(Page):
    header = Header(class_name="header")
    title = Component(tag='h1')
    login = TextField(css='input[type="text"]')
    password = TextField(css='input[type="password"]')
    forgot_password = Button(xpath="//a[contains(text(),'Забыли пароль?')]")
    submit = Button(xpath="//button[text()='Войти']")
    submit_sudir = Component(xpath="//button[text()='Войти через СУДИР']")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.logo.visible
                assert self.header.main_menu.visible

                assert self.title.visible
                assert self.login.visible
                assert self.password.visible
                assert self.forgot_password.visible
                assert self.submit.visible

                return self.submit_sudir.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
