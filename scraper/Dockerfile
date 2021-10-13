FROM python:3.9

WORKDIR /scraper

COPY ./requirements.txt /scraper/

EXPOSE 6800

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /scrapers

CMD ["scrapyd"]
