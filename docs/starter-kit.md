<div class="page-headers">
<h1>Grid Mapping starter kit</h1>
</div>
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
7. Finally, activate "expert mode" in View>Expert mode. This will enable using Overpass API. Also, make sure remote control is enabled in Edit>Preferences>Remote Control. You will need this enabled for the next step!

<div style="float: right; margin: 5px 0 20px 20px; width: 300px;">
  <img src="../images/clickmap.png" class="img-border" style="width: 100%;">
</div>
## Loading power infrastructure into JOSM :inbox_tray:
1\. Make sure remote control is enabled, and then just go to the start mapping [page](http://127.0.0.1:8000/Oh-my-Grid/start_mapping/). Here you can click on the country you want to map, and it will directly open JOSM and load the data of that country. <br>

## How to Map and upload your progress :outbox_tray:
<div style="float: right; margin: 5px 0 20px 20px; width: 300px;">
  <img src="../images/presets.png" class="img-border" style="width: 100%;">
</div>
1\. For ease of mapping, customise your toolbar with presets if you have not used the default preferences. Edit → Preferences → Toolbar. Then select the Presets → Man Made → Man Made/Power and add power towers, power portals and other presets for your mapping acticity.
<div style="float: right; margin: 5px 0 20px 20px; width: 200px;">
  <img src="../images/startmapping.png" class="img-border" style="width: 100%;">
</div>
2\. Start Mapping. Read more about the general mapping process in JOSM. Place nodes (eg.power towers, power portals) or place polygons to delimit an area (eg. substation, generator), and press on the preset structure you want it to be. <br> :pencil: Example: As seen in the image to the right, the red polygon is a substation which is mapped by adding nodes that are connected to each other and tagged as a substation. <br>

3\. Whilst having the OpenStreetMap layer activated, press the green Upload arrow. Avoid ignoring validation results. The only acceptable warning when uploading data is "Possible missing line support node within power line". When you make an edit, please use the **#ohmygrid** in the changeset to help the initiative!

⭐ More info can be found at the [repository](https://github.com/open-energy-transition/grid-mapping-starter-kit)
