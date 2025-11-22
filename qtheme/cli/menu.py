from os import path, listdir
from ..utils.colors import blue, magenta, green, red
from ..utils.schemas import ThemeSelector, Theme
from pydantic import ValidationError
import json


class Menu:
    def __init__(self, user_path: str) -> None:
        self.user_path = user_path

    def menu_themes(self):
        theme_selector_path = path.join(
            self.user_path, ".config", "qtile", "themes", "theme_selector.json"
        )
        qtile_themes_path = path.join(self.user_path, ".config", "qtile", "themes")
        kitty_themes_path = path.join(self.user_path, ".config", "kitty", "themes")
        kitty_file = path.join(self.user_path, ".config", "kitty", "kitty.conf")

        qtile_index = 0
        kitty_index = 0

        with open(theme_selector_path, "r") as file:
            cur_theme_qt = ThemeSelector(**json.load(file))

        with open(kitty_file) as file:
            cur_theme_kitty = ""
            lines = file.readlines()
            for index, line in enumerate(lines):
                if line.startswith("#[theme]"):
                    cur_theme_kitty = lines[index + 1].split(".")[0].split("/")[1]
                    break

        magenta("Available Qtile themes: ")
        for theme in listdir(qtile_themes_path):
            if theme == "theme_selector.json":
                continue
            qtile_index += 1
            theme_name = theme.split(".")[0]

            def maker(text: str):
                return (
                    f"\033[34m{text}*\033[0m"
                    if theme_name == cur_theme_qt.theme
                    else text
                )

            blue(f"[{qtile_index}] -> {maker(theme_name)}")
        print("")

        magenta("Available Kitty themes: ")
        for theme in listdir(kitty_themes_path):
            kitty_index += 1
            theme_name = theme.split(".")[0]

            def maker(text: str):
                return (
                    f"\033[34m{text}*\033[0m" if theme_name == cur_theme_kitty else text
                )

            blue(f"[{kitty_index}] -> {maker(theme_name)}")

    def check_theme_syntax(self):
        try:
            qtile_themes_path = path.join(self.user_path, ".config", "qtile", "themes")

            for theme in listdir(qtile_themes_path):
                if theme == "theme_selector.json":
                    with open(path.join(qtile_themes_path, theme), "r") as file:
                        data = json.load(file)
                        ThemeSelector.model_validate(data)
                    continue

                with open(path.join(qtile_themes_path, theme), "r") as file:
                    data = json.load(file)
                    Theme.model_validate(data)

            green("All themes have correct syntax.")
        except ValidationError as e:
            red("Error in theme syntax:")
            for error in e.errors():
                red(f" - {error['loc']} in file '{theme}'")

    def check_qtile_structure(self):
        try:
            qtile_base_path = path.join(self.user_path, ".config", "qtile")
            qtile_settings_path = path.join(qtile_base_path, "settings")
            qtile_dir_struct = [
                "themes",
                "settings",
                "autostart.sh",
                "config.py",
            ]
            qtile_settings_struct = [
                "groups.py",
                "keys.py",
                "layouts.py",
                "mouse.py",
                "screens.py",
                "widgets.py",
            ]

            if not path.exists(qtile_base_path):
                raise FileNotFoundError("The qtile base directory does not exist.")

            for item in qtile_dir_struct:
                if not path.exists(path.join(qtile_base_path, item)):
                    raise FileNotFoundError(
                        f"The item '{item}' is missing in qtile base directory."
                    )

            for item in qtile_settings_struct:
                if not path.exists(path.join(qtile_settings_path, item)):
                    raise FileNotFoundError(
                        f"The item '{item}' is missing in qtile settings directory."
                    )

            with open(path.join(qtile_base_path, "config.py"), "r") as file:
                file.readline()
                qtheme_header = file.readline()
                if "QTHEME CONFIGURATION" not in qtheme_header:
                    raise ValueError(
                        "The 'config.py' file does not correspond to the format supported by qtheme."
                    )

            for item in qtile_settings_struct:
                with open(path.join(qtile_settings_path, item), "r") as file:
                    file.readline()
                    qtheme_header = file.readline()
                    if "QTHEME CONFIGURATION" not in qtheme_header:
                        raise ValueError(
                            f"The file '{item}' does not correspond to the format supported by qtheme."
                        )

            green("Qtile base directory structure is correct.")
        except FileNotFoundError as e:
            red(f"Error: {e}")
        except ValueError as e:
            red(f"Error: {e}")
        except Exception as e:
            red(f"Unexpected error: {e}")
