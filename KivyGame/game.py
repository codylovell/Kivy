from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.clock import Clock


class Sprite(Image):
    def __init__(self, **kwargs):
        """

        :rtype: object
        """
        super(Sprite, self).__init__(**kwargs)
        self.size = self.texture_size


class Background(Widget):
    def __init__(self, source):
        super(Background, self).__init__()
        self.image = Sprite(source=source)
        self.add_widget(self.image)
        self.size = self.image.size
        self.image_dupe = Sprite(source=source, x=self.width)
        self.add_widget(self.image_dupe)

    def update(self):
        self.image.x -= 2
        self.image_dupe -= 2

        if self.image.right <= 0:
            self.image.x = 0
            self.image_dupe.x = self.width


class Game(Widget):

    def __init__(self):
        super(Game, self).__init__()
        self.background = (Background(source='images/galaxy-transparent.png'))
        self.size = self.background.size
        self.add_widget(self.background)
        self.add_widget(Sprite(source='images/39-bottle-png-image-download-image-of-bottle.png'))
        Clock.schedule_interval(self.update, 1.0/60.0)

    def update(self, *ignore):
        self.background.update()

class GameApp(App):
    def build(self):
        game = Game()
        Window.size = game.size
        return game


if __name__ == '__main__':
    GameApp().run()

