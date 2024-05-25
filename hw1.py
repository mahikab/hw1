# FILL IN ALL THE FUNCTIONS IN THIS TEMPLATE
# MAKE SURE YOU TEST YOUR FUNCTIONS WITH MULTIPLE TEST CASES
# ASIDE FROM THE SAMPLE FILES PROVIDED TO YOU, TEST ON YOUR OWN FILES

# WHEN DONE, SUBMIT THIS FILE TO CANVAS

from collections import defaultdict
from collections import Counter


# ------ TASK 1: READING DATA  --------

# 1.1
# Task 1: Reading Data

# [10 pts] Write a function read_ratings_data(f) that takes in a ratings file name, and returns a dictionary. (Note: the parameter is a file name string such # # as "myratings.txt", NOT a file pointer.) 
# The dictionary should have movie as key, and the list of all ratings for it as value.
# For example:   movie_ratings_dict = { "The Lion King (2019)" : [6.0, 7.5, 5.1], "Titanic (1997)": [7] }
    # parameter f: movie ratings file name f (e.g. "movieRatingSample.txt")
    # return: dictionary that maps movie to ratings

def read_ratings_data(f):
    readRatingsDict = {}
    with open(f, 'r') as file: 
        for line in file: 
            parts = line.strip().split('|')
            movie = parts[0]
            rating = float(parts[1])
            
            if movie in readRatingsDict:
                readRatingsDict[movie].append(rating)
            else: 
                readRatingsDict[movie] = [rating]
                
    return readRatingsDict
    

# [10 pts] Write a function read_movie_genre(f) that takes in a movies file name and returns a dictionary. The dictionary should have a one-to-one mapping from # movie to genre.
# For example   { "Toy Story (1995)" : "Adventure", "Golden Eye (1995)" : "Action" }

# Watch out for leading and trailing whitespaces in movie name and genre name, and remove them before storing in the dictionary.

# 1.2    
# parameter f: movies genre file name f (e.g. "genreMovieSample.txt")
# return: dictionary that maps movie to genre
# WRITE YOUR CODE BELOW
def read_movie_genre(f):
    readGenreDict = {}
    with open(f, 'r') as file:

        for line in file:
            parts = line.strip().split('|')
            genre = parts[0].strip()
            movie = parts[2].strip()
            readGenreDict[movie] = genre
    
    return readGenreDict

# ------ TASK 2: PROCESSING DATA --------

# Task 2: Processing Data

# [8 pts] Genre dictionary
# Write a function create_genre_dict that takes as a parameter a movie-to-genre dictionary, of the kind created in Task 1.2 (read_movie_genre(f)
#   The function should return another # dictionary in which a genre is mapped to all the movies in that genre.
# For example:   { genre1: [ m1, m2, m3], genre2: [m6, m7] }

# 2.1
def create_genre_dict(d):
    createGenreDict = defaultdict(list)
    for movie, genre in d.items():
        createGenreDict[genre].append(movie)

    return dict(createGenreDict)
  
# [8 pts] Average Rating
# Write a function calculate_average_rating that takes as a parameter a ratings dictionary, of the kind created in Task 1.1. It should return a dictionary 
# where the movie is mapped to its average rating computed from the ratings list.
# For example:   {"Spider-Man (2002)": [3,2,4,5]}  ==>   {"Spider-Man (2002)": 3.5}
# 2.2

def calculate_average_rating(d):
    calculateAverageDict = {}

    for movie, ratings in d.items():
        if ratings:
            averageRating = sum(ratings) / len(ratings)
            calculateAverageDict[movie] = averageRating

    return calculateAverageDict
    
# ------ TASK 3: RECOMMENDATION --------
# [10 pts] Popularity based
# In services such as Netflix and Spotify, you often see recommendations with the heading “Popular movies” or “Trending top 10”.

# Write a function get_popular_movies that takes as parameters a dictionary of movie-to-average rating ( as created in Task 2.2), and an integer n (default 
# should be 10). The function should return a dictionary ( movie:average rating, same structure as input dictionary) of top n movies based on the average 
# ratings. If there are fewer than n movies, it should return all movies in ranked order of average ratings from highest to lowest.
# parameter d: dictionary that maps movie to average rating
# parameter n: integer (for top n), default value 10
# return: dictionary that maps movie to average rating, 
# in ranked order from highest to lowest average rating
    
# 3.1
def get_popular_movies(d, n=10):
    # Use Counter = list of movies sorted by average rating
    sortedMovies = Counter(d).most_common()
    return dict(sortedMovies[:n]) 
    #uses : slice


