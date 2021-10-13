# Tanzania News API

News API consisting various sources from Tanzania.

## Fork the project

## Clone the project
```
git clone https://github.com/<username>/news-api.git
```

cd news-api

## Setup to run locally

### Create virtual environment
```
py -m venv .venv
```

### Activate virtual environment
- Windows
```
.venv/scripts/activate
```

- Bash
```
source .venv/bin/activate
```

### Install required packages
Make sure you are in the right directory.
- cd scraper

```
pip install -r requirements.txt
```

### Setup a MongoDB and provide a connection string
```
# .env

MONGO_DETAILS=mongodb://127.0.0.1:12707
```

## Scrawl a particular website
ITV and Dar24 are sites with spiders available for now.

### To scrape
```
scrapy crawl <spider-name>
```

Spider names
- ITV - itv
- Dar24 - dar24
