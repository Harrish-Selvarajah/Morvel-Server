
import csv


from collections import defaultdict


class moviecdata:

    movieID_to_name = {}
    name_to_movieID = {}
    moviesPath = r'./movies1.csv'
    
    def loadMovieLensLatestSmall(self):

        self.movieID_to_name = {}
        self.name_to_movieID = {}
        self.movieID_to_genres = {}

        with open(self.moviesPath, newline='', encoding='ISO-8859-1') as csvfile:
                movieReader = csv.reader(csvfile)
                next(movieReader)  #Skip header line
                for row in movieReader:
                    movieID = int(row[0])
                    movieName = row[1]
                    genres = row[2]
                    self.movieID_to_name[movieID] = movieName
                    self.name_to_movieID[movieName] = movieID
                    self.movieID_to_genres[movieID] = genres
                    lenght = len(self.movieID_to_name)
                    

        return lenght
  
    def getGenress(self):
        genres = defaultdict(list)
        genreIDs = {}
        maxGenreID = 0
        with open(self.moviesPath, newline='', encoding='ISO-8859-1') as csvfile:
            movieReader = csv.reader(csvfile)
            next(movieReader)  #Skip header line
            for row in movieReader:
                movieID = int(row[0])
                genreList = row[2].split('|')
                genreIDList = []
                for genre in genreList:
                    if genre in genreIDs:
                        genreID = genreIDs[genre]
                    else:
                        genreID = maxGenreID
                        genreIDs[genre] = genreID
                        maxGenreID += 1
                    genreIDList.append(genreID)
                genres[movieID] = genreIDList
        # Convert integer-encoded genre lists to bitfields that we can treat as vectors
        for (movieID, genreIDList) in genres.items():
            bitfield = [0] * maxGenreID
            for genreID in genreIDList:
                bitfield[genreID] = 1
            genres[movieID] = bitfield            
        
        return genres
    
    def getMovieName(self, movieID):
        if movieID in self.movieID_to_name:
            return self.movieID_to_name[movieID]
        else:
            return ""
        
    def getMovieID(self, movieName):
        if movieName in self.name_to_movieID:
            return self.name_to_movieID[movieName]
        else:
            return 0
        
    def getGenres(self, movieID):
        if movieID in self.movieID_to_genres:
            return self.movieID_to_genres[movieID]
        else:
            return "Genre Missing"