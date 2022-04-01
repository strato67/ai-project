import json
import csv
from shapely.geometry import shape, Polygon, Point

with open('Neighbourhoods.geojson', 'r') as f:
    js = json.load(f)

coordinateList = []
with open('coordinates.csv', 'r') as f2:
    reader = csv.reader(f2, skipinitialspace=True)
    for row in reader:
        
        coordinateList.append(row)

coordinateList = list(filter(None,coordinateList))

############################################################################################################kill me now
print(list(reversed(coordinateList[0])))

point = Point(-79.41, 43.73)

for feature in js['features']:

    polygon = shape(feature['geometry'])
    #print(polygon)
    
    if polygon.contains(point):
        print(feature['properties']['AREA_SHORT_CODE'])
    
