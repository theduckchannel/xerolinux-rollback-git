#!/bin/bash

OLDVERSION=$(grep '^current_version.*' version.py)

echo "Old Version ====> $OLDVERSION"

read -p "Enter with new version: " NEWVERSION
echo "You entered $NEWVERSION"
