FROM python:3.12-slim

WORKDIR /app

COPY ./backend /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN mkdir -p /app/logs && touch /app/logs/logs.txt && chmod -R 777 /app/logs

EXPOSE 5000

ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]