# [8 pts] Threshold Rating
# Write a function filter_movies that takes as parameters a dictionary of movie-to-average rating (same as for the popularity based function above), and a 
# threshold rating with default value of 3. The function should filter movies based on the threshold rating, and return a dictionary with same structure as the # input. For example, if the threshold rating is 3.5, the returned dictionary should have only those movies from the input whose average rating is equal to or # greater than 3.5.
    # parameter d: dictionary that maps movie to average rating
    # parameter thres_rating: threshold rating, default value 3
    # return: dictionary that maps movie to average rating
# 3.2

def filter_movies(d, thres_rating=3):
    #go through each movie and the average rating 
    filteredMovies = {movie: rating for movie, rating in d.items() if rating >= thres_rating}
    return filteredMovies

# [12 pts] Popularity + Genre based
# In most recommendation systems, genre of the movie/song/book plays an important role. Often, features like popularity, genre, artist are combined to present # recommendations to a user.
# Write a function get_popular_in_genre that, given a genre, a genre-to-movies dictionary (as created in Task 2.1), a dictionary of movie:average rating (as 
# created in Task 2.2), and an integer n (default 5), returns the top n most popular movies in that genre based on the average ratings. The return value should # be a dictionary of movie-to-average rating of movies that make the cut. If there are fewer than n movies, it should return all movies in ranked order of 
# average ratings from highest to lowest.
# Genres will be from those in the movie:genre dictionary created in Task 1.2. The genre name will exactly match one of the genres in the dictionary, so you do # not need to do any upper or lower case conversion.
# 3.3

def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    # make sure genre is in the genre-movie dict
    if genre not in genre_to_movies:
        print(f'Genre {genre} not found.')
        return {}
    
    movies_in_genre = genre_to_movies[genre]
    genreMovRat = {movie: movie_to_average_rating.get(movie, 0) for movie in movies_in_genre}
    sortedMovies = sorted(genreMovRat.items(), key = lambda x: x[1], reverse = True)
    return dict(sortedMovies[:n])


# [8 pts] Genre Rating
# One important analysis for content platforms is to determine ratings by genre.

# Write a function get_genre_rating that takes the same parameters as get_popular_in_genre above, except for n, and returns the average rating of the movies in # the given genre.
# 3.4
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # return: average rating of movies in genre

def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    if genre not in genre_to_movies:
        print(f"Genre '{genre}' not found.")
        return 0 
     
    # Return 0 as a default value if the genre is not found
    moviesInGenre = genre_to_movies[genre]
    genreMovRat = [movie_to_average_rating.get(movie, 0) for movie in moviesInGenre]

    # Calculate the average rating of movies in the genre
    if genreMovRat:
        averageRating = sum(genreMovRat) / len(genreMovRat)
        #return round(averageRating, 2) 
        return averageRating
    else:
        return 0  


# [12 pts] Genre Popularity
# Write a function genre_popularity that takes as parameters a genre-to-movies dictionary (as created in Task 2.1), a movie-to-average rating dictionary (as  
# created in Task 2.2), and n (default 5), and returns the top-n rated genres as a dictionary of genre:average rating. If there are fewer than n genres, it 
# should return all genres in ranked order of average ratings from highest to lowest. Hint: Use the above get_genre_rating function as a helper.
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps genre to average rating
# 3.5
    
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    genreRatings = {genre: get_genre_rating(genre, genre_to_movies, movie_to_average_rating) for genre in genre_to_movies}
    sortedGenres = sorted(genreRatings.items(), key = lambda x: x[1], reverse = True)
    return dict(sortedGenres[:n])

# ------ TASK 4: USER FOCUSED  --------

# [10 pts] Read the ratings file to return a user-to-movies dictionary that maps user ID to a list of the movies they rated, along with the rating they gave. Write a function named read_user_ratings for this, with the ratings file as the parameter.
# For example: { u1: [ (m1, r1), (m2, r2) ], u2: [ (m3, r3), (m8, r8) ] }

# where ui is user ID, mi is movie, ri is corresponding rating. You can handle user ID as int or string type, but make sure you consistently use it as the same type everywhere in your code.
    # parameter f: movie ratings file name (e.g. "movieRatingSample.txt")
    # return: dictionary that maps user to list of (movie,rapythoting)
# 4.1

def read_user_ratings(f):
    userRatingsDict = {}

    with open(f, 'r') as file:
        for line in file:
            # Split into movie, rating, and user
            movie, rating, user = line.strip().split('|')
            user = int(user)
            if user in userRatingsDict:
                userRatingsDict[user].append((movie, float(rating)))
            else:
                userRatingsDict[user] = [(movie, float(rating))]

    return userRatingsDict

