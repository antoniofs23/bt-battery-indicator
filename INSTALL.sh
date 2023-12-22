#!/bin/bash
# an install file that:
# 1. creates a terminal alias
# 2. installs python dependencies
# 3. sets app as a start-up process

# 1. Create a terminal alias in .bashrc
echo "alias bt-battery='python3 ~/bt-battery-indicator/main.py &'" >> ~/.bashrc

# 2. Install python dependencies
pip install -r requirements.txt

# 3. set up as start-up process
# get username 
name=$(whoami)
#build the .desktop file
cd ~/.config/autostart/
cat <<EOT >> bt-battery-indicator.desktop
[Desktop Entry]
Type=Application
Path=/home/$name/bt-battery-indicator/
Exec=python3 main.py
Terminal=false
Icon=htop
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_US]=bt-battery-indicator
Comment[en_US]=runs bt-battery-indicator
EOT
