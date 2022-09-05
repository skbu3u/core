# The Core
Main logic of application

## Docker
    For deploying backend part in docker container, follow next steps:
    - docker build -t core-api . 
    - docker run -d -p 8000:8000 --env HOST=0.0.0.0 --env PORT=8000 --name core-api core-api

    Be carefully, docker container always install dependencies by poetry avoiding poetry.lock