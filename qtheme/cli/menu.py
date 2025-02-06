from os import path, listdir
from qtheme.utils.colors import blue, magenta
import json


class Menu:
    def __init__(self, user_path) -> None:
        self.user_path = user_path

    def menu_themes(self):
        full_path = path.join(
            self.user_path, '.config', 'qtile', 'themes', 'theme_selector.json'
        )
        qtile_themes_path = path.join(
            self.user_path, '.config', 'qtile', 'themes'
        )
        kitty_themes_path = path.join(
            self.user_path, '.config', 'kitty', 'themes'
        )
        kitty_file = path.join(
            self.user_path, '.config', 'kitty', 'kitty.conf'
        )

        qtile_index = 0
        kitty_index = 0

        with open(full_path, 'r') as file:
            cur_theme_qt = json.load(file)
        with open(kitty_file) as file:
            cur_theme_kitty = ""
            lines = file.readlines()
            for index, line in enumerate(lines):
                if line.startswith('#[theme]'):
                    cur_theme_kitty = lines[index + 1] \
                            .split('.')[0] \
                            .split('/')[1]
                    break

        magenta('Available Qtile themes: ')
        for theme in listdir(qtile_themes_path):
            if theme == 'theme_selector.json':
                continue
            qtile_index += 1
            theme_name = theme.split('.')[0]
            maker = (
                lambda text: f'\033[34m{text}*\033[0m'
                if theme_name == cur_theme_qt.get('theme') else text
            )

            blue(f'[{qtile_index}] -> {maker(theme_name)}')
        print('')

        magenta('Available Kitty themes: ')
        for theme in listdir(kitty_themes_path):
            kitty_index += 1
            theme_name = theme.split('.')[0]
            maker = (
                lambda text: f'\033[34m{text}*\033[0m'
                if theme_name == cur_theme_kitty else text
            )

            blue(f'[{kitty_index}] -> {maker(theme_name)}')
