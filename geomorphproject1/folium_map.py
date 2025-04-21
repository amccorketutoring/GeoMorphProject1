import folium
import geopandas as gpd


class CustomFoliumMap(folium.Map):
    """
    Interactive map using folium with basemap, vector, and layer control.
    """

    def __init__(self, location=(20, 0), zoom_start=2, **kwargs):
        super().__init__(location=location, zoom_start=zoom_start, **kwargs)

    def add_basemap(self, tiles="OpenStreetMap", attr=None):
        folium.TileLayer(tiles=tiles, attr=attr or tiles).add_to(self)

    def add_layer_control(self):
        folium.LayerControl().add_to(self)

    def add_vector(self, filepath):
        gdf = gpd.read_file(filepath)
        folium.GeoJson(gdf).add_to(self)
