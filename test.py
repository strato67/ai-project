import folium
import requests
import pandas as pd

m = folium.Map(location=[43.6532, -79.3832],
           zoom_start=12,
           tiles='https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png',
           attr='My Data Attribution')

geoJSON = r".\Neighbourhoods.geojson"

folium.GeoJson(geoJSON, name="geojson").add_to(m)
crimeRate = requests.get("https://services.arcgis.com/S9th0jAJ7bqgIRjw/arcgis/rest/services/Neighbourhood_MCI/FeatureServer/0/query?where=1%3D1&outFields=Neighbourhood,Hood_ID,Population,Shape__Area,Shape__Length,Assault_AVG,AutoTheft_AVG,BreakandEnter_AVG,Homicide_AVG,Robbery_AVG,TheftOver_AVG&outSR=4326&f=json")







m.save("index.html")


#print(crimeRate.text)