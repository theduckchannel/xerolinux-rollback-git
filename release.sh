#!/bin/bash

PKGNAME="xerolinux-rollback-git"
BINARY="xerolinux-rollback"
CURRENT_DIR=$(pwd)
OLDVERSION=$(grep '^current_version.*' $BINARY)
echo "Old Version ====> $OLDVERSION"
#####
# New Version Dialog
read -p "Enter with new version: " NEWVERSION
sed -i "s/^pkgver=.*/pkgver=$NEWVERSION/" ../"$PKGNAME"-AUR/PKGBUILD
sed -i "s/^current_version.*/current_version='$NEWVERSION'/" xerolinux-rollback
#####
echo "Preparing to release $NEWVERSION on AUR...."
cd ../"$PKGNAME"-AUR
makepkg --printsrcinfo > .SRCINFO
git add -A
git commit -m "release $NEWVERSION"
git push
echo "Everything ok $NEWVERSION released!"
echo "......."
cd $CURRENT_DIR

echo "Updating github repo..."
./update.sh
git tag -a $NEWVERSION -m "release $NEWVERSION"
git push origin $NEWVERSION
