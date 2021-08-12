
import ncurus.layout
import ncurus.widgets as widget


class Layout(widget.Widget):

    def __init__(self, win):
        self.win = win

        self.left, self.center, self.right = self.disp_win()
        self.dialog_zone = win.subwin(self.max_y // 3 * 2, 0)

    def disp_win(self):
        for i in (0, 1, 2):
            subwin = self.win.subwin(self.max_y // 3*2,
                                     self.max_x // 3,
                                     0,
                                     (self.max_x // 3)*i)
            yield subwin

    def disp_dialog(self, *args, **kwargs):
        d = self.dialog_zone

        return widget.ChoiceBox(0, self.max_y // 3, *d.getmaxyx()[::-1], global_win=self.dialog_zone)

    def disp_frames(self):
        windows = (self.left, self.center, self.right)

        return (widget.Frame(window) for window in windows)
