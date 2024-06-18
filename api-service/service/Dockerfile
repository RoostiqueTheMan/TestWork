FROM python:3.8.12

ENV SERVICE_FOLDER=/service

RUN mkdir $SERVICE_FOLDER

COPY .. $SERVICE_FOLDER

RUN cd $SERVICE_FOLDER && pip install -r requirements.txt

WORKDIR $SERVICE_FOLDER

ENTRYPOINT ["python3.8", "main.py"]
