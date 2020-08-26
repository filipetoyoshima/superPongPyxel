# Super Pong!

This game is supposed to be a version of the classic game Pong.
It was built using [Pyxel](https://github.com/kitao/pyxel), and, actually, this repository is more like experimentation of Pyxel features.

It is a work in progress, so I won't write the rules cause they may change according to some crazy ideas of mine.

## Build Instructions

### Pyxel

First, give a look at [Pyxel requirements](https://github.com/kitao/pyxel#how-to-install), and install'em all. Just look for your operating system instructions and follow them.

### :arrow_down: Download

Get the code! Clone this repository:

```bash
# Clone the repository
git clone https://github.com/filipetoyoshima/superPongPyxel.git

# Go to the directory
cd superPongPyxel
```

### :ballot_box_with_check: Enviroment (Optional, but recommended)

First of all, I strongly recommend you to set up a venv to run this project. If you don't know what is it, then I recommend you to [read about it](https://docs.python.org/3/library/venv.html). Don't forget that the **Python version** must be compatible with Pyxel.

```bash
# You must install venv first
python3 -m venv env
```

### :heavy_check_mark: Install Requirements

Once you have all of the Pyxel things checked, then install the project requirements which is... pretty much just what Pyxel demands. All of it is in the `requirements.txt`, which can be consumed by pip.

> You do not have pip installed yet? [Install it here](https://pip.pypa.io/en/stable/installing/).
>
> If you use Linux, I recommend [install by your official package manager](https://packaging.python.org/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers). If not, I recommend using :wink:

```bash
pip3 install -r requirements.txt
```

### :runner: Run

Then you are ready to go. Just run the `main.py` and see what this game can do for you! (Well... not pretty much yet...)

```
python3 main.py
```