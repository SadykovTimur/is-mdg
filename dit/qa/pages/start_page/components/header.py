from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    img = Component(class_name="img-fluid")
    lk_user = Button(css='[class*="btn-lk"]')
    telegram = Component(css='[alt="Телеграм"]')
    vk = Component(css='[alt="Наш Вконтакте"]')
    youtube = Component(css='[alt="Наш YouTube"]')
    ok = Component(css='[alt="Одноклассники"]')


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
