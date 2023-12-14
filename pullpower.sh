#!/bin/bash

# get devices and battery power
devices=$(upower -d | grep model)
battery=$(upower -d | grep percentage)

# remove repetitions
# would be easier using xargs sorting but then everything is jumbled up
devices=$(echo "$devices" | awk '{for (i=1;i<=NF;i++) if (!devices[$i]++) printf("%s%s",$i,FS)}{printf("\n")}')
battery=$(echo "$battery" | awk '{for (i=1;i<=NF;i++) if (!battery[$i]++) printf("%s%s",$i,FS)}{printf("\n")}')

# remove the pesky Diplay device %
battery=${battery::-3}