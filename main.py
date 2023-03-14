import kivy
import random
import time
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader

Window.clearcolor = (1, 1, 1, 1)
music = SoundLoader.load('music.wav')
music.play()


class WindowManager(ScreenManager):
    pass


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    time60 = ObjectProperty(None)
    hammer = ObjectProperty(None)
    quitbtn = ObjectProperty(None)
    fmy = ObjectProperty(None)
    startbtn = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(SecondWindow, self).__init__(**kwargs)
        index = random.sample(range(0, 5), 1)[0]
        x_index = [0.14, 0.4, 0.66, 0.14, 0.4, 0.66]
        y_index = [0.383, 0.383, 0.383, 0.11, 0.11, 0.11]
        self.fmy.pos_hint = {"x": x_index[index], "y": y_index[index]}

    def on_touch_down(self, touch):
        prior = eval(self.ids.score.text)
        a = touch.pos[0] - Window.size[0] / 851 * 20
        b = touch.pos[1] - Window.size[0] / 851 * 20
        f = touch.pos[0] - Window.size[0] / 851 * 53
        c = Window.size[0] / 851 * 62
        d = Window.size[1] / 478 * 91
        g = Window.size[0] / 851 * 170
        h = Window.size[1] / 478 * 52
        i = Window.size[0] / 851 * 110
        j = Window.size[1] / 478 * 35
        x_index = [0.14, 0.4, 0.66, 0.14, 0.4, 0.66]
        y_index = [0.383, 0.383, 0.383, 0.11, 0.11, 0.11]
        self.hammer.pos = [a, b]
        self.hammer.background_normal = "hammer_r.png"
        if self.fmy.pos[0] <= f <= self.fmy.pos[0] + c and self.fmy.pos[1] <= touch.pos[1] <= self.fmy.pos[1] + d and eval(self.time60.text) > 0 and eval(self.time60.text) != 60:
            e = random.sample(range(0, 5), 1)[0]
            self.fmy.pos_hint = {"x": x_index[e], "y": y_index[e]}
            mus = SoundLoader.load('scream.wav')
            mus.play()
            self.ids.score.text = str(int(prior) + 1)
        if self.startbtn.pos[0] <= touch.pos[0] <= self.startbtn.pos[0] + g and self.startbtn.pos[1] <= touch.pos[1] <= self.startbtn.pos[1] + h:
            self.startbtn.background_normal = "startbtndown.png"
        if self.quitbtn.pos[0] <= touch.pos[0] <= self.quitbtn.pos[0] + i and self.quitbtn.pos[1] <= touch.pos[1] <= self.quitbtn.pos[1] + j:
            self.quitbtn.background_normal = "Quit.png"
        print("touch down", touch)

    def on_touch_up(self, touch):
        a = Window.size[0]/851*110
        b = Window.size[1]/478*35
        c = Window.size[0] / 851 * 170
        d = Window.size[1] / 478 * 52
        self.hammer.background_normal = "hammer.png"
        if self.quitbtn.pos[0] <= touch.pos[0] <= self.quitbtn.pos[0] + a and self.quitbtn.pos[1] <= touch.pos[1] <= self.quitbtn.pos[1] + b:
            self.ids.score.text = "0"
            self.time60.text = "60"
            self.quitbtn.background_normal = "Quit1.png"
            Clock.unschedule(self.update_time)
            self.quits()
        if self.startbtn.pos[0] <= touch.pos[0] <= self.startbtn.pos[0] + c and self.startbtn.pos[1] <= touch.pos[1] <= self.startbtn.pos[1] + d:
            self.startbtn.background_normal = "startbtn.png"
            self.reset()

    def on_touch_move(self, touch):
        a = touch.pos[0] - Window.size[0] / 851 * 20
        b = touch.pos[1] - Window.size[0] / 851 * 20
        self.hammer.pos = [a, b]
        print("touch move", touch)

    def quits(self):
        sm.current = 'Main'
        self.manager.transition.direction = "right"

    def reset(self):
        self.ids.score.text = "0"
        self.time60.text = "60"
        Clock.unschedule(self.update_time)
        self.countdown()

    def countdown(self):
        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, dt):
        prior = eval(self.time60.text)
        if prior <= 0:
            Clock.unschedule(self.update_time)
        else:
            self.time60.text = str(int(prior) - 1)


kv = Builder.load_file("my.kv")
sm = WindowManager()
screens = [MainWindow(name="Main"), SecondWindow(name="Second")]
for screen in screens:
    sm.add_widget(screen)
sm.current = "Main"


class HitRatApp(App):
    def build(self):
        #Window.fullscreen =False
        Window.size = (2002, 1080)
        return sm


if __name__ == '__main__':
    HitRatApp().run()