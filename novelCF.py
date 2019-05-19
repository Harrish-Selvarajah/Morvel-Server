# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 13:42:22 2019

@author: Harrish Selvarajah
"""
from NovelLens import NovelLens
from surprise import KNNBasic
import heapq
from collections import defaultdict
from operator import itemgetter
from bookimgurl import bookimgurl


class novelCF:
    
    def computeNovelCf(userid):
        testSubject = userid
        k = 10

# Load our data set and compute the user similarity matrix
        ml = NovelLens()
        bi = bookimgurl()
        data = ml.loadNovelLensLatestSmall()
        datab = bi.loadurlLensLatestSmall()

        trainSet = data.build_full_trainset()

        sim_options = {'name': 'cosine',
               'user_based': True
               }

        model = KNNBasic(sim_options=sim_options)
        model.fit(trainSet)
        simsMatrix = model.compute_similarities()

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
        noveldatapro = []
        novels = []
        novellinks = []
        for itemID, ratingSum in sorted(candidates.items(), key=itemgetter(1), reverse=True):
    
         if not itemID in watched:
          novelID = trainSet.to_raw_iid(itemID)
          noveldatapro.append(novelID)
          print(ml.getNovelName(int(novelID)), ratingSum)
          novels.append(ml.getNovelName(int(novelID)))
          pos += 1
          if (pos > 9):
            print("The top 10 novels for the user: " + testSubject )
            print(noveldatapro)
            break
        
        lenght = 10
        for i in range(lenght):
            novellinks.append(bi.getNovellink(int(noveldatapro[i])))
            
        print(novellinks)
        
        return novellinks
          


    


    
            



