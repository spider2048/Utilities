# AutoRunner

A basic, fine, and a **cross-platform** alternative to `entr`.

Runs frequent commands on file saves.

Useful when [entr](https://eradman.com/entrproject/) doesn't work on your platform.

## Usage

```
$ python autorun.py
usage: autorun.py [-h] [-delay DELAY] [-timeout TIMEOUT] [-wd WD] [-clear]
                  command [command ...]
```

Auto compile files on save
```bash
$ echo Code.cpp | python autorun.py make
```

Increase the delay `2s` and set the timeout `5s` and set the cwd to `/Temp` and `clear` the screen 
```bash
$ echo Code.cpp | python autorun.py -delay 2 -timeout 5 -wd /Temp -clear
```

## Help

```text
usage: autorun.py [-h] [-delay DELAY] [-timeout TIMEOUT] [-wd WD] [-clear]
                  command [command ...]

a cross-platform replacement for `entr`

positional arguments:
  command           command to run

options:
  -h, --help        show this help message and exit
  -delay DELAY      delay to wait before polling
  -timeout TIMEOUT  timeout for the command
  -wd WD            working directory for the command
  -clear            clear the screen on change
```