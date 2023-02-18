It lists folders (movie_title-year) over samba (Windows share) connection, try to search movies in IMDB,
if it finds it query accross API for determine ratings and genres.

Main file: 
----------
samba_imdb_query.py

Install(Win10):
---------------
https://user-images.githubusercontent.com/8656998/219881856-5e0b8ee0-5024-4a53-b489-5da5067e5329.mp4

```
python -m venv .
 .\Scripts\activate
 pip install -r requirements.txt
 ```

Input folders form on samba share:
----------------------------------
```
movie-name_1   2012
movie-name_2   2014 
movie-name_3   2022
movie-name...  2011 
movie-name_n   2011 

Bloodlust Zombies 2011
Checkmate 1973
Home Run Showdown 2015
The Do-Deca-Pentathlon 2012
```

Output form:
------------
```
Movie name (year) # IMDBMovieName # https://www.imdb.com/title/tt[IMDBMovieID]/# RATING # [RatingNumber] # [Action, Adventure, etc.]

The Do-Deca-Pentathlon         (2012) # The Do-Deca-Pentathlon         # https://www.imdb.com/title/tt0811137/      # RATING # 5.9 # Comedy
Home Run Showdown              (2015) # Home Run Showdown              # https://www.imdb.com/title/tt1680311/      # RATING # 4.9 # Family, Sport
```

Python 3.11.0
