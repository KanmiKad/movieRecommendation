import pandas as pd
import numpy as np

udata = pd.read_csv("udata.csv")
uitem = pd.read_csv("uitem.csv")
ratings = pd.merge(udata, uitem)
ratings.head()

movieRatings = ratings.pivot_table(index=['Userid'], columns=['Title'], values='Rating')
movieRatings.head()

#provides the stats for each movie by giving the number of people that rated it(size) and the mean rating(mean)
movieStats = ratings.groupby('Title').agg({'Rating': [np.size, np.mean]})
movieStats.head()

#selecting movies with a rating size greater than 200
popularMovies = movieStats['Rating']['size'] >= 200

#this returns the ratings of just the column with the selected movie ('Star Wars (1977) used as an example)'
selectedMovie = movieRatings['Star Wars (1977)']
selectedMovie.head()

#this finds correlation between the selected movie ratings and other movie ratings
corrMovies = movieRatings.corrwith(selectedMovie)

#drops the NaN values from the correlation calculation
corrMovies = corrMovies.dropna()

#applying the popular movies parameter
similarMovies = movieStats[popularMovies].join(pd.DataFrame(corrMovies, columns=['similarity']))
similarMovies = pd.DataFrame(similarMovies.sort_values(['similarity'], ascending=False))
similarMovies.head()



