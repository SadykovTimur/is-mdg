from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    logo = Component(class_name='dg-logo')
    main_menu = Component(class_name="main-menu")
    user_name = Button(css='[class*="user__name"]')
    chat = Component(class_name="chat_icon")


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
