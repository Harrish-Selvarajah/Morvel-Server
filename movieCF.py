# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 13:42:22 2019

@author: Harrish Selvarajah
"""
import csv
import pickle
from MovieLens import MovieLens
from surprise import KNNBasic
import heapq
from collections import defaultdict
from operator import itemgetter
from tmdblens import tmdblens


class movieCF:
    
    def __init__(self):
        self.filename = ""
        
    def computeMovieCf(self, userid ):
        testSubject = userid
        k = 10

# Load our data set and compute the user similarity matrix
        ml = MovieLens()
        tl = tmdblens()
        data = ml.loadMovieLensLatestSmall()
        datat = tl.loadtmdbLensLatestSmall()

        trainSet = data.build_full_trainset()
        print(datat)

        sim_options = {'name': 'cosine',
               'user_based': True
               }

        model = KNNBasic(sim_options=sim_options)
        model.fit(trainSet)
        simsMatrix = model.compute_similarities()
        
        with open('model.pkl', 'wb') as handle:
            pickle.dump(model, handle, pickle.HIGHEST_PROTOCOL)

# Get top N similar users to our test subject
# (Alternate approach would be to select users up to some similarity threshold - try it!)
        testUserInnerID = trainSet.to_inner_uid(testSubject)
        similarityRow = simsMatrix[testUserInnerID]

        similarUsers = []
        for innerID, score in enumerate(similarityRow):
         if (innerID != testUserInnerID):
          similarUsers.append( (innerID, score) )

        kNeighbors = heapq.nlargest(k, similarUsers, key=lambda t: t[1])

# Get the stuff they rated, and add up ratings for each item, weighted by user similarity
        candidates = defaultdict(float)
        for similarUser in kNeighbors:
         innerID = similarUser[0]
         userSimilarityScore = similarUser[1]
         theirRatings = trainSet.ur[innerID]
        for rating in theirRatings:
         candidates[rating[0]] += (rating[1] / 5.0) * userSimilarityScore
    
# Build a dictionary of stuff the user has already seen
        watched = {}
        for itemID, rating in trainSet.ur[testUserInnerID]:
          watched[itemID] = 1
    
# Get top-rated items from similar users:
        pos = 0
        moviedatapro = []
        movies = []
        moviestmdb = []
        for itemID, ratingSum in sorted(candidates.items(), key=itemgetter(1), reverse=True):
    
         if not itemID in watched:
          movieID = trainSet.to_raw_iid(itemID)
          moviedatapro.append(movieID)
          print(ml.getMovieName(int(movieID)), ratingSum)
          movies.append(ml.getMovieName(int(movieID)))
          pos += 1
          if (pos > 9):
            print("The top 10 movies for the user: " + testSubject )
            
            print( moviedatapro)
            break
       
        self.createFile(testSubject, ml, moviedatapro )
        lenght = len(moviedatapro)
        for i in range(lenght):
            moviestmdb.append(tl.gettmdbID(int(moviedatapro[i])))
            
        print(moviestmdb)  
        return moviestmdb
    
    def createFile(self, testSubject, ml, moviedatapro):
        filename = "currentuser.csv"
        with open(filename, 'w', newline='') as csvfile:
             filewriter = csv.writer(csvfile
                            )  
             filewriter.writerow(['ID', 'Name', 'Genres'])
             i = 0
             while i <= 9:
              x = moviedatapro[i]
              filewriter.writerow([i+1, ml.getMovieName(int(x)), ml.getGenres(int(x))])
              i += 1
            
            
            
            
            
            
            


    


    
            



