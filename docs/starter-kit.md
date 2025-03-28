# **Grid Mapping starter kit**
A [starter kit](https://github.com/open-energy-transition/grid-mapping-starter-kit) for Electrical Transmission Grid Mapping in OpenStreetMap, combining Osmose and Overpass with JOSM.
<div style="display: flex; gap: 20px; margin: 20px auto; flex-wrap: wrap;">
  <img src="../images/kenyamap.png" class="img-border" style="width: 400px;">
  <img src="../images/startermap.png" class="img-border" style="width: 380px;">
</div>
## Setup JOSM on your device :rocket:
<div style="float: right; margin: -25px 50px 0 50px;">
  <img src="../images/josm_logo.png"  width="100">
</div>
1\. Install [Java](https://www.java.com/en/download/help/download_options.html) on your device if not installed. <br>
2\. Install [JOSM](https://josm.openstreetmap.de/) on your device.<br>
3\. (Optional) If you want preconfigured preferences, download this preferences.xml [file](https://github.com/open-energy-transition/grid-mapping-starter-kit/blob/main/josm-config/preferences.xml) and paste it in the correct folder on your device. The [JOSM wiki](https://josm.openstreetmap.de/wiki/Help/Preferences) provides details on where to place it.<!-- No space here -->
<div style="float: right; margin: 5px 0 20px 20px; width: 350px;">
  <img src="../images/mapcss_tutorial.png" class="img-border" style="width: 100%;">
</div>
4\. Add our custom paint style which you can find [here](https://github.com/open-energy-transition/grid-mapping-starter-kit/blob/main/josm-config/transmission_grid_mapping_style.mapcss). To add to JOSM, go to Edit>Preferences>Map Paint Styles and press the "+" in the top right. Then you can paste this [URL](https://raw.githubusercontent.com/open-energy-transition/grid-mapping-starter-kit/refs/heads/main/josm-config/transmission_grid_mapping_style.mapcss) or the file saved on your device.<br>
5. Download this [template](https://github.com/open-energy-transition/grid-mapping-starter-kit/blob/main/josm-config/transmission_grid_mapping_template.joz) session, and in JOSM go to File>Open and open the .joz file. <br>
6. Create an OSM [account](https://www.openstreetmap.org/user/new?cookie_test=true) if you don't have one. Once you do, go to Edit>Preferences>OSM Server and press authorise now. Login with your OSM account, and authorise. Your account is now linked to JOSM on your device. <br>
7. Finally, activate "expert mode" in View>Expert mode. This will enable using Overpass API.

## Downloading transmission data such as power lines, substations, power plants. :inbox_tray:
<div style="float: right; margin: 5px 0 0 20px; width: 200px;">
  <img src="../images/activatelayer.png" class="img-border" style="width: 100%;">
</div>
1\. Make sure the layer that is activated is the "osm-transmission-grid" layer, and press the green "Download" button.
Switch to the Download from Overpass API tab. Paste [this](https://github.com/open-energy-transition/grid-mapping-starter-kit/blob/main/josm-config/transmission-grid.overpassql) overpassql query. <br>

<div style="float: right; margin: 10px -200px 0px 40px; width: 300px;">
  <img src="../images/bounding_box.png" class="img-border" style="width: 100%;">
</div>
2\. Select the Slippy Map tab in the Download from Overpass API and draw a bounding box for the country or region you want to map. (See at the bottom of this page the full explanation of how it currently is working if you want). With the red bounding box, try and put the centre of the box around the centre of the country or where you can see the name of the country. If you want to only map a region, you will have to change the admin_level to 4 in the script.

3\. Press Download. This will fetch for all the power infrastructure in the country/region. If "No info is found", then try again making sure the bounding box is over the name of the country and more or less centered.


:question: How the bounding box currently works with our Overpass query:
Currently, the boundary of the country we want is associated

⭐ More info can be found at the [repository](https://github.com/open-energy-transition/grid-mapping-starter-kit)
