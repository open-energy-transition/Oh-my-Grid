<div class="page-headers">
<h1>Grid Mapping starter kit</h1>
</div>
A [starter kit](https://github.com/open-energy-transition/grid-mapping-starter-kit) for Electrical Transmission Grid Mapping in OpenStreetMap, combining Osmose and Overpass with JOSM.
<div style="display: flex; gap: 20px; margin: 20px auto; flex-wrap: wrap;">
  <img src="../images/kenyamap.jpg" class="img-border" style="width: 400px;">
  <img src="../images/startermap.jpg" class="img-border" style="width: 380px;">
</div>

## **<div class="tools-header">Setup JOSM on your device :rocket:</div>**

<div style="float: right; margin: -25px 50px 0 50px;">
  <img src="../images/josm_logo.jpg"  width="100">
</div>
1\. Install [Java](https://www.java.com/en/download/help/download_options.html) on your device if not installed. <br>
2\. Install [JOSM](https://josm.openstreetmap.de/) on your device.<br>
3\. (Optional) If you want preconfigured preferences, download this preferences.xml [file](https://github.com/open-energy-transition/grid-mapping-starter-kit/blob/main/josm-config/preferences.xml) and paste it in the correct folder on your device. The [JOSM wiki](https://josm.openstreetmap.de/wiki/Help/Preferences) provides details on where to place it.<!-- No space here -->
<div style="float: right; margin: 5px 0 20px 20px; width: 350px;">
  <img src="../images/mapcss_tutorial.jpg" class="img-border" style="width: 100%;">
</div>
4\. Add our custom paint style which you can find [here](https://github.com/open-energy-transition/grid-mapping-starter-kit/blob/main/josm-config/transmission_grid_mapping_style.mapcss). To add to JOSM, go to Edit>Preferences>Map Paint Styles and press the "+" in the top right. Then you can paste this [URL](https://raw.githubusercontent.com/open-energy-transition/grid-mapping-starter-kit/refs/heads/main/josm-config/transmission_grid_mapping_style.mapcss) or the file saved on your device.<br>
5. Download this <a href="https://github.com/open-energy-transition/grid-mapping-starter-kit/blob/main/josm-config/transmission_grid_mapping_template.joz" target="_blank">template</a> session, and in JOSM go to File>Open and open the .joz file. <br>
6. Create an OSM [account](https://www.openstreetmap.org/user/new?cookie_test=true) if you don't have one. Once you do, go to Edit>Preferences>OSM Server and press authorise now. Login with your OSM account, and authorise. Your account is now linked to JOSM on your device. <br>
7. Finally, activate "expert mode" in View>Expert mode. This will enable using Overpass API. <br>
8. Make sure remote control is enabled in **Edit>Preferences>Remote Control**. You will need this enabled for the next step!

<div style="float: right; margin: 5px 0 20px 20px; width: 300px;">
  <img src="../images/clickmap.jpg" class="img-border" style="width: 100%;">
</div>
## **<div class="tools-header">Loading power infrastructure into JOSM :inbox_tray:</div>**
1\. Make sure remote control is enabled, and then just go to the start mapping [page](https://ohmygrid.org/start_mapping/). Here you can click on the country you want to map, and it will directly open JOSM and load the data of that country. <br>

## **<div class="tools-header">How to Map and upload your progress :outbox_tray:</div>**
<div style="float: right; margin: 5px 0 20px 20px; width: 300px;">
  <img src="../images/presets.jpg" class="img-border" style="width: 100%;">
</div>
1\. For ease of mapping, customise your toolbar with presets if you have not used the default preferences. Edit → Preferences → Toolbar. Then select the Presets → Man Made → Man Made/Power and add power towers, power portals and other presets for your mapping acticity.
<div style="float: right; margin: 5px 0 20px 20px; width: 200px;">
  <img src="../images/startmapping.jpg" class="img-border" style="width: 100%;">
</div>
2\. Start Mapping. Read more about the general mapping process in JOSM. Place nodes (eg.power towers, power portals) or place polygons to delimit an area (eg. substation, generator), and press on the preset structure you want it to be. If you want to learn how to map fast, go to the advanced kit tab! <br> 

:pencil: Example: As seen in the image to the right, the red polygon is a substation which is mapped by adding nodes that are connected to each other and tagged as a substation. <br>

3\. Whilst having the OpenStreetMap layer activated, press the green Upload arrow. Avoid ignoring validation results. The only acceptable warning when uploading data is "Possible missing line support node within power line". When you make an edit, please use the **#ohmygrid** in the changeset to help the initiative!

## <div class="tools-header">Map fast  :pushpin:</div>
If you want to be able to map efficiently and fast, you will need to know how to correctly place towers and power lines. This will save you loads of time: <br>
1\. Press A and draw nodes as you follow the towers. This will create a long line of untagged nodes, all connected by a untagged way. <br>
2\. Click on the way, and select power line to tag it. <br>
3\. Then press on the way again, and control+F to open up search. Then paste in the bar: _child selected type:node AND untagged_ 
This will select all untagged nodes of the way. <br>
4\. Then you can tag all the selected nodes as towers in one go. <br>
5\. Use the preset power tower or poles to set all nodes at once.  <br>
6\. If you ever lose this query, click the right arrow on the search window and select it from your history. <br>

## **<div class="tools-header">Common Mistakes :name_badge:</div>**
1\. Do not use the interactive map or the default queries for distribution grid mapping. The Overpass Turbo script provided with this starter kit and present in the interactive map is optimised for transmission grid mapping. Lines on towers below 90 kV are not visualised in JOSM and should not be mapped with the standard configuration of this script. <br>

2\. Not reading about [good practices](https://wiki.openstreetmap.org/wiki/Good_practice).<br>

3\. When you leave the downloaded area, you may find transmission grids that do not appear to have been mapped. Actually, they were not downloaded to JOSM and you map them 2 times. To avoid this always be aware of the country boundary and be careful when crossing highlighted dashed orange lines. Due to the design of Overpass Turbo, some elements such as power lines may still be visible. across the border, but other objects such as substations will appear as if they have not yet been mapped. <br>

4\. Mapping beyond your experience is something you should avoid. Mapping is an iterative process and you should not expect to be able to finish all the details you are mapping. If you cannot map with a high degree of certainty, leave it to local mappers, better satellite imagery or experienced grid mappers.

## Mapping Regulations
**⚠️ Before you start mapping, please find out about the mapping restrictions in the respective country. In some countries, the mapping of transmission lines is not permitted. Get in touch with local users by finding out about [local projects](https://wiki.openstreetmap.org/wiki/Power_networks). ⚠️**

⭐ More info can be found at the [repository](https://github.com/open-energy-transition/grid-mapping-starter-kit)
