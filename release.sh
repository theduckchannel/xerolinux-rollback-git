#!/bin/bash

OLDVERSION=$(grep '^current_version.*' 'xerolinux-rollback')

echo "Old Version ====> $OLDVERSION"

read -p "Enter with new version: " NEWVERSION

sed -i "s/^pkgver=.*/pkgver=$NEWVERSION/" ../xerolinux-rollback-git-AUR/PKGBUILD
sed -i "s/^current_version.*/current_version='$NEWVERSION'/" xerolinux-rollback

cd ../xerolinux-rollback-git-AUR
makepkg --printsrcinfo > .SRCINFO

echo "Preparing to release $NEWVERSION...."


cd ~/xerolinux-rollback-git

