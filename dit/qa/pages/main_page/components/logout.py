from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Logout']


class LogoutWrapper(ComponentWrapper):
    submit_yes = Button(xpath="//button[text()='Да']")


class Logout(Component):
    def __get__(self, instance, owner) -> LogoutWrapper:
        return LogoutWrapper(instance.app, self.find(instance), self._locator)
