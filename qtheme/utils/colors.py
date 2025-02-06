def red(text):
    print(f'\033[31m{text}\033[00m')


def yelow(text):
    print(f'\033[33m{text}\033[00m')


def green(text):
    print(f'\033[32m{text}\033[00m')


def blue(text):
    print(f'\033[36m{text}\033[00m')


def magenta(text):
    print(f'\033[35m{text}\033[00m')


def imagenta(text):
    return input(f'\033[35m{text}\033[00m').strip()
