'''
CSS Project - Option 1: IMDB Data

'''
import pandas as pd

data = pd.read_csv("movie_dataset.csv")

'''What is the average revenue of all movies in the dataset? '''
x = data["Revenue (Millions)"].mean()
print("Average revenue : ",  x)

data["Revenue (Millions)"].fillna(x, inplace = True)

''' Highest rating movie'''
print("Highest rating : ", data['Rating'].max())

print(data[data['Rating'] == 9.0]['Title'])

'''How many movies were released in the year 2016? '''
print("Number movies in 2016: ", data[data['Year'] == 2016].shape[0])

'''How many movies were directed by Christopher Nolan? '''
print("Number movies by Christopher Nolan: ", data[data['Director'] == "Christopher Nolan"].shape[0])

'''How many movies in the dataset have a rating of at least 8.0?'''
print("Number movies have a rating of at least 8.0: ",data[data['Rating'] >= 8.0].shape[0])

'''What is the median rating of movies directed by Christopher Nolan? '''
print("The median rating of movies directed by Christopher Nolan: ", data[data['Director'] == "Christopher Nolan"]["Rating"].median())


''''Find the year with the highest average rating? '''
i = data["Year"].min()
year = 0
rating = 0
while i <= data["Year"].max():
    r = data[data['Year'] == i]["Rating"].mean()
    if r > rating :
        year = i
        rating = r
    i=i+1

print("Year with the highest average rating: ", year)

'''What is the percentage increase in number of movies made between 2006 and 2016? '''
x, y = data[data['Year'] == 2006].shape[0], data[2016 == data['Year']].shape[0]
print("Percentage increase: ", (y-x)/x *100)

'''Find the most common actor in all the movies?'''
lst = data['Actors'].tolist()
actors = []
for i in lst:
    actors = actors+i.split(',')
#print(actors)
    
def most_common(x):
    counter = 0
    com = x[0]
     
    for i in x:
        curr  = x.count(i)
        if(curr > counter):
            counter = curr
            com = i
 
    return com
 
print(most_common(actors))

'''How many unique genres are there in the dataset?'''
print()
lst = data['Genre'].tolist()
genre = []
for i in lst:
    genre = genre+i.split(',')

print(most_common(genre))

