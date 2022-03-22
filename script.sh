#!/bin/bash
# sudo chmod +x script.sh
clear

echo "update core"
git pull

echo "check database"
FILE=/src/database/sqlite.db
if test -f "$FILE"; then
  echo "$FILE exist"
else
  python3 -m alembic revision --autogenerate 'Initial'
  python3 -m alembic upgrade head
fi

echo "check dependencies"
python3 -m poetry install

echo "run server"
# shellcheck disable=SC2164
cd src
pytho3 main.py