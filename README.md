# movies_repo

    
introuduction

***

Welcome to watchnext.py
---
---
The file named watchnext.py contains code about which movie is bes recommended to watch next from s file named (movies.txt ) where each separate line is a description of a different movie.


-----------------
-----------------
about watchnext,py
----------
***
Inside this file I have created a function with (description as the parameter)
of the function.I imported the module spacy and included(nlp = spacy.load('en_core_web_md')) This will return a Language object containing all components and data needed to process text. I then opened the file movies.txt that contains the description of all the movies, and created an empty list that declares and initialize a list to store movie list splitted into movie title and description

***
used the variable count to get the  number of movies in the  text file, then used a loop to iterate as many times as the number of movies in the text file .we check similarity between the movie description with the recently watched movie description, and get the index of the most similar value. And finally we returned the movie title similar to the watched movie

***


How to view this file
------------
*first you need to dowload this file on your local machine
* you can then view it by opening it after you have dowloaded this folder. 
* note that you can view it anywhere e.g using your phone or laptop 


