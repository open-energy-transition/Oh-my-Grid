# **Useful Grid Mapping tools for OSM**

<img src="../images/osmoseapi.png" class="img-border" align="right" width="320">
## **1. Osmose per country** 
[Osmose per country](https://github.com/open-energy-transition/osmose_per_country) - This is a front end interface that allows fetching data on gaps in the OSM data through the OSMOSE API on a country level.

### What is Osmose?
"[Osmose-QA](https://osmose.openstreetmap.fr/en/map/) is a quality assurance tool that detects issues in OpenStreetMap data"

### How to use the Osmose per country tool
1. Go to the tool [website](https://open-energy-transition.github.io/osmose_per_country/) or the repository to find it.
2. Type the name of the country you want to find osmose issues for.
3. Press Fetch Data. This will download a geojson file you can use as a hint layer in JOSM.

Tip: Certain countries have different names associated, so to fetch the data for the entire country use an asterisk (wildcard) like: France*
<br> 
<br>
<img src="../images/gemtracker.png" class="img-border" align="right" width="320">
## 2. **OSM and Global Energy Monitor comparison tool**
[GEM per Country Power Tracker web application](https://github.com/open-energy-transition/gem_per_country) - The tool allows users to preview and download GeoJSON data for global power plants in the Global Energy Monitor database filtered by country and power plant status.

### How to use the GEM power plants per country tool
1. Go to the [repository](https://github.com/open-energy-transition/gem_per_country) and copy the line to clone (instructions can be found there)
2. In your terminal/command prompt: 
```
git clone https://github.com/open-energy-transition/gem_per_country.git
```
```
cd gem_per_country
```
```
open index.html   # macOS
xdg-open index.html   # Linux
start index.html   # Windows
```





