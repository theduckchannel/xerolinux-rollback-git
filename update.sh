#!/bin/bash
read -p "Commit message: " COMMITMSG
git add -A
git commit -m "$COMMITMSG"
git push
