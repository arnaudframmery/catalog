# Catalog
Easily search and sort its data, whatever the type

Data from the same family are belong to the same catalog, the equivalent of a table
Therefore a Catalog can bring together:
- contacts with their personal data
- vacation spots
- books you have read
- films you have seen
- ...

Let us consider that you want to store all the films that you have seen until now: you will need to store them in a new catalog called `My Movie` for example.

Then, every film has the same kind of data: a `title`, a `producer`, a `duration`, a `display` ... All these features can be seen as the columns of a table: here they will be the components of our catalog. You also have to set up a type for every component: is you component a simple text (good choice for the producer), number (more for the duration) or image (for the display of course).

Finally, every film is like a line in a table: each film is therefore an article.

To sum up, a catalog is composed of several articles with the same components. With a small number of article (for example 10 films) it's easy to find a film in particular. The task become more complicated if you have seen more than 100 films in your life (and it's surely the case).

Fortunately, you can set up filters on your components to find quickly the films that you want to find: all the films with a duration of more than 2 hours, or the ones with a specific producer for example. Moreover, it's also up to you to sort the articles against a specific component: have the ones with a minimum duration first for example.

Need to add a new component or to change the filter on a component ? You can easily do it to best suit your needs.


## Why this project ?

- Learn more about QT and SQLalchemy
- Provide a simple and user friendly solution to create, store, sort and filter data

## Requirements

- Python 3.9 or higher  
- Packages in requirements.txt

## Launch

execute the script `launch.py` with python
````shell script
python launch.py
````

## Features

- DB:
- [x] DB structure
- [x] Populate DB
- Catalog:
- [x] Catalog display & interaction
- [x] Catalog creation
- [x] Catalog suppression
- Filter:
- [x] Filter display & interaction
- [x] Filter component creation & edition
- [x] Filter component suppression
- Sorting:
- [x] Sorting display & interaction
- [x] Sorting component creation & edition
- [x] Sorting component suppression
- Article:
- [x] Article display & interaction & detail view
- [x] Article creation & edition
- [x] Article suppression
- Filter types:
- [x] Category filter
- [ ] Range filter
- Style:
- [x] Icons
- [x] Article detail view
- [x] Catalog view
- [x] Component settings dialog
- [x] Custom widgets
- [ ] Article select view
- Data types:
- [x] text
- [x] Number (int)
- [x] Number (float)
- [x] Pictures
- [ ] Dates
- [ ] Files
- [ ] Links
- Data injection:
- [ ] From csv
