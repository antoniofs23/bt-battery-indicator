[![Python application](https://github.com/antoniofs23/bt-battery-indicator/actions/workflows/python-app.yml/badge.svg)](https://github.com/antoniofs23/bt-battery-indicator/actions/workflows/python-app.yml)

# Quick Intro
a simple linux panel app that outputs the battery percent of connected bluetooth devices. 

![Screenshot from 2023-12-28 17-20-47](https://github.com/antoniofs23/bt-battery-indicator/assets/39067846/81287b34-f49e-47ef-8335-b8e957e554fb)

 usage:
 
- the `manual refresh` bypasses the default 5min refresh -- useful if you just added a new device

 - the `add device` opens up bt setting on GNOME, it can easily be set up to work on your DE of choice by changing line `99` on `main.py`


## Installation

1. clone this repo to your home directory via:
    `git clone https://github.com/antoniofs23/bt-battery-indicator.git`
2. In app directory run the `INSTALL.sh` file (first make it executable via `chmod +x INSTALL.sh`)

>
>[!NOTE]
>*the install file assumes python is already installed (which it normally is)* if not python3 is required prior to running `INSTALL.sh`. To quickly check if python is installed run `python -V` in your terminal

## running the app
The app should auto-start on login.
However, it can also be run through the `bt-battery` terminal command

