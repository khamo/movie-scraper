#!/bin/bash
echo "Starting scraper"
scrapy runspider cinema_scraper.py -t json --nolog -o - > "movies.json"
echo "Scrape complete, checking movies with imdb"
python check_imdb.py movies.json
