# This script will auto-update Visual Studio Code for Chromebook in the terminal when out of date.

wget "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64" -O /tmp/code_latest_amd64.deb

sudo dpkg -i /tmp/code_latest_amd64.deb