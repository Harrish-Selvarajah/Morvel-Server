# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 21:33:12 2019

@author: Harrish Selvarajah
"""
import csv
from collections import defaultdict

from surprise import Dataset
from surprise import Reader 

class NovelLens:
 
    ratingsDataset = 0
    novelID_to_name = {}
    name_to_novelID = {}
    novelID_to_genres = {}
    
    ratingsPath = r'./ratings1.csv'
    novelPath = r'./books.csv'
    
    def loadNovelLensLatestSmall(self):

        ratingsDataset = 0
        self.novelID_to_name = {}
        self.name_to_novelID = {}
        self.novelID_to_genres = {}

        reader = Reader(line_format='user item rating timestamp', sep=',', skip_lines=1)

        ratingsDataset = Dataset.load_from_file(self.ratingsPath, reader=reader)

        with open(self.novelPath, newline='', encoding='ISO-8859-1') as csvfile:
                novelReader = csv.reader(csvfile)
                next(novelReader)  #Skip header line
                for row in novelReader:
                    novelID = int(row[0])
                    novelName = row[1]
                    self.novelID_to_name[novelID] = novelName
                    self.name_to_novelID[novelName] = novelID
                    
        return ratingsDataset
    
    def getGenress(self):
        genres = defaultdict(list)
        genreIDs = {}
        maxGenreID = 0
        with open(self.novelPath, newline='', encoding='ISO-8859-1') as csvfile:
            novelReader = csv.reader(csvfile)
            next(novelReader)  #Skip header line
            for row in novelReader:
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
