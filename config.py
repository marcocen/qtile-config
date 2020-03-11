import os
import subprocess
import screens
import keybinds
import groups
import platform
from libqtile.config import Key, Screen, Group, Drag, Click, ScratchPad, DropDown
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401

@hook.subscribe.startup_once
def autostart():
   home = os.path.expanduser('~/.config/qtile/autostart.sh')
   subprocess.call([home])

mod = "mod4"
border_color = '339966'
keys = keybinds.init_keys(mod)

groups = groups.init_groups(platform.node(), border_color)

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])
groups.append(ScratchPad("scratchpad", [
   # define a drop down terminal.
   # it is placed in the upper third of selfcreen by default.
   DropDown("term", "xterm", height=0.5),
   DropDown("org", "emacs", height=0.5),
]))
layouts = [
    layout.Max(),
    layout.Stack(num_stacks=2,border_focus=border_color, border_width=2),
    layout.MonadTall(border_focus=border_color, border_width=2),
    layout.MonadWide(border_focus=border_color, border_width=2),
    layout.TreeTab(border_focus=border_color, border_width=2),
]

screens = screens.init_screens(border_color)

# Drag floating layouts.
mouse = [
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
#focus_on_window_activation = "smart"
