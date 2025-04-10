# **Grid Mapping advanced kit**
## Mapping strategies :mag:
The following strategies outline different approaches to extending the existing transmission network. In general, the larger the tower and substation, the higher the voltage and therefore the greater the importance to the network. Priority should therefore be given to large, high-voltage infrastructure first. The easiest way to start mapping the transmission network is to find the location of new 'towers'. You can hardly go wrong with this and it will help you to familiarise yourself with the tool and the local network. **Only map infrastructure that you can confidently classify using satellite or ground imagery.** <br>
:eight_spoked_asterisk: Search for all "Unfinished power lines" in Osmose and check if you are able to find new towers at the end of the line. See the [tools](https://andreashd11.github.io/Grid-mappers/tools/) section. <br>
:eight_spoked_asterisk: Check if windparks, solar farms, and power plants are connected to the transmission grid.  The [GEM per Country](https://andreashd11.github.io/Grid-mappers/tools/) tool helps you to create a geojson file of all the power plants in a country.<br>
:eight_spoked_asterisk: Ensure all transmission substations are connected to the grid. <br>
:eight_spoked_asterisk: Check for news reports on new substations and transmission lines that have become operational in recent years. LLMs like ChatGPT allow you to search in the local language: "Please search for news about transmission lines or substation recently opened in country A. Please use the official language of the country for your search". <br>
:eight_spoked_asterisk: Search for new substation records and national substation records as a reference "hint" layer. LLMs like ChatGPT allow you to search in the local language: "Please search for transmission lines or substation datasets in X. Please use the official language of the country for your search." For a curated list of datasets that may be useful, see Awesome Electric Grid Mapping List.


### Bing attribution issue :no_entry:
<div class="align-with-heading">
  <img src="../images/bing_issue.png" class="img-border" width="300">
</div>
At the moment, there seems to be an issue with Bing attribution where it only seems to load in the mornings (CET). However, you can work around that for the time being using this little trick. <br>

1\. On a day where bing is working for you, copy and save the bing.attribution.xml file in another personal folder somewhere on your device. <br>

On Windows, this is in Appdata>Roaming>JOSM <br>
On Linux, it can be found in .cache>JOSM <br>

2\. On the day where it is not working, just go this folder and replace the bing.attribution.xml file with the one saved from the previous day. You might have to reload JOSM.