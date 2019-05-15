# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 21:33:12 2019

@author: Harrish Selvarajah
"""
import os
import csv
import sys
from collections import defaultdict

class Noveldata:

    novelID_to_name = {}
    name_to_novelID = {}
    novelID_to_genres = {}
    
    novelPath = './data/novel-data/NovelLens.csv'
    
    def loadNovelLensLatestSmall(self):

        # Look for files relative to the directory we are running from
        #os.chdir(os.path.dirname(sys.argv[0]))

        
        self.novelID_to_name = {}
        self.novelName_to_novelID = {}
        self.novelID_to_genres = {}        

        with open(self.novelPath, newline='', encoding='ISO-8859-1') as csvfile:
                novelReader = csv.reader(csvfile)
                next(novelReader)  #Skip header line
                for row in novelReader:
                    novelID = int(row[0])
                    novelName = row[3]
                    genres = row[4]
                    self.novelID_to_name[novelID] = novelName
                    self.novelName_to_novelID[novelName] = novelID
                    self.novelID_to_genres[novelID] = genres
                    lenght = len(self.novelID_to_name)
                   
                    
        return lenght
    
    def getGenress(self):
        genres = defaultdict(list)
        genreIDs = {}
        maxGenreID = 0
        with open(self.novelPath, newline='', encoding='ISO-8859-1') as csvfile:
            movieReader = csv.reader(csvfile)
            next(movieReader)  #Skip header line
            for row in movieReader:
                novelID = int(row[0])
                genreList = row[4].split('|')
                genreIDList = []
                for genre in genreList:
                    if genre in genreIDs:
                        genreID = genreIDs[genre]
                    else:
                        genreID = maxGenreID
                        genreIDs[genre] = genreID
                        maxGenreID += 1
                    genreIDList.append(genreID)
                genres[novelID] = genreIDList
        # Convert integer-encoded genre lists to bitfields that we can treat as vectors
        for (novelID, genreIDList) in genres.items():
            bitfield = [0] * maxGenreID
            for genreID in genreIDList:
                bitfield[genreID] = 1
            genres[novelID] = bitfield            
        
        return genres

    
    def getNovelName(self, novelID):
        if novelID in self.novelID_to_name:
            return self.novelID_to_name[novelID]
        else:
            return ""
        
    def getNovelID(self, novelName):
        if novelName in self.novelName_to_novelID:
            return self.novelName_to_novelID[novelName]
        else:
            return 0
        
    def getGenres(self, novelID):
        if novelID in self.novelID_to_genres:
            return self.novelID_to_genres[novelID]
        else:
            return "Genre Missing"