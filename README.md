# Movie Scraper

Showcase for how to scrape your local cinema website and email yourself when
it is showing movies that have an imdb rating above a certain score.

## Files

* **README.md** - the file you are reading.
* **run.sh** - a bash shell script which helps us run the program.
* **odeon_spider.py** - contains the Scrapy spider which retrieves the movie names.
* **check_imdb.py** - contains a Python script which reads the found movie names, checks them on imdb and sends an email if any were found with a high enough rating.
* **requirements.txt** - this is a Python file which holds our depdencies. These are applications we rely on (Scrapy, sendgrid wrapper, imdb wrapper).

# Running

```bash
$ pip install -r requirements.txt
$ ./run.sh
```

