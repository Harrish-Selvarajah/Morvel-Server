# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 13:42:22 2019

@author: Harrish Selvarajah
"""

from moviecdata import moviecdata
from CurrentUserData import CurrentUserData
import math
import numpy as np
from tmdblens import tmdblens


nl = moviecdata()
ml = CurrentUserData() 
tl = tmdblens()       
genres1 = {}
genres2 = {}



sortedlist = []
others = {}
thisRating = 0
otherRating = 0
average = 0


class contentm:

     def computesimilarityscore(self): 
        
        datan = nl.loadMovieLensLatestSmall()+1
        datam = ml.loadCurrentData()+1
        datat = tl.loadtmdbLensLatestSmall()
        genresm = ml.getGenress()
        genresn = nl.getGenress() 
        similarities = np.zeros((datan, datan))
        for thisRating in range(1, datam): #movie
            if (thisRating % 1 == 0):
                print(thisRating, " of ", 10)
            for otherRating in range(1, datan): #novel
                #print('hsere')
                thisMovieID = ml.getMovieID(ml.getMovieName(thisRating))
                otherMovieID = nl.getMovieID(nl.getMovieName(otherRating))
                if otherMovieID == 0:
                    break
                else:
                 genreSimilarity = self.computeGenreSimilarity(thisMovieID, otherMovieID, genresm, genresn)
                 #print(genreSimilarity)
                 similarities[thisRating, otherRating] = genreSimilarity
                 similarities[otherRating, thisRating] = similarities[thisRating, otherRating]
                
        similarityScore=0       
        for x in range(1, thisRating):#iterating through movie
         for y in range(1, otherRating):#iterating through novel
                similarityScore += similarities[x,y]
        

        print('similarity score:', similarityScore)
        average = similarityScore/(otherRating)
        print(average)
        neighbour = {}
        for x in range(1, thisRating):#iterating through movie
         for y in range(1, otherRating):#iterating through novel
          if similarities[x,y] < average:
            score = similarities[x,y]
            neighbour[nl.getMovieName(y)] = score
          else:
            others[x,y] = 0
        
        
        sorted_x = sorted(neighbour.items(),key=lambda x: x[1], reverse=True)
        
        
        for i in sorted_x:
            sortedlist.append(i[0])
        topreco = []
        print(sortedlist)
        for i in range(10):
            topreco.append(sortedlist[i])
            
        toprecoid = []
        for i in range(10):
            toprecoid.append(nl.getMovieID((topreco[i])))
         
        moviestmdb = []     
        for i in range(10):
            moviestmdb.append(tl.gettmdbID(int(toprecoid[i])))
            
        print(moviestmdb)
        return moviestmdb
         
     def computeGenreSimilarity(self, movie, novel, genresm, genresn):
         ml = CurrentUserData()
         nl = moviecdata()
         genresm = ml.getGenress()
         genresn = nl.getGenress()   
         genres1 = genresm[movie]
         genres2 = genresn[novel]
         print("came here")
         print(movie)
         print(novel)
         print(genres1)
         print(genres2)
         print(len(genres2))  
         sumxx, sumxy, sumyy = 0, 0, 0
         for i in range(len(genres1)):
            x = genres1[i]
            y = genres2[i]
            sumxx += x * x
            sumyy += y * y
            sumxy += x * y
            
         if sumyy == 0:
            sumyy = 1
            
         return sumxy/math.sqrt(sumxx*sumyy)
        #return sumyy
     
           
       
    

        
        

    

   
       



  



