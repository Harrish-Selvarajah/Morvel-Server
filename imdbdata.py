# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 03:41:06 2019

@author: Harrish Selvarajah
"""

from imdb import IMDb

# create an instance of the IMDb class
ia = IMDb()

# get a movie
movie = ia.get_movie('1')

# =============================================================================
# # print the names of the directors of the movie
# print('Directors:')
# for director in movie['directors']:
#     print(director['name'])
# 
# # print the genres of the movie
# print('Genres:')
# for genre in movie['genres']:
#     print(genre)
# 
# # search for a person name
# people = ia.search_person('Mel Gibson')
# for person in people:
#    print(person.personID, person['name'])
# =============================================================================
   
print(movie['title'])