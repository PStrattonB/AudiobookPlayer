from kivy.animation import Animation
from kivy.uix.label import Label
'''
The purpose of this code was to create a label that scrolls the text if it's too long to fit in the window.
However what seems to be happening currently is that it's just resizing and won't scroll the way I intended.
For now that's fine, but I need to come back to this and figure out why it's not scrolling.

Maybe it's because the text is being resized to fit the window, and then the scroll is being applied to the resized text.
Or it's because scrolling means something different in Kivy than I thought it did.

Marquee is the word I was looking for. I need to make a marquee label.
'''

class ScrollLabel(Label):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.max_lines = 1  # Keeps the text on a single line
        self.bind(size=self.on_size)
        self.bind(text=self.on_size)
        self.on_size()
        print("ran on_size")

    def on_size(self, *args):
        self.stop_scroll()
        if self.texture_size[0] > self.width:
            self.start_scroll()
        # if self.width < self.texture_size[0]:
        #     anim = Animation(x=-(self.texture_size[0]-self.width),
        #                      duration=5.0, t='in_out_quad') + Animation(x=0, duration=5.0, t='in_out_quad')
        #     anim.repeat = True
        #     anim.start(self)

    def start_scroll(self):
        anim = Animation(x=-(self.texture_size[0] - self.width), duration=5.0, t='in_out_quad') + \
            Animation(x=0, duration=5.0, t='in_out_quad')
        anim.repeat = True
        anim.start(self)
        self.anim = anim

    def stop_scroll(self):
        if hasattr(self, 'anim'):
            self.anim.cancel(self)
