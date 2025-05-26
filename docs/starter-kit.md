<div class="page-headers">
<h1>Grid Mapping Starter Kit 🌱</h1>
</div>
A [starter kit](https://github.com/open-energy-transition/grid-mapping-starter-kit) for Electrical Transmission Grid Mapping in OpenStreetMap, combining Osmose and Overpass with JOSM.
<div style="display: flex; gap: 20px; margin: 20px auto; flex-wrap: wrap;">
  <img src="../images/kenyamap1.jpg" class="img-border" style="width: 400px;">
  <img src="../images/starter_map.jpg" class="img-border" style="width: 380px;">
</div>

## **<div class="tools-header">Get started with OpenStreetMap and Open Infrastructure Map 🗺️</div>**

<div style="float: right; margin: 5px 0 20px 20px; width: 350px;">
  <img src="../images/openinframap-portugal.jpg" class="img-border" style="width: 100%;">
  <figcaption class="image-caption">Open infrastructure map showing the highly detailed transmission and distribution grid in Portugal.</figcaption>
</div>

If you don't already have an OpenStreetMap account, [create one first](https://www.openstreetmap.org/user/new). If you're new to OpenStreetMap, now is a good time to learn the basics of editing using the in-browser editor (iD) - find something which is missing from the map in your local area and add it! The [OpenStreetMap Wiki](https://wiki.openstreetmap.org) has lots of information about how to map with OpenStreetMap, and you can start by reading the [iD Beginners' Guide](https://learnosm.org/en/beginner/id-editor/). Adding missing power towers or substations can significantly improve mapping progress, as it gives other mappers a clue as to where parts of the entire grid are missing. To quickly check if anything is missing near you, go to the Open Infrastructure Map. Press the 'Find my location' button in the top right corner or enter your town in the search box. See something missing next to you? Map it using your iD editor. Don't worry about making mistakes. Mapping is an iterative process, and the OpenStreetMap community automatically detects anything that is missing. The OpenStreetMap Wiki pages [The Power Network](https://wiki.openstreetmap.org/wiki/Power_networks) and [Key:Power](https://wiki.openstreetmap.org/wiki/Key:power) provide an overview of how to map different power infrastructure.

**⚠️ Before you start mapping, please find out about the mapping restrictions in the respective country. In some countries, the mapping of transmission lines is not permitted. Get in touch with local users by finding out about [local projects](https://wiki.openstreetmap.org/wiki/Power_networks). ⚠️**

## **<div class="tools-header">Install JOSM :rocket:</div>**

JOSM is a more advanced desktop OpenStreetMap editor which is more suitable for power grid mapping.

<div style="float: right; margin: -25px 20px 0 50px;">
  <img src="../images/josm_logo.jpg"  width="90">
</div>

!!! note
    The JOSM Preferences window is accessed through the `Edit → Preferences` menu on Windows and Linux, and `JOSM → Settings` on Mac.

1\. Install [Java](https://www.java.com/en/download/help/download_options.html) on your device if not installed. <br>
2\. Install [JOSM](https://josm.openstreetmap.de/) on your device.<br>
3\. (Optional) If you want preconfigured preferences, download this preferences.xml [file](https://github.com/open-energy-transition/grid-mapping-starter-kit/blob/main/josm-config/preferences.xml) and paste it in the correct folder on your device. The [JOSM wiki](https://josm.openstreetmap.de/wiki/Help/Preferences) provides details on where to place it.<!-- No space here -->
4\. Further instructions on how to install and use JOSM on your device can be found at [learnOSM](https://learnosm.org/en/josm/start-josm/).<br> 


5\. Download this <a href="https://github.com/open-energy-transition/grid-mapping-starter-kit/blob/main/josm-config/transmission_grid_mapping_template.joz" target="_blank">template</a> session, and in JOSM go to File>Open and open the .joz file. <br>

6\. Create an OSM [account](https://www.openstreetmap.org/user/new?cookie_test=true) if you don't have one. Once you do, go to `Preferences → OSM Server` and press authorise now. Login with your OSM account, and authorise. Your account is now linked to JOSM on your device. 
:exclamation: Be aware that your token will be stored in your local preferences.xml file. Do not share your preferences file with anyone. <br>

7\. Finally, activate "expert mode" in `View → Expert mode`. This will enable using Overpass API. <br>

8\. Make sure remote control is enabled in `Preferences → Remote Control`. This must be activated for the grid data to be loaded automatically.


## **<div class="tools-header">Coloring your grid map and legend 🎨</div>**

<a href="https://raw.githubusercontent.com/open-energy-transition/color-my-grid/refs/heads/main/legend/power-grid-legend.png" target="_blank">
  <img 
    src="https://raw.githubusercontent.com/open-energy-transition/color-my-grid/refs/heads/main/legend/power-grid-legend.png" 
    class="img-border float-right" 
    alt="Power Grid Legend"
    width="300">
</a>


1. Add our custom paint style which you can find [here](https://raw.githubusercontent.com/open-energy-transition/color-my-grid/refs/heads/main/ohmygrid-default.mapcss). 
2. To add to JOSM, go to `Preferences → Map Paint Styles` and press the "+" in the top right. Then you can paste this [URL](https://raw.githubusercontent.com/open-energy-transition/grid-mapping-starter-kit/refs/heads/main/josm-config/transmission_grid_mapping_style.mapcss) or the file saved on your device. We recommend using this MapCSS file for [low-density grids](https://raw.githubusercontent.com/open-energy-transition/color-my-grid/refs/heads/main/ohmygrid-default.mapcss) and this one for [high-density grids](https://raw.githubusercontent.com/open-energy-transition/color-my-grid/refs/heads/main/ohmygrid-default.mapcss). 
3. You can use [ColorMyGrid](https://github.com/open-energy-transition/color_my_map), our MapCSS Generator tool, to easily adapt the MapCSS file to fit any special requirements you might have. 
4. In the ColorMyGrid repo you will also find the raw data to edit the [map legend](https://raw.githubusercontent.com/open-energy-transition/color-my-grid/refs/heads/main/legend/power-grid-legend.png).



## **<div class="tools-header">Loading power infrastructure into JOSM :inbox_tray:</div>**
Make sure remote control is enabled and ad-blocker disabled, and then go to the start mapping [page](https://ohmygrid.org/map-it/). Here you can click on the country you want to map, and it will directly open JOSM and load the data of that country. Use the "Default" to pull the data. <br>



## **<div class="tools-header">How to Map and upload your progress :outbox_tray:</div>**
<img 
  src="../images/presets.jpg" 
  class="img-border float-right" 
  alt="Clickmap screenshot"
  width="300">
1\. For ease of mapping, customise your top toolbar with presets if you have not used the default preferences. Right click the toolbar and choose `Configure toolbar`, then select `Presets → Man Made → Man Made/Power` and add power towers, power portals and other presets for your mapping acticity.
2\. Start Mapping. Read more about the general mapping process in JOSM. Place nodes (eg.power towers, power portals) or place polygons to delimit an area (eg. substation, generator), and press on the preset structure you want it to be. If you want to learn how to map fast, go to the advanced kit tab! <br> 
<img 
  src="../images/startmapping.jpg" 
  class="img-border float-right" 
  alt="Clickmap screenshot"
  width="300">
:pencil: Example: As seen in the image, the red polygon is a substation which is mapped by adding nodes that are connected to each other and tagged as a substation. <br>

3\. Whilst having the OpenStreetMap layer activated, press the green Upload arrow. Avoid ignoring validation results. The only acceptable warning when uploading data is "Possible missing line support node within power line". When you make an edit, please use the **#ohmygrid** in the changeset to help the initiative!


## **<div class="tools-header">Unfinished lines with Osmose and the todo Plugin ✅</div>**
<img 
  src="../images/todo.jpg" 
  class="img-border float-right" 
  alt="Clickmap screenshot"
  width="300">
:pencil: Example
A simple but very efficient way of mapping the network is the continuation of “Unfinished Transmission Lines”:

1. Download the [Unfinished Power Transmission lines (Class 2) via Osmose](https://ohmygrid.org/map-it/) for your country.
1. Drag and drop the downloaded geojson file into JSOM.
1. Download the todo plugin for JSOM. Edit --> Preferences. Search for todo, mark it and press OK. Press Windows --> todo list to show the todo list window. 
1. Press STRG+A (CTRL + A or COMMAND + A)  to select all issues in the new layer. Press the Add in the todo plugin window.
1. Switch back to the OSM data layer.
1. You can now systematically step through all the issues by pressing Mark.  


## <div class="tools-header">Map fast  :pushpin:</div>
If you want to be able to map efficiently and fast, you will need to know how to correctly place towers and power lines. This will save you loads of time:

1. Press `A` and draw nodes as you follow the towers. This will create a long line of untagged nodes, all connected by a untagged way.
1. Click on the way, and tag it as a power line.
1. Click on the way again, and `control+F` to open up search. Then paste in the bar: `child selected type:node AND untagged`. This will select all untagged nodes of the way.
1. Then you can tag all the selected nodes as towers in one go.
1. Use the preset power tower or poles to set all nodes at once.
1. If you ever lose this query, click the right arrow on the search window and select it from your history.

## **<div class="tools-header">Common Mistakes :name_badge:</div>**
1\. Do not use the interactive map or the default queries for distribution grid mapping. The Overpass Turbo script provided with this starter kit and present in the interactive map is optimised for transmission grid mapping. Lines on towers below 90 kV are not visualised in JOSM and should not be mapped with the standard configuration of this script. <br>

2\. Not reading about [good practices](https://wiki.openstreetmap.org/wiki/Good_practice).<br>

3\. When you leave the downloaded area, you may find transmission grids that do not appear to have been mapped. Actually, they were not downloaded to JOSM and you map them 2 times. To avoid this always be aware of the country boundary and be careful when crossing highlighted dashed orange lines. Due to the design of Overpass Turbo, some elements such as power lines may still be visible. across the border, but other objects such as substations will appear as if they have not yet been mapped. <br>

4\. Mapping beyond your experience is something you should avoid. Mapping is an iterative process and you should not expect to be able to finish all the details you are mapping. If you cannot map with a high degree of certainty, leave it to local mappers, better satellite imagery or experienced grid mappers.



