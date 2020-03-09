from libqtile.config import Key
from libqtile.command import lazy
from functions import screenlayout, kbd_layout

def init_keys(mod):
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
        Key([mod], "v", lazy.function(screenlayout, 'vertical')),
        Key([mod], "h", lazy.function(screenlayout, 'horizontal')),

        # Keyboard layouts
        Key([mod], "s", lazy.function(kbd_layout, "es", option=" ")),
        Key([mod], "e", lazy.function(kbd_layout, "us", "altgr-intl", "compose:menu,ctrl:nocaps")),

        # Lock screen
        Key([mod], "l", lazy.spawn("xscreensaver-command -lock")),
    ]
    return keys
