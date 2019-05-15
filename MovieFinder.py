# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:27:52 2019

@author: Harrish Selvarajah
"""

from MovieData import MovieData

class MovieFinder:
    
 ml = MovieData()
 datan = ml.loadMovieLensLatestSmall()

 movies = []
 moviesfound=[]

 def computesimilarmovie(self, search):
     
     print(self.ml.name_to_movieID[1])

# =============================================================================
#     for i in range(1,34):
#         print(self.movies)
#         self.movies.append(self.ml.movieID_to_name[i])
#     
#     
# 
#     for i in (name for name in self.movies if name.startswith(search)):
#      self.moviesfound.append(i.title())
#     
#     return self.moviesfound
#     
# =============================================================================
