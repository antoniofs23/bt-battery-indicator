import os
import signal
import subprocess

# to avoid warnings and code crashes first import gi
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gst', '1.0')
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify


APPINDICATOR_ID = 'myappindicator'

# change the working directory when script is run through command-line
abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)

def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('battery.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    notify.init(APPINDICATOR_ID)
    gtk.main()


def build_menu():
    menu = gtk.Menu()

    item_myapp = gtk.MenuItem('activate')
    item_myapp.connect('activate', myapp)
    menu.append(item_myapp)

    item_quit1 = gtk.MenuItem('quit')
    item_quit1.connect('activate', quit1)
    menu.append(item_quit1)

    menu.show_all()
    return menu


def myapp(_):
    subprocess.call("~/battery-indicator/pullpower.sh", shell=True)
    return myapp


# closes icon <doesnt close app | F10 closes app>
def quit1(_):
    gtk.main_quit()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()