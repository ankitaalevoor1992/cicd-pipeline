FROM python:3.13-alpine3.22

WORKDIR /app

COPY app.py .

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python" , "app.py"]

