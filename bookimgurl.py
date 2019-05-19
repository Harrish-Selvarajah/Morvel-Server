import csv

class bookimgurl:

    movieID_to_imgurl = {}
   
    bookspath = r'./bookslink.csv'
    
    
    def loadurlLensLatestSmall(self):
        ratingsDataset = 0
        self.movieID_to_imgurl = {}
      
        with open(self.bookspath, newline='', encoding='ISO-8859-1') as csvfile:
                novelReader = csv.reader(csvfile)
                next(novelReader)  #Skip header line
                for row in novelReader:
                    novelID = int(row[0])
                    booklink = row[1]
                    self.movieID_to_imgurl[novelID] = booklink
                    
        return ratingsDataset
    
    
    def getNovellink(self, novelID):
        if novelID in  self.movieID_to_imgurl:
            return  self.movieID_to_imgurl[novelID]
        else:
            return ""
