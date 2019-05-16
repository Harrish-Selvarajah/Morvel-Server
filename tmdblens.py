import os
import csv
import sys



class tmdblens:

    movieID_to_tmdbid = {}
   
    linksPath = './links.csv'
    
    
    def loadtmdbLensLatestSmall(self):

        # Look for files relative to the directory we are running from
        os.chdir(os.path.dirname(sys.argv[0]))
        ratingsDataset = 0
        self.movieID_to_tmdbid = {}
      
        with open(self.linksPath, newline='', encoding='ISO-8859-1') as csvfile:
                movieReader = csv.reader(csvfile)
                next(movieReader)  #Skip header line
                for row in movieReader:
                    movieID = int(row[0])
                    tmdbid = row[2]
                    self.movieID_to_tmdbid[movieID] = tmdbid
                    
        return ratingsDataset
    
    
    def gettmdbID(self, movieID):
        if movieID in self.movieID_to_tmdbid:
            return self.movieID_to_tmdbid[movieID]
        else:
            return "tmdb id missing"
