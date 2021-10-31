
Debian
====================
This directory contains files used to package bitscoind/bitscoin-qt
for Debian-based Linux systems. If you compile bitscoind/bitscoin-qt yourself, there are some useful files here.

## bitscoin: URI support ##


bitscoin-qt.desktop  (Gnome / Open Desktop)
To install:

	sudo desktop-file-install bitscoin-qt.desktop
	sudo update-desktop-database

If you build yourself, you will either need to modify the paths in
the .desktop file or copy or symlink your bitscoin-qt binary to `/usr/bin`
and the `../../share/pixmaps/bitscoin128.png` to `/usr/share/pixmaps`

bitscoin-qt.protocol (KDE)

