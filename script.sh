#!/bin/bash
# sudo chmod +x script.sh
clear

echo "==> Update core from Git"
git pull

echo "==> Check and update dependencies"
python3 -m poetry update

echo "==> Check database and migrations"
FILE="./src/database/sqlite.db"
if test -f "$FILE"; then
  echo "$FILE exist"
else
  python3 -m alembic revision --autogenerate -m 'Initial'
  python3 -m alembic upgrade head
fi

echo "==> Run server"
python3 main.py
