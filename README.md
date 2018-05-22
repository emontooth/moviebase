# MovieBase
## A web application built by Edward Montooth used to maintain a database of movies, their producers, and some of their actors!
### In MovieBase you can learn more about Edward Montooth, edit the information in the database, add or delete producers and movies and view information about producers and their movies. 
#### The application uses a database design of two tables, Movies and Producers. In the Movies table the columns consist of the movie ID which is the primary key, name, year, producer, and actors. In the Producers table the primary key is the producer ID followed by columns of name, and about. The two tables feature a *one to many relationship* where one producer can have many movies in the database. Producers must be added before their movie is added to the database and if a producer is deleted the movies belonging to that producer will also be deleted. 
#### Below is the database design in table format. 

### **Movies**
Movie ID | Name | Year | Producer | Actors
------------ | ------------- | ------------- | ------------- | -------------
1 | Interstellar | 2014 | Christopher Nolan | View 
2 | Avatar | 2009 | James Cameron | View 
3 | Titanic | 1997 | James Cameron | View 
4 | Star Wars | 1977 | George Lucas | View 


### **Producers**
Producer ID | Name | About  
------------ | ------------- | ------------- 
1 | Christopher Nolan | Christopher Edward Nolan is an English film director, screenwriter, and producer who holds both British and American citizenship. 
2 | James Cameron | James Francis Cameron (born August 16, 1954) is a Canadian filmmaker, philanthropist, and deep-sea explorer.
3 | Geogre Lucas | George Walton Lucas Jr. (born May 14, 1944) is an American filmmaker and entrepreneur.


## Instruction on how to run MovieBase

First you navigate to the [MovieBase repo.](https://github.com/emontooth/moviebase.git)

