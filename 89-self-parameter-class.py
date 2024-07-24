
# The self Parameter:
# The self parameter is a reference to the current instance of the class, 
#  and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like,
# but it has to be the first parameter of any function in the class:

# Examples
# Using ohene as the "self" here
class Countries:
  def __init__(ohene,continent,price):
    ohene.continent = continent
    ohene.price = price

Miami = Countries('Europe',450000)
print(Miami.continent) 

# using zz as the "self" here
class Stars:
  def __init__(zz,star,country,position):
    zz.star = star
    zz.country = country
    zz.position = position
Mona = Stars('Azar','USA','dg')
Abella = Stars('Danger','USA','cg')
Violet = Stars('Myers','USA','bj')
print(Mona.star)







# class definitions cannot be empty, but if you for some reason have a class definition with no content, 
# put in the pass statement to avoid getting an error.

class Person:
  pass











# W3 Schools example
# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc):
#     print("Hello my name is " + abc.name)

# p1 = Person("John", 36)
# p1.myfunc()




