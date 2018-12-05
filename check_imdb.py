import json
import sys

import imdb
import sendgrid

NOTIFY_ABOVE_RATING = 7.5

SENDGRID_API_KEY = "API KEY GOES HERE"


def run_checker(scraped_movies):
    imdb_conn = imdb.IMDb()
    good_movies = []
    for scraped_movie in scraped_movies:
        imdb_movie = get_imdb_movie(imdb_conn, scraped_movie['name'])
        if imdb_movie['rating'] > NOTIFY_ABOVE_RATING:
            good_movies.append(imdb_movie)
    if good_movies:
        send_email(good_movies)


def get_imdb_movie(imdb_conn, movie_name):
    results = imdb_conn.search_movie(movie_name)
    movie = results[0]
    imdb_conn.update(movie)
    print("{title} => {rating}".format(**movie))
    return movie


def send_email(movies):
    sendgrid_client = sendgrid.SendGridClient(SENDGRID_API_KEY)
    message = sendgrid.Mail()
    message.add_to("trevor@example.com")
    message.set_from("no-reply@example.com")
    message.set_subject("Highly rated movies of the day")
    body = "High rated today:<br><br>"
    for movie in movies:
        body += "{title} => {rating}".format(**movie)
    message.set_html(body)
    sendgrid_client.send(message)
    print("Sent email with {} movie(s).".format(len(movies)))


if __name__ == '__main__':
    movies_json_file = sys.argv[1]
    with open(movies_json_file) as scraped_movies_file:
        movies = json.loads(scraped_movies_file.read())
    run_checker(movies)
