
# __init__ : a blueprint for objects attributes for classes
# class Games:
#     def __init__(self,genre,os,no_of_players):
#         self.genre = genre
#         self.os = os
#         self.no_of_players = no_of_players
# Fifa = Games('soccer','windows',2)
# print(Fifa.genre)

class Books:
    def __init__(self,author,rating,genre,year):
        self.author = author
        self.rating = rating
        self.genre = genre
        self.year = year

Python = Books('Mosh Drew',8.5,'programming','2015')
Javascript = Books('Brad',9.4,'programming',2017)
Swift = Books('Sean',8.5,'coding',2019)

print(Javascript.genre)











