```

from geomorphproject1.folium_map import CustomFoliumMap
import folium

m = CustomFoliumMap(location=(35.96, -83.92), zoom_start=10)

```


```

m.add_basemap("Stamen Toner")
m.add_layer_control()
m.add_vector("data/us_states.geojson")

```


```

tile_url = "https://basemap.nationalmap.gov/arcgis/rest/services/USGSShadedReliefOnly/MapServer/tile/{z}/{y}/{x}"
m.add_raster(tile_url, name="USGS Shaded Relief", opacity=0.8, attr="USGS The National Map")

```


```

image_url = "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/SE/GEOCOLOR/GOES16-SE-GEOCOLOR-1000x1000.jpg"
image_bounds = [[24, -92], [38, -75]]
m.add_image(image_url, bounds=image_bounds, opacity=0.7)

```


```

video_url = "https://rammb.cira.colostate.edu/ramsdis/online/loop_of_the_day/images/loop_of_the_day/goes-16/20200303000000/video/20200303000000_tnstorms.mp4"
video_bounds = [[34, -91], [37, -81]]
m.add_video(video_url, bounds=video_bounds, opacity=0.7)

```


```

wms_url = "https://neo.gsfc.nasa.gov/wms/wms"
m.add_wms_layer(
    url=wms_url,
    layers="BlueMarbleNG",
    name="NASA Blue Marble",
    format="image/png",
    transparent=True
)

```


```

folium.LayerControl().add_to(m)
m.save("folium_lab6_7_output.html")
m

```
