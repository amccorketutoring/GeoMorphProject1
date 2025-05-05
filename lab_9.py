# Lab 9: Advanced Geospatial Visualization (Corrected with Forward Slashes)

import geopandas as gpd
import pandas as pd
import leafmap
from ipyleaflet import (
    Map,
    GeoJSON,
    LayersControl,
    SearchControl,
    WidgetControl,
    TileLayer,
    WMSLayer,
)
from ipywidgets import HTML

# Question 1: Search-enabled map
search_map = Map(center=[35.96, -83.92], zoom=10, scroll_wheel_zoom=True)
search_control = SearchControl(
    position="topleft",
    url="https://nominatim.openstreetmap.org/search?format=json&q={s}",
    zoom=12,
    property_name="display_name",
    marker=None,
)
search_map.add_control(search_control)
search_map.add_control(LayersControl())

# Question 2: ESA WMS layer and legend
esa_map = leafmap.Map()
esa_map.add_wms_layer(
    url="https://services.terrascope.be/wms/v2?",
    layers="WORLDCOVER_2021_MAP",
    name="ESA WorldCover 2021",
    attribution="ESA",
    transparent=True,
)
esa_map.add_legend(title="ESA WorldCover", legend_type="esa_worldcover")

# Question 3: Marker cluster map using local building file
gdf_buildings = gpd.read_file("data/KnoxCounty_Buildings.geojson")
gdf_buildings["latitude"] = gdf_buildings.geometry.y
gdf_buildings["longitude"] = gdf_buildings.geometry.x

cluster_map = leafmap.Map(center=[35.96, -83.92], zoom=10)
cluster_map.add_circle_markers_from_xy(
    gdf_buildings,
    x="longitude",
    y="latitude",
    radius=5,
    fill_colors="yellow",
    line_colors="red",
    fill_opacity=0.8,
)

# Question 4: Vector overlay map
vector_map = leafmap.Map(center=[35.96, -83.92], zoom=10)
vector_map.add_geojson(
    "data/KnoxCounty_Buildings.geojson",
    layer_name="Buildings",
    style={"color": "red", "fillOpacity": 0},
)

gdf_roads = gpd.read_file("data/tl_2023_47093_roads.shp")
vector_map.add_geojson(
    gdf_roads.__geo_interface__, layer_name="Roads", style={"color": "red", "weight": 2}
)

gdf_counties = gpd.read_file(
    "https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/data/US-counties.geojson"
)
df_attr = pd.DataFrame(
    {
        "FIPS": ["01001", "01003", "01005", "01007"],
        "UnemploymentRate": [5.6, 3.8, 6.1, 4.5],
    }
)
gdf_counties["id"] = gdf_counties["id"].astype(str)
df_attr["FIPS"] = df_attr["FIPS"].astype(str)
gdf_merged = gdf_counties.merge(df_attr, left_on="id", right_on="FIPS")

vector_map.add_data(
    gdf_merged,
    column="UnemploymentRate",
    cmap="YlOrRd",
    legend_title="Unemployment Rate (%)",
)

# Question 5: Split map of Libya flood imagery
split_map = leafmap.SplitMap(center=[32.1, 20.1], zoom=10)
split_map.add_basemap("Esri.WorldImagery")
split_map.add_left_layer(
    url="https://github.com/opengeos/datasets/releases/download/v0.1/libya_flood_before.tif",
    layer_name="Before Flood",
)
split_map.add_right_layer(
    url="https://github.com/opengeos/datasets/releases/download/v0.1/libya_flood_after.tif",
    layer_name="After Flood",
)
