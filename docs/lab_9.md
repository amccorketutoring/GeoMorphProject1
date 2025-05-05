# Lab 9: Advanced Geospatial Visualization (Aligned with .ipynb)

## Question 1: Creating an Interactive Map
An interactive map using `ipyleaflet` with search capability was created. The search tool uses OpenStreetMap’s Nominatim service and zooms to searched places.

## Question 2: Adding Map Legends
The ESA WorldCover WMS tile layer was added using `leafmap`. A built-in ESA legend was displayed alongside.

## Question 3: Creating Marker Clusters
Using local building centroid data from `KnoxCounty_Buildings.geojson`, cluster markers were added with circle styles. Latitude and longitude were derived from the GeoDataFrame.

## Question 4: Visualizing Vector Data
Three vector layers were added:
- **Buildings**: From a local GeoJSON file, styled with red outlines and no fill.
- **Roads**: From a TIGER/Line shapefile `tl_2023_47093_roads.shp`, displayed in red.
- **Choropleth**: A merged dataset showing unemployment rate by county using US counties GeoJSON + simulated census data.

## Question 5: Creating a Split Map
A `SplitMap` was used to compare Libya before and after a flood using two remote GeoTIFFs. Esri World Imagery served as the basemap.