# CP Templates

> Licensed under GNU GPL v3

> Sp1d3R | 2023-2024

A collection of templates for use in competitive programming (CP).

## Usage | Code.py

Totally compatible with every text editor.
Totally cross-platform.

First, get the requirements:

```
pip install watchdog pyperclip
```

Next, set the environment variable `LOCAL` to a non-null value.

```
> $env:LOCAL = $true # powershell
$ export LOCAL=1     # bash
```

Copy `Code.py` to your directory.
Make a new file `input.txt` - this will be the `stdin` for your program (to pass testcases).


Run the script - **before** writing any code:

```
$ python Code.py
```

Now, you may notice, the file runs automatically whenever the code is saved and copies the file contents to the clipboard.
You may submit the same file in any platform (Codechef, Codeforces, ...) and the code would run as expected.


On windows, the program doesn't respond to `Ctrl+C`.
To make it work, use my other utility: [ForceControlC](https://github.com/spider2048/Utilities/tree/main/ForceControlC).

```bash
$ ForceControlC python Code.py
```

Now, `Ctrl+C` will terminate the program.

## Misc

> MULTIPLE_TESTS = True/False

This variable tries to avoid an outer loop in the `main()` function.
You will need to set this variable if problems give multiple test cases in one run.
