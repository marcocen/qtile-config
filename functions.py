import os

def screenlayout(qtile, orientation):
    home = os.path.expanduser('~')
    qtile.cmd_spawn(home + "/.config/screenlayout/{}.sh".format(orientation))
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
