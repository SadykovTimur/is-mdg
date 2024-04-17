from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['UserNav']


class UserNavWrapper(ComponentWrapper):
    exit = Button(css='[class*="exit"]')


class UserNav(Component):
    def __get__(self, instance, owner) -> UserNavWrapper:
        return UserNavWrapper(instance.app, self.find(instance), self._locator)
