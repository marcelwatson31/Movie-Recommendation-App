#Random recommendation System based on the amount of times a person selects

import os
import random
import math
import csv




#opens csv of movies and complies them into an ordered array

with open('C:/Users\marce\Desktop\movies.csv', 'r') as csv_movies:
  csv = csv.reader(csv_movies)
  genres = []
  movies = []
  tomatoes_ratings = []
  for row in csv:
      
      genres.append(row[1])
      movies.append(row[0])
      tomatoes_ratings.append(row[5])

movies_list = list(zip(movies,genres))

print("The movie you should watch is",random.choice(movies_list))
      
# Shows movies and genres listed
'''print(movies)
print(genres)
print(movies_list)

movies_genre_list = movies_list.values()'''







  
      

      


# This part of code is rudementary movie recommendation system that feeds on your genre watch history
# Uncomment the triple quotes and it will use input to suggest movie
# Main problem with code like this is in a large systems like Hulu or Netflix, condition statements like these become complicated to improve, debug, and follow
# To improve readability comments can be implemented, reduce conditionals to the minimum value needed for function, or define a functions with rules for your static classes or variables 

'''actioncount = 0
comedycount = 0
horrorcount = 0
on = True



action_movies = ["GoodFellas","Casino","Scarface","Die Hard","IP Man","Bad Boys II"]
horror_movies = ["Insidious","Counjouring","Temple","Chucky","Nightmare on Elm Street","Friday The 13th"]
comedy_movies = ["Hot Fuzz","Billy Madison","Django Unchained","Snakes on a Plane","Scary Movie 3","40 Year Old Virgin"]
genres = ["Comedy", "Action", "Horror"]
for tomato in range(1):
  print(genres[0], genres[1], genres[2] + ' these are the genres to choose from \n \n')
# While loop allows for this code to run indefinitely until terminated. input is converted into lower case and if given an input
#not known it will give a random movie from the category you have chosen most

while on == True:
      

    what_to_watch = input("What genre would you like to watch? ").lower()

    if what_to_watch == "comedy":
      comedycount += 1

      print("You will be watching comedy enjoy!")

    elif what_to_watch == "action":
        actioncount += 1
        print("You will be watching action enjoy!")

    elif what_to_watch == "horror":
      horrorcount += 1
      print("You will be watching horror enjoy!")

    elif what_to_watch != "comedy" or "horror" or "action":
      print("sorry that isn't a genre in our inventory yet! Please choose between action, horror, or comedy.")
      if actioncount > comedycount and actioncount > horrorcount:
        print("How about watching: " + random.choice(action_movies) + " \n")
      elif horrorcount > actioncount and horrorcount > comedycount:
        print("How about watching: " + random.choice(horror_movies) + " \n")
      elif comedycount > actioncount and comedycount  > horrorcount:
            print("How about watching: " + random.choice(comedy_movies) + " \n")  

    print("Action has been watched: " + str(actioncount))
    print("Horror has been watched: " + str(horrorcount))
    print("Comedy has been watched: " + str(comedycount))'''


  


 







