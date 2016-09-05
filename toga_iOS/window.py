from .libs import *


class Window(object):
    def __init__(self, title, position=(100, 100), size=(640, 480)):
        self._app = None
        self._content = None

        self.startup()

    def startup(self):
        self._impl = UIWindow.alloc().initWithFrame_(UIScreen.mainScreen().bounds)

    @property
    def app(self):
        return self._app

    @app.setter
    def app(self, app):
        if self._app:
            raise Exception("Window is already associated with an App")

        self._app = app

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, widget):
        self._content = widget
        self._content.window = self
        self._content.app = self.app

        self._controller = UIViewController.alloc().init()
        self._controller.view = widget._impl

        self._impl.rootViewController = self._controller

    def show(self):
        self._impl.makeKeyAndVisible()

        # self._impl.visualizeConstraints_(self._impl.contentView().constraints())
        # Do the first layout render.
        self.content._update_layout(
            width=self.content._impl.frame.size.width,
            height=self.content._impl.frame.size.height
        )
