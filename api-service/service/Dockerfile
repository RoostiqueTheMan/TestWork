FROM python:3.8.12

RUN python3.8 -m pip install poetry
RUN poetry config virtualenvs.create false

ENV SERVICE_FOLDER=/service

RUN mkdir $SERVICE_FOLDER

COPY .. $SERVICE_FOLDER

RUN cd $SERVICE_FOLDER && poetry install --only main

WORKDIR $SERVICE_FOLDER

ENTRYPOINT ["python3.8", "main.py"]
