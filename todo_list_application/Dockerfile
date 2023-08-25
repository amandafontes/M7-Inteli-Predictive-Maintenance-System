FROM python:3.8-alpine

WORKDIR /frontend_ponderada

COPY requirements.txt requirements.txt
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN python3 -m pip install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

ENV FLASK_APP=app.py
EXPOSE 8080
