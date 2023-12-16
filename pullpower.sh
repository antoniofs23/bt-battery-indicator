#!/bin/bash

# get devices and battery power
devices=$(upower -d | grep model)
battery=$(upower -d | grep percentage)

echo $devices
echo $battery