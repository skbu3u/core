#!/bin/bash
# sudo chmod +x script.sh
clear

echo "update core"
git reset --hard
git pull

echo "check dependencies"
python3 -m poetry update

echo "check database"
FILE="./src/database/sqlite.db"
if test -f "$FILE"; then
  echo "$FILE exist"
else
  python3 -m alembic revision --autogenerate 'Initial'
  python3 -m alembic upgrade head
fi

echo "run server"
FILE="./src/main.py"
if test -f "$FILE"; then
  echo "$FILE exist"
  folder="src"
  # shellcheck disable=SC2164
  cd ${folder}
  python3 main.py
else
  echo "Server not found"
fi
