import pandas as pd

# Reading ratings file
# Ignore the timestamp column
ratings = pd.read_csv('./data/ml-latest-small/ratings1.csv', sep='\t', encoding='latin-1', usecols=['user_id', 'movie_id', 'rating'])

# Reading users file
users = pd.read_csv('./data/ml-latest-small/users1.csv', sep='\t', encoding='latin-1', usecols=['user_id', 'gender', 'zipcode', 'age_desc', 'occ_desc'])

# Reading movies file
movies = pd.read_csv('./data/ml-latest-small/movies1.csv', sep='\t', encoding='latin-1', usecols=['movie_id', 'title', 'genres'])

# Create a wordcloud of the movie titles
movies['title'] = movies['title'].fillna("").astype('str')
title_corpus = ' '.join(movies['title'])

ratings['rating'].describe()

# Join all 3 files into one dataframe
dataset = pd.merge(pd.merge(movies, ratings),users)
# Display 20 movies with highest ratings
dataset[['title','genres','rating']].sort_values('rating', ascending=False).head(20)

# Make a census of the genre keywords
genre_labels = set()
for s in movies['genres'].str.split('|').values:
    genre_labels = genre_labels.union(set(s))
    
class simMovie:

# Function that counts the number of times each of the genre keywords appear
 def count_word(self, dataset, ref_col, census):
    keyword_count = dict()
    for s in census: 
        keyword_count[s] = 0
    for census_keywords in dataset[ref_col].str.split('|'):        
        if type(census_keywords) == float and pd.isnull(census_keywords): 
            continue        
        for s in [s for s in census_keywords if s in census]: 
            if pd.notnull(s): 
                keyword_count[s] += 1
    #______________________________________________________________________
    # convert the dictionary in a list to sort the keywords by frequency
    keyword_occurences = []
    for k,v in keyword_count.items():
        keyword_occurences.append([k,v])
    keyword_occurences.sort(key = lambda x:x[1], reverse = True)
    return keyword_occurences, keyword_count

# Calling this function gives access to a list of genre keywords which are sorted by decreasing frequency
    keyword_occurences, dum = self.count_word(movies, 'genres', genre_labels)
    keyword_occurences[:5]



# Define the dictionary used to produce the genre wordcloud
    genres = dict()
    trunc_occurences = keyword_occurences[0:18]
    for s in trunc_occurences:
     genres[s[0]] = s[1]

# Break up the big genre string into a string array
    movies['genres'] = movies['genres'].str.split('|')
# Convert genres to string value
    movies['genres'] = movies['genres'].fillna("").astype('str')

# =============================================================================
#     from sklearn.feature_extraction.text import TfidfVectorizer
#     tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
#     tfidf_matrix = tf.fit_transform(movies['genres'])
#     tfidf_matrix.shape
# 
#     from sklearn.metrics.pairwise import linear_kernel
#     cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
#     cosine_sim[:4, :4]
# =============================================================================
 
# Build a 1-dimensional array with movie titles
# =============================================================================
#     titles = movies['title']
#     indices = pd.Series(movies.index, index=movies['title'])
# 
# =============================================================================
# Function that get movie recommendations based on the cosine similarity score of movie genres
 def genre_recommendations(title):
      
    movielist = []
    from sklearn.feature_extraction.text import TfidfVectorizer
    tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
    tfidf_matrix = tf.fit_transform(movies['genres'])
    tfidf_matrix.shape

    from sklearn.metrics.pairwise import linear_kernel
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    cosine_sim[:4, :4] 
    titles = movies['title']
    indices = pd.Series(movies.index, index=movies['title'])
    
    
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    #sim_scores = sim_scores[1:21]
    #movie_indices = [i[0] for i in sim_scores]
    
    
    

 genre_recommendations('Good Will Hunting (1997)')
 genre_recommendations('Toy Story (1995)')
 genre_recommendations('Saving Private Ryan (1998)')
 genre_recommendations('Jumanji (2018)')
