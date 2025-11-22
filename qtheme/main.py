from os import path
from .utils.colors import red
from .cli import Qtile, Kitty, Menu
from argparse import ArgumentParser
from importlib.metadata import version


user_path = path.expanduser("~")
VERSION = version("qtheme")


def main():
    try:
        parser = ArgumentParser(
            prog="qtheme",
            description=(
                "Ideal tool to control the themes of your qtile environment "
                "and your kitty terminal."
            ),
        )

        main_actions = parser.add_mutually_exclusive_group()
        main_actions.add_argument(
            "-l", "--list", action="store_true", help="List available themes"
        )
        main_actions.add_argument(
            "--check", action="store_true", help="Check theme files syntax"
        )

        parser.add_argument("-t", dest="theme", help="Theme to set", metavar="theme")
        parser.add_argument(
            "-p",
            dest="position",
            help="Position of the qtile bar [top/bottom] or [t/b]",
            metavar="position",
        )

        group = parser.add_argument_group("Terminal options")
        group.add_argument(
            "-k",
            dest="terminal",
            help="Theme to set for Kitty terminal",
            metavar="kitty-theme",
        )
        group.add_argument(
            "-kf",
            dest="terminal_font",
            help="Font to set for Kitty Terminal",
            metavar="kitty-font",
        )
        group.add_argument(
            "-ko",
            dest="terminal_opacity",
            help="Opacity to set for Kitty Terminal",
            metavar="kitty-opacity",
        )

        parser.add_argument(
            "-v",
            "--version",
            action="version",
            version="%(prog)s " + VERSION,
            help="Show the version number",
        )

        args = parser.parse_args()

        qtile = Qtile(user_path)
        kitty = Kitty(user_path)
        menu = Menu(user_path)

        is_action: bool = args.list or args.check
        has_config_options: bool = any(
            [
                args.theme,
                args.position,
                args.terminal,
                args.terminal_font,
                args.terminal_opacity,
            ]
        )

        if is_action and has_config_options:
            parser.error(
                "The flags --list/--check cannot be used with configuration options"
            )

        if args.list:
            menu.menu_themes()
            return
        if args.check:
            menu.check_theme_syntax()
            menu.check_qtile_structure()
            return
        elif has_config_options:
            qtile.set_qtile_theme(args.theme)
            qtile.set_bar_position(args.position)
            kitty.set_terminal_theme(args.terminal)
            kitty.set_terminal_font(args.terminal_font)
            kitty.set_terminal_opacity(args.terminal_opacity)
            return
        else:
            parser.print_help()
            return

    except Exception as e:
        red(f"Unexpected error: {e.with_traceback()}")
