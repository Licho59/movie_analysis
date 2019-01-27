#!/usr/local/bin/python3

from collections import namedtuple

from constants_local import OMDB_API_KEY

DB_PATH = 'sqlite:////Users/jakubtlalka/it/ds/projects/movies/movies.sqlite'

IMDB_BASE_URL = 'https://www.imdb.com'

Review = namedtuple('Review', ['movie_url', 'reviewer_type', 'reviewer_name', 'reviewer_url', 'rating', 'text', 'date'])

TYPE_CRITIC = 'critic'
TYPE_USER = 'user'
RT_BASE_URL = "https://www.rottentomatoes.com"

AWARD_WINNER = 'winner'
AWARD_NOMINEE = 'nominee'

IMDB_TYPE_MOVIE = 'title'
IMDB_TYPE_PERSON = 'name'

"""
{'Title': 'Guardians of the Galaxy Vol. 2',
 'Year': '2017',
 'Rated': 'PG-13',
 'Released': '05 May 2017',
 'Runtime': '136 min',
 'Genre': 'Action, Adventure, Comedy, Sci-Fi',
 'Director': 'James Gunn',
 'Writer': 'James Gunn, Dan Abnett (based on the Marvel comics by), Andy Lanning (based on the Marvel comics by), Steve Englehart (Star-Lord created by), Steve Gan (Star-Lord created by), Jim Starlin (Gamora and Drax created by), Stan Lee (Groot created by), Larry Lieber (Groot created by), Jack Kirby (Groot created by), Bill Mantlo (Rocket Raccoon created by), Keith Giffen (Rocket Raccoon created by), Steve Gerber (Howard the Duck created by), Val Mayerik (Howard the Duck created by)',
 'Actors': 'Chris Pratt, Zoe Saldana, Dave Bautista, Vin Diesel',
 'Plot': "The Guardians must fight to keep their newfound family together as they unravel the mystery of Peter Quill's true parentage.",
 'Language': 'English',
 'Country': 'USA',
 'Awards': 'Nominated for 1 Oscar. Another 12 wins & 42 nominations.',
 'Poster': 'https://m.media-amazon.com/images/M/MV5BMTg2MzI1MTg3OF5BMl5BanBnXkFtZTgwNTU3NDA2MTI@._V1_SX300.jpg',
 'Ratings': [{'Source': 'Internet Movie Database', 'Value': '7.7/10'},
  {'Source': 'Rotten Tomatoes', 'Value': '83%'},
  {'Source': 'Metacritic', 'Value': '67/100'}],
 'Metascore': '67',
 'imdbRating': '7.7',
 'imdbVotes': '431,166',
 'imdbID': 'tt3896198',
 'Type': 'movie',
 'tomatoMeter': 'N/A',
 'tomatoImage': 'N/A',
 'tomatoRating': 'N/A',
 'tomatoReviews': 'N/A',
 'tomatoFresh': 'N/A',
 'tomatoRotten': 'N/A',
 'tomatoConsensus': 'N/A',
 'tomatoUserMeter': 'N/A',
 'tomatoUserRating': 'N/A',
 'tomatoUserReviews': 'N/A',
 'tomatoURL': 'http://www.rottentomatoes.com/m/guardians_of_the_galaxy_vol_2/',
 'DVD': '22 Aug 2017',
 'BoxOffice': '$389,804,217',
 'Production': 'Walt Disney Pictures',
 'Website': 'https://marvel.com/guardians',
 'Response': 'True'}"""