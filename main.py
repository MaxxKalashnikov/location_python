import pandas
import gmplot
from haversine import haversine

loc=pandas.read_csv('Location2.csv')
loc.head()

location_frame=loc[['latitude','longitude']]
location_list=location_frame.values.tolist()
my_path=zip(*location_list)
gmap = gmplot.GoogleMapPlotter(65.071375,25.516165, 13 )
gmap.plot(*my_path, color='red', edge_width=10)
gmap.draw('map_test1.html')

lon=loc['longitude']
lat=loc['latitude']

s=0
for k in range(len(lon)-1):
  s=s+haversine([lon[k],lat[k]],[lon[k+1],lat[k+1]])

print(f"The traveled distance is approximately: {s * 1000:.2f} m")
