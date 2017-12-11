FROM python:3.5

COPY requeriments.txt /

RUN pip install -r requeriments.txt

COPY . /

CMD [ "python", "-u", "./main.py"]