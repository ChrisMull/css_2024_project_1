# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 13:32:10 2024

@author: chris
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

names = ['Rank', 'Title', 'Genre', 'Description', 'Director', 'Actors', 'Year', 'Runtime', 'Rating', 'Votes', 'Revenue', 'Metascore']  # more appropriate col. names
df = pd.read_csv("movie_dataset.csv",header=0,index_col=0,names=names)  # header=0 allows us to replace the col. names in the data with more appropriate ones

print("Q1")
max_rating = df["Rating"].max()  # finds maximum value in rating column 
max_rating_loc = df["Rating"].idxmax()  # identifies the index of the highest rated movie
max_rating_name = df.iloc[max_rating_loc-1,0]  # returns the name by searching the Title column at highest ranked index (index - 1 used to account for 1st counted value being at 0)
print("The highest rated movie is", max_rating_name,"with rating of", max_rating)

print("\nQ2")
revenue_og = df["Revenue"].mean()
df_rev = df
df_rev = df_rev.dropna() 
revenue_mod = df_rev["Revenue"].mean()  # not an ideal approach, as dropping nan also drops movies where revenue is known, since there are also nan values in metascore
print("Average revenue is", revenue_og, "million USD when assuming missing revenue values are 0. This mean slightly increases to", revenue_mod, "million USD when not considering films with no revenue data.")

print("\nQ3")
grouped = df.groupby("Year")
yearly_rev = grouped["Revenue"].mean()
avg_rev = yearly_rev[9:].mean()
print("Average revenue from 2015 onwards was", avg_rev, "million USD")

print("\nQ4")
year_count = grouped.size()
year_count = pd.DataFrame(year_count)
count_2016 = year_count.iloc[10,0]
print("The number of films released in 2016 was", count_2016)

print("\nQ5")
group_director = df.groupby("Director")
count_nolan = group_director.size()
count_nolan = pd.DataFrame(count_nolan)
print("In the df produced above, it can be seen Christopher Nolan directed 5 films")

print("\nQ6")
rating_8_up = df[df["Rating"]>=8.0]
rating_8_up_no = rating_8_up.groupby("Year").size().sum()
print("The number of films with a rating of at least 8.0 and up are", rating_8_up_no)

print("\nQ7")
nolan_rating = group_director.median(numeric_only=True)
print("In the df produced above, it can be seen that Christopher Nolan achieved a median rating of 8.6")

print("\nQ8")
avg_rating_year = grouped["Rating"].mean().idxmax()
print("The year with the highest average rating was", avg_rating_year)

print("\nQ9")
no_2006 = year_count.iloc[0,0]
increase = count_2016/no_2006*100
print("The number of movies made in 2016 represents a", increase, "% increase over that made in 2006")

print("\nQ10")
actors = df["Actors"].str.split(",",expand=True)  # Separates the string of all actors into separate actor strings
actors.columns = ["Actor 1", "Actor 2", "Actor 3", "Actor 4"]
actors_melted = pd.melt(actors)  # unpivots the columns, i.e. appends the columns 1 below the next
actors_melted["value"] = actors_melted["value"].str.lstrip().str.rstrip() # some actor names had spaces before/after, this command removes those spaces
actors_count = actors_melted.groupby("value").size()  # can then use grouping to find how many movies each actor has been in
actor_name = actors_count.idxmax()
print("The actor who has appeared in the most movies is", actor_name)

print("\nQ11")
genres = df["Genre"].str.split(",", expand=True)
genres_melted = pd.melt(genres)
genres_melted["value"] = genres_melted["value"].str.lstrip().str.rstrip()
genres_count = genres_melted.groupby("value")
genres_count = len(pd.DataFrame(genres_count))
print("There are ", genres_count, "unique genres catalogued")

print("\nQ12")
print("Q12 output can be seen in the plots pane - conclusions have been uploaded to the canvas project")

plt.figure(1)
plt.scatter(df["Runtime"],df["Rating"])
plt.xlabel("Time (min)")
plt.ylabel("Rating")


plt.figure(2)
plt.scatter(df["Metascore"],df["Revenue"])
plt.xlabel("Metascore")
plt.ylabel("Revenue")

plt.figure(3)
plt.scatter(df["Votes"],df["Metascore"])
plt.xlabel("Votes")
plt.ylabel("Metascore")

plt.figure(4)
plt.bar(df["Year"],df["Revenue"])
plt.xlabel("Year")
plt.ylabel("Total revenue")

plt.figure(5)
plt.scatter(df["Rating"],df["Revenue"])
plt.xlabel("Rating")
plt.ylabel("Revenue")

plt.show()

