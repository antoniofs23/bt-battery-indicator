[![Python application](https://github.com/antoniofs23/bt-battery-indicator/actions/workflows/python-app.yml/badge.svg)](https://github.com/antoniofs23/bt-battery-indicator/actions/workflows/python-app.yml)

# Quick Intro
a simple linux panel app that outputs the battery percent of connected bluetooth devices. 

![Screenshot from 2023-12-28 17-20-47](https://github.com/antoniofs23/bt-battery-indicator/assets/39067846/81287b34-f49e-47ef-8335-b8e957e554fb)

## Installation

1. clone this repo to your home directory via:
    `git clone https://github.com/antoniofs23/bt-battery-indicator.git`
2. In app directory run the `INSTALL.sh` file

*the install file assumes python is already installed (which it normally is)* if not python3 is required prior to running `INSTALL.sh`. To quickly check if python is installed run `python -V` in your terminal

### running the app
The app should auto-start on login.
However, it can also be run through the `bt-battery` terminal command

>> `updated 12/28/23`
    >> (+) `manual refresh` option if you dont want to wait 5min for app to refresh when you add a new device
    >> (+) `add device` option that brings up the add bt device window in `gnome` settings
