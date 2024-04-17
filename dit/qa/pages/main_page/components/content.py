from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['Content']


class ContentWrapper(ComponentWrapper):
    title = Component(tag='h1')
    info = Component(css='[class*="reestr"]')
    table = Component(css='[class*="mdg-lk-table"]')
    filter = Component(class_name="mdg-lk-header-row")


class Content(Component):
    def __get__(self, instance, owner) -> ContentWrapper:
        return ContentWrapper(instance.app, self.find(instance), self._locator)
