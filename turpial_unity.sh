#!/bin/bash

# Author: Andrea Stagi (4ndreaSt4gi)
# Description: launches Turpial in Ubuntu with Unity support
# License: GPL v3

sudo chmod +x ./turpial/ui/unity/daemon.py
./turpial/ui/unity/daemon.py start
turpial
./turpial/ui/unity/daemon.py stop
