from libqtile.config import Group, ScratchPad, DropDown
from libqtile import layout

def init_groups(hostname, border_color):
    if hostname == 'crusher.fing.edu.uy':
        groups = [
            Group('1', layouts=[
                layout.Max(),
                layout.Stack(num_stacks=2,
                             border_focus=border_color,
                             border_width=2),
                layout.MonadTall(border_focus=border_color,
                                 border_width=2),
            ]),
            Group('2', layouts=[
                layout.Max(),
                layout.MonadWide(border_focus=border_color,
                                 border_width=2),
            ]),
        ]
    if hostname == 'mcenturion-agesic':
        groups = [
            Group('1', layouts=[layout.Max()]),
            Group('2', layouts=[
                layout.Max(),
                layout.Stack(num_stacks=2,
                             border_focus=border_color,
                             border_width=2),
                layout.TreeTab(border_focus=border_color,
                               border_width=2),
            ]),
            Group('3', layouts=[
                layout.Max(),
                layout.Stack(num_stacks=2,
                             border_focus=border_color,
                             border_width=2),
                layout.TreeTab(border_focus=border_color,
                               border_width=2),
            ]),
        ]
    return groups
