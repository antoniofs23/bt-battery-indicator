from threading import Thread
from collections import OrderedDict
import signal
import gi
import os
import subprocess
import time
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3, GObject

# change the working directory when script is run through command-line
abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)


class Indicator():
    def __init__(self):
        self.app = 'bt-battery-indicator'
        iconpath = os.path.abspath('battery.svg')
        self.indicator = AppIndicator3.Indicator.new(
            self.app, iconpath, AppIndicator3.IndicatorCategory.OTHER)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.create_menu())
        # self.indicator.set_label(" ", self.app)
        # add thread
        self.update = Thread(target=self.update_battery_status)
        # daemonize thread to make indicator stopable
        self.update.setDaemon(True)
        self.update.start()

    def create_menu(self):
        menu = Gtk.Menu()

        dev, perc = subprocess.getoutput("./pullpower.sh").split('\n')
        
        #split by device
        dev = dev.split("model:")
        dev.pop(0) # remove empty space
        #split by percent
        perc = perc.split("percentage:")
        perc.pop(0); perc.pop() # remove display devices in my case..
        
        # acount for the fact that device sometimes show up twice ....
        keep = OrderedDict((device, dev.index(device)) for device in dev)
        keepIdx=list(keep.values()) 
        # define kept device models and battery percentage
        model,battery=[],[]
        for idx in keepIdx:
            model.append(dev[idx])
            battery.append(perc[idx])
        
        # add devices + battery%s 
        for num in range(len(model)):
            item_model = Gtk.MenuItem(model[num]+": "+battery[num])
            menu.append(item_model)
            
            
        # add a separator between devices and quit button
        menu_sep = Gtk.SeparatorMenuItem()
        menu.append(menu_sep)
        
        # quit button
        item_quit1 = Gtk.MenuItem('quit')
        item_quit1.connect('activate', self.stop)

        menu.append(item_quit1)
        menu.show_all()
        return menu

    def stop(self, source):
        Gtk.main_quit()

    def update_battery_status(self):
        while True:
            time.sleep(300)  # updates every 5 minutes
            # apply interface update
            GObject.idle_add(
                self.indicator.set_menu,
                self.create_menu(),
                priority=GObject.PRIORITY_DEFAULT
            )


Indicator()
GObject.threads_init()
signal.signal(signal.SIGINT, signal.SIG_DFL)
Gtk.main()
