import random
import time

from soco import SoCo
my_zone = SoCo('192.168.221.25')
print my_zone.player_name

change_to = 11
benIsIdiot = True
seconds = 1

while benIsIdiot:
    print "current volume: " + str(my_zone.volume) + "; Will change to " + \
          str(change_to) + " in " + str(seconds) + " seconds"
    time.sleep(seconds)
    my_zone.volume = change_to
    seconds = random.randint(10, 30)


def change_gradually(change_to_volume):
    if my_zone.volume == change_to_volume:
        return

    add_or_subtract = 1
    if my_zone.volume > change_to_volume:
        add_or_subtract = -1

    while my_zone.volume != change_to_volume:
        time.sleep(1)
        my_zone.volume = my_zone.volume + add_or_subtract
        print "changed to" - str(my_zone.volume)
