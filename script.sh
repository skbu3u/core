#!/bin/bash
# sudo chmod +x script.sh
clear
echo ""

echo "==> Update core from Git"
git reset --hard
git fetch
git pull
echo ""

echo "==> Check and update dependencies"
python3 -m poetry update
echo ""

echo "==> Check database and migrations"
FILE="./src/database/sqlite.db"
if test -f "$FILE"; then
  echo "Path: $FILE"
  echo "Database exist and up to date"
else
  python3 -m alembic revision --autogenerate -m 'Initial'
  python3 -m alembic upgrade head
fi
echo ""

echo "==> Run server"
python3 main.py
