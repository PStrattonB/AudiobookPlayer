# import os to grab all .mp3 songs from folder
# and random to pick a random song from the song list
import os
import random
# import kivy library for UI design
import kivy
kivy.require('2.3.0')
from kivy.app import App
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.button import MDIconButton
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivymd.app import MDApp
# import soundloader to load song in kivy
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.clock import Clock

Window.size = (400, 600)


class MyApp(MDApp):

    def build(self):
        layout = MDRelativeLayout(md_bg_color=[0, 0.5, 1, 1])
        self.music_dir = 'C:/Aaa'
        music_files = os.listdir(self.music_dir)

        print(music_files)

        self.song_list = [x for x in music_files if x.endswith('.mp3')]
        print(self.song_list)

        self.song_count = len(self.song_list)

        # Song Label/Title
        self.songlabel = Label(pos_hint={'center_x': 0.5, 'center_y': 0.96},
                               size_hint=(1, 1),
                               font_size=18)

        # Album Image
        self.albumimage = Image(pos_hint={'center_x': 0.5, 'center_y': 0.55},
                                size_hint=(0.8, 0.75))

        # Play and Stop buttons
        self.playbutton = MDIconButton(pos_hint={'center_x': 0.4, 'center_y': 0.05},
                                       icon='play',
                                       on_press=self.playaudio)

        self.stopbutton = MDIconButton(pos_hint={'center_x': 0.55, 'center_y': 0.05},
                                       icon='stop',
                                       on_press=self.stopaudio, disabled=True)
        layout.add_widget(self.playbutton)
        layout.add_widget(self.stopbutton)
        layout.add_widget(self.songlabel)
        layout.add_widget(self.albumimage)

        # Play a random song on start
        # Clock.schedule_once(self.playaudio)

        return layout

    def playaudio(self, obj):
        self.playbutton.disabled = True
        self.stopbutton.disabled = False
        self.song_title = self.song_list[random.randrange(0, self.song_count)]
        print(self.song_title)
        self.sound = SoundLoader.load('{}/{}'.format(self.music_dir, self.song_title))
        self.songlabel.text = "==== Playing ~ " + self.song_title[:-4] + " ===="
        self.albumimage.source = "C:/Aaa/The Primal Hunter.jpg"
        self.sound.play()

    def stopaudio(self, obj):
        self.playbutton.disabled = False
        self.stopbutton.disabled = True
        self.sound.stop()

if __name__ == '__main__':
    MyApp().run()
