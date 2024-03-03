from libqtile import bar, layout, widget, extension ,qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from libqtile.dgroups import simple_key_binder


# apps: pavucontrol, pamixer, brightnessctl, dmenu
# maybe widgets: bluetooth, wlan
# remove sep groups 


# https://www.reddit.com/r/unixporn/comments/o41k74/qtile_first_attempt_at_using_a_wm_let_me_know/?onetap_auto=true
# https://www.reddit.com/r/qtile/comments/qupcl4/some_qtile_changes_config_file/?onetap_auto=true

########## variables ##########

mod = "mod4"
terminal = "kitty"
browser = "brave"
editor = "code"
colors = {
    "background": "#2e3440",
    "light-background": "#3a4253",
    "foreground": "#e1e3e7",
    "white": "#ffffff",
    "blue": "#88c0d0",
}


########## keybinds ##########

keys = [
    # apps
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "c", lazy.spawn(editor), desc="Launch editor"),
    Key([mod], "d", lazy.run_extension(extension.DmenuRun(
        background=colors["background"],
        foreground=colors["foreground"],
        selected_background=colors["blue"],
        selected_foreground=colors["background"],
        dmenu_ignorecase=True,
        font="Cascadia Code Nerd Font",
        fontsize=14,
    ))),
    
    # window movement
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
     
    Key([mod], "Comma", lazy.layout.grow()),
    Key([mod], "period", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "m", lazy.layout.maximize()),
    
    # misc
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "e", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),

    # special keys (from xev)
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")), #FN+F1 mute audio
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --unmute --decrease 5")), #FN+F2 volume down
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --unmute --increase 5")), #FN+F3 volume up
    #FN+F4
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")), #FN+F5 brightness down
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")), #FN+F6 brightness up
    #FN+F7
    #FN+F8
    #FN+F9
    #FN+F10
    #FN+F11
    #FN+F12
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
    Click([mod, 'shift'], "Button1", lazy.window.disable_floating()),
    Click([mod], "Button1", lazy.window.bring_to_front()),
]


########## groups ##########

groups = [
    Group("    Sys"),
    Group("    Web"),
    Group("󰭹    Chat"),
    Group("    Misc"),
]
dgroups_key_binder = simple_key_binder("mod4")


########## layouts ##########

layout_theme = {
    "margin": 6,
    "border_width": 0,
    "border_focus": colors["blue"],
    "border_normal": colors["background"],
}

layouts = [
    layout.MonadTall(**layout_theme),
]


########## widgets ##########

widget_defaults = dict(
    font="Cascadia Code Nerd Font",
    fontsize=18,
    padding=0,
    foreground=colors["foreground"],
    background=colors["background"],
)
extension_defaults=widget_defaults.copy()

def sep():
    return widget.Sep(
        linewidth=0,
        padding=14,
    )

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(
                    filename="~/.config/qtile/dark_arch.png",
                    scale="True",
                    background=colors["blue"],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal)}
                ),
                widget.GroupBox(
                    margin_x=0,
                    margin_y=3,
                    padding_x=12,
                    padding_y=0,
                    borderwidth=3,
                    disable_drag=True,
                    use_mouse_wheel=False,
                    highlight_method="line",
                    highlight_color=colors["light-background"],
                    this_current_screen_border=colors["blue"],
                    active=colors["blue"],
                    inactive=colors["foreground"],
                ),
                widget.WindowName(
                    background=colors["light-background"],
                    padding=12,
                    format="{name}",
                ),
                widget.Systray(
                    background=colors["light-background"],
                    padding=6,
                ),
                widget.Sep(
                    linewidth=0,
                    padding=12,
                    background=colors["light-background"],
                ),
                sep(),
                widget.TextBox(
                    text="CPU: ",
                    foreground=colors["blue"],
                ),
                widget.CPU(
                    format="{load_percent}%",
                ),
                sep(),
                widget.TextBox(
                    text="RAM:",
                    foreground=colors["blue"],
                ),
                widget.Memory(
                    measure_mem="G",
                ),
                sep(),
                widget.TextBox(
                    text="Volume: ",
                    foreground=colors["blue"],
                    mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")}
                ),
                widget.PulseVolume(
                    volume_app="pavucontrol",
                    update_interval=0.02,
                ),
                sep(),
                widget.TextBox(
                    text="Battery: ",
                    foreground=colors["blue"],
                ),
                widget.Battery(
                    format="{percent:2.0%}",
                    #format="{char} {percent:2.0%}  {hour:d}:{min:02d}",
                    charge_char="charging",
                    update_interval=10,
                ),
                sep(),
                widget.Clock(
                    padding=14,
                    format="%y-%m-%d %H:%M",
                    background=colors["blue"],
                    foreground=colors["background"],
                ),
            ],
            size=28,
        ),
    ),
]

dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = True
cursor_warp = True

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    **layout_theme,
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"
