# nav_planner
This app aims to generate a navigation for microlight classic competition.
# How it works
First, it will generate a kml trace, based on a perfect circle starting at your point with the given angle, with some drift apply on each point.  
Then, it will move each point to a knowing point in OpenStreetMap database. These points could be road, village limit, forest limit, etc.   
It will then get a picture for each turn points from Google Maps Satellites database.  
Finally, it will generate a pdf file on two pages with 12 pictures. All pictures are on turn point, but some turn points may not have a picture.  
# How to use it
## Generate your navigation
```bash
python src/nav_creator.py
```
All the files you need will be generated in the folder "nav_DATE".
## And then ?
Print the pdf file.  
Report the trace from the kml file on your map.
You can also go to [geoportail](https://www.geoportail.gouv.fr/donnees/cartes-ign-classiques) and import the kml, and print it !
# Useful links
https://developers.google.com/maps/documentation/javascript/get-api-key?hl=fr
https://developers.google.com/maps/documentation/maps-static?hl=fr
# Developer
Guilhem ROLLAND  
guilhem99.rolland@gmail.com  