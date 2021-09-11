#!/bin/bash

OLDVERSION=$(grep '^current_version.*' 'xerolinux-rollback')

echo "Old Version ====> $OLDVERSION"

read -p "Enter with new version: " NEWVERSION

sed -i "s/^pkgver=.*/pkgver=$NEWVERSION/" PKGBUILD
sed -i "s/^current_version.*/current_version=$NEWVERSION/" version.py

echo "Preparing to release $NEWVERSION...."

