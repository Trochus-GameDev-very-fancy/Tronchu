
import ncurus

from scenes import scene1
from src.layout import Layout


@ncurus.startup()
@ncurus.process_scene(scene1.execute)
def main(win):
    layout = Layout(win)

    dialog = layout.disp_dialog("Name")
    left, center, right = layout.disp_frames()

    layout.refresh()

    return dialog, left, center, right


if __name__ == "__main__":
    main()

    # gallery = layout.disp_widget(Gallery, "half", "up")
    # dialogs = layout.disp_widget(Dialogs, "half", "down")

    # layout.draw_borders(sep_line=True)

    # db_one = dialogs.disp_box("One")
    # db_two = dialogs.disp_box("Two")

    # return gallery, db_one, db_two
