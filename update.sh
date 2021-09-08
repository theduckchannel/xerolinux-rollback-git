#!/bin/bash

git config --global user.email "fredcox@gmail.com"
git config --global user.name "theduckchannel"
current_date=$(date +"%d%m%Y%H%M%S")
git add -A
git commit -m "backup current datetime is: $current_date"
git push
