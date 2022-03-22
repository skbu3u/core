#!/bin/bash
# sudo chmod +x script.sh
clear

echo "try to update"
git remote update
count=$(git rev-list HEAD...origin/fast-api --count)
if [ "$count" -gt "0" ]
then
  echo -e "\e[31m"
  read -r -p  "Update [y/n] " answer
  echo -e "\e[39m"
  if [ "$answer" = "y" ]
  then
    git fetch --all
    git reset --hard origin/master
  fi
fi

echo "check database"
FILE=/src/database/sqlite.db
if test -f "$FILE"; then
  echo "$FILE exist"
else
  echo python3 -m alembic revision --autogenerate 'Initial'
  echo python3 -m alembic upgrade head
fi

echo "check dependencies"
echo python3 -m poetry install

echo "run server"
# shellcheck disable=SC2164
cd src
echo pytho3 main.py