# CP Templates

> Sp1d3R | 2023-2024

A collection of templates for use in competitive programming (CP).

## Usage | Code.py

Totally compatible with every text editor.
Totally cross-platform.

First, get the requirements:

```bash
pip install watchdog pyperclip
```

Next, set the environment variable `LOCAL` to a non-null value.

```bash
> $env:LOCAL = $true # powershell
$ export LOCAL=1     # bash
```

Copy `Code.py`, `local.so` (or `local.pyd` for windows) to your directory.
Make a new file `input.txt` - this will be the `stdin` for your program (to pass testcases).

The pre-built libraries are for a little speed boost to your program.

Run the script - **before** writing any code:

```bash
python Code.py
```

Now, you may notice, the file runs automatically whenever the code is saved and copies the file contents to the clipboard.
You may submit the same file in any platform (Codechef, Codeforces, ...) and the code would run as expected.


On windows, the program doesn't respond to `Ctrl+C`.
To make it work, use my other utility: [ForceControlC](https://github.com/spider2048/Utilities/tree/main/ForceControlC).

```bash
ForceControlC python Code.py
```

Now, `Ctrl+C` will terminate the program.

## Building libraries

The files `build/local.py` (or `build_windows/local.py` for Windows) were built using Makefiles or Meson.

You would need a C/C++ compiler to build them on your side.

**I do not guarantee the pre-built files to work on your PC**

#### Linux

To build `local.so` for Linux:

```bash
cd build
make
```

#### Windows

To build `local.pyd` for Windows:

```bash
cd build_windows
cython local.py -3 -o local.c
meson setup build --buildtype release
ninja -C build
```

## Misc

> MULTIPLE_TESTS = True/False

This variable tries to avoid an outer loop in the `main()` function.
You will need to set this variable if problems give multiple test cases in one run.
