# QTHEME


![preview](https://raw.githubusercontent.com/jsusmachaca/qtheme/master/preview/bars.png)
![preview](https://raw.githubusercontent.com/jsusmachaca/qtheme/master/preview/term.png)

# Installation

```sh
git clone https://github.com/jsusmachaca/qtheme.git
cd qtheme
```

In Arch Linux
```sh
makepkg -si
```

In other distros
```sh
python setup.py build
python setup.py install
```

# Aplication

## Qtile
To list available themes for qtile and kitty
```sh
qtheme -ls
```
Output:

![preview](https://raw.githubusercontent.com/jsusmachaca/qtheme/master/preview/list.png)

To change the qtile theme
```sh
qtheme --theme [theme]
```

To change the position of the bar
```sh
qtheme --position [top/bottom]
```

You can put the parameters together
```sh
qtheme -t nord -p t
```

## Kitty

To change the terminal theme
```sh
qtheme --terminal [theme]
```

To change the opacity
```sh
qtheme --terminal-opacity [opacity-value]
```

To change the terminal font family
```sh
qtheme --terminal-font [font-family]
```

## Qtile + Kitty

You can use the parameters together
```sh
qtheme -t onedark -To 0.80 -kf "UbuntuMono Nerd Font"
```

You can also use the qtile and kitty parameters
```sh
qtheme -t forest -p b -k onedark -ko 1 -kf "Hack Nerd Font"
