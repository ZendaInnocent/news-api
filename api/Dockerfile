FROM python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /news_api

COPY requirements.txt /news_api/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /news_api

CMD ["python", "main.py"]
