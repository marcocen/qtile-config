from libqtile.config import Screen
from libqtile import bar, widget
import platform
import re


def init_screens(border_color):
    hostname = platform.node()
    widget_defaults = dict(
        font = 'Consolas',
        fontsize = 18,
        padding = 3,
    )
    if hostname == 'mcenturion-agesic':
        return  [
            Screen(bottom = bar.Bar([
                widget.GroupBox(
                    urgent_alert_method='text',
                    this_current_screen_border=border_color,
                    disable_drag=True,
                    **widget_defaults
                ),
                widget.Spacer(),

                widget.Volume(**widget_defaults),
            ], 30,),
            ),
            Screen(bottom = bar.Bar([
                widget.GroupBox(
                    urgent_alert_method='text',
                    this_current_screen_border=border_color,
                    disable_drag=True,
                    **widget_defaults
                ),
                widget.Prompt(**widget_defaults),
                widget.Spacer(),
                widget.Systray(**widget_defaults),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p', **widget_defaults),
            ], 30,),
            ),
            Screen(bottom = bar.Bar([
                widget.GroupBox(
                    urgent_alert_method='text',
                    this_current_screen_border=border_color,
                    disable_drag=True,
                    **widget_defaults
                ),
                widget.Spacer(),
                widget.Systray(**widget_defaults),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p', **widget_defaults),
            ], 30,),
            )
        ]
    if hostname == 'crusher.fing.edu.uy':
        return [
            Screen(bottom = bar.Bar([
                widget.GroupBox(
                    urgent_alert_method='text',
                    this_current_screen_border=border_color,
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
                    this_current_screen_border=border_color,
                    **widget_defaults
                ),
                widget.Spacer(),
                widget.Systray(**widget_defaults),
                widget.Volume(**widget_defaults),
            ], 30,),
            ),
        ]
