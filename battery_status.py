from psutil import sensors_battery
from win10toast import ToastNotifier
from time import sleep
import keyboard
import sys

toast = ToastNotifier()
charging_toast = 0
uncharged_toast = 0
in80charged_toast = 0
fullycharged_toast = 0
running = 1

def flip():
    global running
    running = not running

keyboard.add_hotkey('ctrl+shift+alt+o', flip)

while running:
    battery = sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    if plugged and percent == '80' and charging_toast == 1 and in80charged_toast == 0:
        charging_toast = 0
        uncharged_toast = 0
        in80charged_toast = 1
        fullycharged_toast = 0
        toast.show_toast('Charging Status🔌', 'Laptop is still charging. Current charge: ' + percent + '%', sys.executable, 10)
        print(charging_toast, uncharged_toast, in80charged_toast, fullycharged_toast)
    if plugged and percent != '100' and charging_toast == 0 and in80charged_toast == 0:
        charging_toast = 1
        uncharged_toast = 0
        in80charged_toast = 0
        fullycharged_toast = 0
        toast.show_toast('Charging Status🔌', 'Laptop is now charging. Current charge: ' + percent + '%', sys.executable, 10)
        print(charging_toast, uncharged_toast, in80charged_toast, fullycharged_toast)
    if not plugged and percent != '100' and uncharged_toast == 0:
        charging_toast = 0
        uncharged_toast = 1
        in80charged_toast = 0
        fullycharged_toast = 0
        toast.show_toast('Charging Status🔌', 'Laptop is uncharged. Current charge: ' + percent + '%', sys.executable, 10)
        print(charging_toast, uncharged_toast, in80charged_toast, fullycharged_toast)
    if plugged and percent == '100' and fullycharged_toast == 0:
        charging_toast = 0
        uncharged_toast = 0
        in80charged_toast = 0
        fullycharged_toast = 1
        toast.show_toast('Charging Status🔋', 'Fully charged! Unplug your laptop.', sys.executable, 10)
        print(charging_toast, uncharged_toast, in80charged_toast, fullycharged_toast)
    sleep(1)
    
