"""
Example script that scatters random points across a country and generates the Voronoi regions for them. Both the regions
and their points will be plotted using the `plotting` sub-module of `geovoronoi`.
Author: Markus Konrad <markus.konrad@wzb.eu>
March 2018
"""
import json
import shapely
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
from geovoronoi import coords_to_points, points_to_coords, voronoi_regions_from_coords
from geovoronoi.plotting import subplot_for_map, plot_voronoi_polys_with_points_in_area

from unprocessed_data.bom.process_weather_station_data import get_stations_dict


stations = get_stations_dict()
station_vals = list(stations.values())

mapping = {}
coords = [Point(i['long'], i['lat']) for i in station_vals]
stnum = [i['stnum'] for i in station_vals]
name = [i['name'] for i in station_vals]
coords = {'stnum': stnum, 'name': name, 'geometry': coords}
coords = gpd.GeoDataFrame(coords, crs="EPSG:4326")
coords = coords.to_crs(epsg=3395)
for _, row in coords.iterrows():
    mapping[float(row['geometry'].x), float(row['geometry'].y)] = (row['stnum'], row['name'])


coords = [[float(i.x), float(i.y)] for i in coords.geometry]
print(coords)
coords = np.array(coords, dtype='float')
print(coords)

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
area = world[world.name == 'Australia']
assert len(area) == 1

# convert to World Mercator CRS
area = area.to_crs(epsg=3395)
# get the Polygon
area_shape = area.iloc[0].geometry
# converts to shapely Point
pts = [p for p in coords_to_points(coords) if p.within(area_shape)]
# convert back to simple NumPy coordinate array
coords = points_to_coords(pts)
poly_shapes, pts, poly_to_pt_assignments = voronoi_regions_from_coords(coords, area_shape)

o = json.loads(gpd.GeoSeries(poly_shapes).to_json())
print(o)

for xx, (poly_shape, pt) in enumerate(zip(poly_shapes, [pts[_[0]] for _ in poly_to_pt_assignments])):
    print(poly_shape, pt, (pt.x, pt.y), mapping[pt.x, pt.y])
    stnum, name = mapping[pt.x, pt.y]
    o['features'][xx]['properties']['stnum'] = stnum
    o['features'][xx]['properties']['name'] = name

with open('out.json', 'w') as f:
    f.write(json.dumps(o))

fig, ax = subplot_for_map()
plot_voronoi_polys_with_points_in_area(ax, area_shape, poly_shapes, coords, poly_to_pt_assignments)
#plot_voronoi_polys_with_points_in_area(ax, area_shape, poly_shapes, coords)   # monocolor

plt.tight_layout()
plt.savefig('random_points_across_italy.png')
plt.show()
