#!/bin/bash
# sudo chmod +x script.sh
clear

echo "==> Update core"
git pull

echo "==> Check dependencies"
python3 -m poetry update

echo "==> Check database"
FILE="./src/database/sqlite.db"
if test -f "$FILE"; then
  echo "$FILE exist"
else
  python3 -m alembic revision --autogenerate 'Initial'
  python3 -m alembic upgrade head
fi

echo "==> Run server"
python3 main.py
