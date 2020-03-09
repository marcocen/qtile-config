# -*- coding: utf-8 -*-
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget
from typing import List  # noqa: F401

import os

mod = "mod4"

def vertical(qtile):
    home = os.path.expanduser('~')
    qtile.cmd_spawn(home + "/.config/screenlayout/vertical.sh")
    qtile.cmd_restart()

def horizontal(qtile):
    home = os.path.expanduser('~')
    qtile.cmd_spawn(home + "/.config/screenlayout/horizontal.sh")
    qtile.cmd_restart()

def kbd_layout(qtile, layout=None, variant=None, option=None):
    cmd = "setxkbmap "
    if layout:
        cmd = cmd + "-layout {} ".format(layout)
    if variant:
        cmd = cmd + "-variant {} ".format(variant)
    if option:
        cmd = cmd + "-option {} ".format(option)
    qtile.cmd_spawn(cmd)


keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),

    # Move windows to other stack
    Key([mod, "shift"], "j", lazy.layout.client_to_next()),

    # Switch window focus to other pane(s) of stack
    Key(["mod1"], "Tab", lazy.layout.next()),

    # Swap panes of split stack
    Key(["mod5"], "Tab", lazy.screen.next()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn("xterm")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),

    # Monitor orientation
    Key([mod], "v", lazy.function(vertical)),
    Key([mod], "h", lazy.function(horizontal)),

    # Keyboard layouts
    Key([mod], "s", lazy.function(kbd_layout, "es", option=" ")),
    Key([mod], "e", lazy.function(kbd_layout, "us", "altgr-intl", "compose:menu,ctrl:nocaps")),

    # Lock screen
    Key([mod], "l", lazy.spawn("xscreensaver-command -lock")),

]

groups = [Group(i) for i in "1234"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

layouts = [
    layout.Max(),
    layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    # layout.MonadTall(),
    layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# global font options
widget_defaults = dict(
    font = 'Consolas',
    fontsize = 18,
    padding = 3,
)
extension_defaults = widget_defaults.copy()
inoffensive_green = '339966'

screens = [
    Screen(bottom = bar.Bar([
        widget.GroupBox(
            urgent_alert_method='text',
            this_current_screen_border=inoffensive_green,
            disable_drag=True,
            **widget_defaults
        ),
        widget.Prompt(**widget_defaults),
        widget.Spacer(),
        widget.Clock(format='%Y-%m-%d %a %I:%M %p', **widget_defaults),
    ], 30,),
    ),
    Screen(bottom = bar.Bar([
        widget.GroupBox(
            urgent_alert_method='text',
            disable_drag=True,
            this_current_screen_border=inoffensive_green,
            **widget_defaults
        ),
        widget.Spacer(),
        widget.Systray(**widget_defaults),
        widget.Volume(**widget_defaults),
    ], 30,),
    ),
]


# Drag floating layouts.
mouse = [
    # Drag([mod], "Button1", lazy.window.set_position_floating(),
    #      start=lazy.window.get_position()),
    # Drag([mod], "Button3", lazy.window.set_size_floating(),
    #      start=lazy.window.get_size()),
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
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
