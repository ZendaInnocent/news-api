# Tanzania News API

News API consisting various sources from Tanzania.

## Fork the project

## Clone the project
```
git clone https://github.com/<username>/news-api.git
```

cd news-api

## Setup to run scraper locally

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
Sites with spiders available for now.

- ITV (https://itv.co.tz)
- Dar24 (https://dar24.com)
- MillardAyo (https://millardayo.com)

### To scrape
```
scrapy crawl <spider-name>
```

Spider names
- ITV - itv
- Dar24 - dar24
- MillardAyo - millardayo


## Setup to run API locally

### Install the required packages

```
cd api
pip install -r requirements.txt
```

### Run API
```
python main.py
```

The project will be available at http://127.0.0.1
