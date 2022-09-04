FROM python:3.10
RUN mkdir /app
RUN mkdir /app/src

COPY /src /app/src
COPY main.py /app
COPY cfg.py /app
COPY pyproject.toml /app
COPY alembic.ini /app
EXPOSE 8000

WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

RUN python3 -m alembic revision --autogenerate -m 'Initial'
RUN python3 -m alembic upgrade head
CMD ["python3", "main.py"]