# [12 pts] Write a function get_user_genre that takes as parameters a user id, the user-to-movies dictionary (as created in Task 4.1 above), and the movie-to-genre dictionary (as created in Task 1.2), and returns the top genre that the user likes based on the user's ratings. Here, the top genre for the user will be determined by taking the average rating of the movies genre-wise that the user has rated. If multiple genres have the same highest ratings for the user, return any one of genres (arbitrarily) as the top genre.
# 4.2
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # return: top genre that user likes

def get_user_genre(user_id, user_to_movies, movie_to_genre):
    userMoviesRatings = user_to_movies.get(user_id, [])

    # return none if the user has not rated anything
    if not userMoviesRatings:
        return None

    genreRatings = defaultdict(list)
    for movie, rating in userMoviesRatings:
        genre = movie_to_genre.get(movie)
        if genre:
            genreRatings[genre].append(rating)

    genreAverageRatings = {genre: sum(ratings) / len(ratings) for genre, ratings in genreRatings.items()}
    finalGenre = max(genreAverageRatings, key = genreAverageRatings.get)
    return finalGenre

    
    
# [12 pts] Recommend 3 most popular (highest average rating) movies from the user's top genre that the user has not yet rated. Write a function recommend_movies for this, that takes as parameters a user id, the user-to-movies dictionary (as created in Task 4.1 above), the movie-to-genre dictionary (as created in Task 1.2), and the movie-to-average rating dictionary (as created in Task 2.2). The function should return a dictionary of movie-to-average rating. If fewer than 3 movies make the cut, then return all the movies that make the cut in ranked order of average ratings from highest to lowest.
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # parameter movie_to_average_rating: dictionary that maps movie to average rating
    # return: dictionary that maps movie to average rating

# 4.3    
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    topGenre = get_user_genre(user_id, user_to_movies, movie_to_genre)
    if not topGenre:
        return {}

    userRatedMovies = set(movie for movie, _ in user_to_movies.get(user_id, []))
    unratedMoviesInGenre = [movie for movie, genre in movie_to_genre.items() if genre == topGenre and movie not in userRatedMovies]
    unratedMovieAvgRatings = {movie: movie_to_average_rating.get(movie, 0) for movie in unratedMoviesInGenre}
    sortedUnratedMovies = sorted(unratedMovieAvgRatings.items(), key = lambda x: x[1], reverse = True)
    
    return dict(sortedUnratedMovies[:3])

# -------- main function for your testing -----
def main():
    print("------ TASK 1: READING DATA  --------")
    print("Task1.1")
    fileName = "ratings.txt"
    result1_1 = read_ratings_data(fileName)
    print(result1_1)
        
    print("\nTask1.2")
    fileName2 = "movies.txt"
    result1_2 = read_movie_genre(fileName2)
    print(result1_2)
    
    print("\n---- TASK 2: PROCESSING DATA --------")
    print("Task2.1")
    result = create_genre_dict(result1_2)
    print(result)
        
    print("\nTask2.2")
    result = calculate_average_rating(result1_1)
    print(result)
    
    print("\n---- TASK 3: RECOMMENDATION --------")
    print("Task3.1")
    x = calculate_average_rating(result1_1)
    result = get_popular_movies(x)
    print(result)
         
    print("\nTask3.2")
    x = calculate_average_rating(result1_1)
    result = filter_movies(x)
    print(result)
        
    print("\nTask3.3")    
    y = create_genre_dict(result1_2)
    x = calculate_average_rating(result1_1)
    result = get_popular_in_genre("Comedy", y, x)
    print(result)
           
    print("\nTask3.4")
    gen = "Comedy"
    result = get_genre_rating(gen, y, x)
    print(gen)
    print(result)
       
    print("\nTask3.5")
    print(gen)
    result = genre_popularity(create_genre_dict(result1_2), calculate_average_rating(result1_1))
    print(result)
    
    print("\n-----TASK 4: USER FOCUSED  -------")
    print("Task4.1")
    fileName = "ratings.txt"
    result = read_user_ratings(fileName)
    print(result)

    print("\nTask4.2")
    userID = 15
    print(f'userID: {userID}')
    w = read_user_ratings(fileName)
    result = get_user_genre(userID, w, result1_2)
    print(result)
    
    print("\nTask4.3")
    userID = 15
    print(f'userID: {userID}')
    l = calculate_average_rating(result1_1)
    result = recommend_movies(userID, w, result1_2, l)
    print(result)
    
# when you execute hw1.py
main()