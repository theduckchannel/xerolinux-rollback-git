#!/bin/bash

PKGNAME="xerolinux-rollback-git"
CURRENT_DIR=$(pwd)
OLDVERSION=$(grep '^current_version.*' 'xerolinux-rollback')
echo "Old Version ====> $OLDVERSION"
read -p "Enter with new version: " NEWVERSION
sed -i "s/^pkgver=.*/pkgver=$NEWVERSION/" ../xerolinux-rollback-git-AUR/PKGBUILD
sed -i "s/^current_version.*/current_version='$NEWVERSION'/" xerolinux-rollback
echo "Preparing to release $NEWVERSION...."
cd ../xerolinux-rollback-git-AUR
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
