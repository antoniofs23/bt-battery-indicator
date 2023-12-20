# Intro
a simple linux panel app that outputs the battery percent of connected bluetooth devices. 

# installation
clone this repo to your home directory via:

`git clone https://github.com/antoniofs23/bt-battery-indicator.git`

### dependencies
the app requires `upower` which should already be installed in your system.

For python dependencies you can run the `pip install -r requirements.txt` command 

### running the app

To run via your terminal you can create an alias in your `.bashrc`:

`alias bt-battery='python3 ~/bt-battery-indicator/run.py &'`

dont forget to `source .bashrc` after making the change

### Running on startup
To run the app automatically on startup do the following:
1. create a `bt-battery-indicator.desktop` file in your `.config/autostart` directory
2. Paste the following in `bt-battery-indicator.desktop` (make sure to replace path with your username)
```
[Desktop Entry]
Type=Application
Path=/home/your_username/bt-battery-indicator/
Exec=python3 run.py
Terminal=false
Icon=htop
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_US]=bt-battery-indicator
Comment[en_US]=runs bt-battery-indicator
```
to make sure that it works you can then run `gio launch bt-battery-indicator.desktop` or just log-in and out
