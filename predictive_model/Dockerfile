FROM python:3.8-slim

WORKDIR /code

COPY . .

RUN apt-get update && apt-get install -y libgomp1

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

CMD ["python", "app.py"]
