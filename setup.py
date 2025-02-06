from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()

setup(
    name="qtheme",
    version="2.0.4",
    description="Tools for management qtile environment",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Jesus Machaca",
    author_email="falcorgd@gmail.com",
    url="https://github.com/loadept/qtheme",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Terminals :: Terminal Emulators/X Terminals"
    ],
    license="MIT",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "qtheme = qtheme.main:main"
        ]
    },
)
