<div class="page-headers">
<h1>Useful Grid Mapping Tools </h1>
</div>
<p>The following strategies and tooles will help you to extend the existing transmission grid networks in OpenStreetMap. In general, the larger the tower and substation, the higher the voltage and therefore the greater the importance to the network. Priority should therefore be given to large, high-voltage infrastructure first. The easiest way to start mapping the transmission network is to find the location of missing towers with the help of osmose.</p>

## <div class="tools-header">Osmose per country (integrated in Map It 📍)</div></h2>
<div class="tool-section">
  <div class="tool-content"> 
    <p> This tool is integrated in Map It 📍, but can also be found at <a href="https://open-energy-transition.github.io/osmose_per_country/">this</a> front end interface. The tool allows fetching data on gaps in the OSM data through the OSMOSE API on a country level.</p>

    <h3>What is Osmose?</h3>
    <p>"<a href="https://osmose.openstreetmap.fr/en/map/">Osmose-QA</a> is a quality assurance tool that detects issues in OpenStreetMap data". These include different classes of issues, such as "unfinished power transmission lines".</p>

    <h3>How to use the Osmose per country tool</h3>
    <ol>
      <li>Click on the Osmose issues button in Map It 📍 or go to the tool interface <a href="https://open-energy-transition.github.io/osmose_per_country/">website</a>.</li>
      <li>In Map It 📍, you can simply choose the issue you want to look at, and then click on a country/region. This will download a geojson file for you which you can open in JOSM and use as a hint layer.</li>
    </ol>
    <p>Tip: On the tool website, certain countries have different names associated, so to fetch the data for the entire country use an asterisk (wildcard) like: <code>France*</code></p>
  </div>
  <div class="tool-images">
  <figure>
    <img src="../images/osmoseapi.jpg" class="img-border" alt="Osmose API Tool Interface">
    <figcaption class="image-caption">Web interface.</figcaption>
    </figure>
  <figure>
    <img src="../images/osmosenamib.jpg" class="img-border" alt="Osmose example">
    <figcaption class="image-caption">Geojson layer in JOSM with Osmose issues in Namibia.</figcaption>
    </figure>
  </div>
</div>


## <div class="tools-header"> Global Energy Monitor tool (integrated in Map It 📍)</div></h2>
<div class="tool-section">
  <div class="tool-content">
    <p><a href="https://open-energy-transition.github.io/gem_per_country/">GEM per Country Power Tracker web application</a> - This tool is integrated in Map It 📍, and it allows users to preview and download GeoJSON data for global power plants in the <a href="https://globalenergymonitor.org/">Global Energy Monitor</a> database filtered by country and power plant status.</p>

    <h3>How to use the GEM power plants per country tool</h3>
    <ol>
      <li>Click on the Global Energy Monitor Power Plant button in Map It 📍 or go to the <a href="https://open-energy-transition.github.io/gem_per_country/">website</a>.</li>
      <li>A) In Map It 📍, you can simply choose the issue you want to look at, and then click on a country/region. This will download a geojson file for you.<br>
          B) On the website, type the name of the country you want data for. Press preview, and download the geojson file.</li>
      <li>You can open this geojson file in JOSM, where you will be able to see all power plants from the GEM database.</li>
    </ol>
  </div>
  <div class="tool-images">
  <figure>
    <img src="../images/gemtracker1.jpg" class="img-border" alt="GEM Tracker Interface">
    <figcaption class="image-caption">Web interface.</figcaption>
    </figure>
  <figure>
    <img src="../images/gem_angola.jpg" class="img-border" alt="GEM Angola Data Example in JOSM">
    <figcaption class="image-caption">Geojson layer in JOSM, of GEM power plants in Angola.</figcaption>
    </figure>
  </div>
</div>


## <div class="tools-header">Data and maps as hint layers</div></h2>
<div class="tool-section">
  <div class="tool-content">
    <p> In order to map more effectively, it is recommended to try and find maps and datasets that can help you find power lines, substations and power plants. National transmission system operators sometimes have publicly available maps, which can help you visualise the current state of the grid, and locate what is missing in OSM. Furthermore, having the names of substations can also help locate them. <br><br>
    
    We have made an <a href="https://ohmygrid.org/awesome/">awesome list</a> which you can access on this website too, which has datasets, maps, and information for many countries around the world. <br><br>
    
    ❗ Please use these datasets as hint layers, and check licenses to see how/if you are allowed to use them. Do not copy/data from these maps directly into OpenStreetMap. Each data point of the transmission network must be set manually and <a href="https://wiki.openstreetmap.org/wiki/Verifiability">verified</a> with official satellite data provided by the OpenStreetMap community.</p>
  </div>
  <div class="tool-images">
    <img src="../images/awesomelist.jpg" class="img-border" alt="GEM Tracker Interface">
  <figure>
    <img src="../images/bangladeshawesome.jpg" class="img-border" alt="GEM Angola Data Example in JOSM">
    <figcaption class="image-caption">Power Grid Company of Bangladesh transmission grid map.</figcaption>
    </figure>
  </div>
</div>

## <div class="tools-header">OSM and Wikidata comparison tool (integrated in Map It 📍)</div>
<div class="tool-section">

  <div class="tool-content">
    <p>
      This <a href="https://github.com/open-energy-transition/osm-wikidata-comparison/tree/main">repository</a>
      contains two Python scripts that compare power plant data between OpenStreetMap (OSM) and Wikidata, and also substation data.
      The power plant tool fetches data from both sources using APIs, performs comparisons based on geographic proximity
      and name, and identifies missing power plants or coordinate mismatches. The comparison results are saved in CSV
      and GeoJSON formats.
    </p>

    <h3>How to use the OSM‑Wikidata powerplant comparison tool</h3>
    <ol>
      <li> Since it is integrated in <a href="https://ohmygrid.org/map_it/">Map It 📍</a>, you can select the _Wikidata_ button.</li>
      <li> Once selected, you can choose between substations and powerplants.</li>
      <li> Press on a country of your choice, and it will download a geojson file of that country, if there is Wikidata data.
      </li>
      <li>Open the resulting GeoJSON, as a hint layer, in JOSM to inspect and map powerplants. Do not upload this layer though!</li>
    </ol>
  </div>

  <div class="tool-images">
  <figure>
    <img src="../images/wikicsv.jpg" class="img-border" alt="Wikidata Comparison CSV Output">
    <figcaption class="image-caption">Wikidata power plant CSV output file for Bolivia.</figcaption>
    </figure>
    <figure>
    <img src="../images/wikigeo.jpg" class="img-border" alt="Wikidata Comparison GeoJSON Output">
    <figcaption class="image-caption">Geojson layer in JOSM, of Wikidata power plants in Bolivia.</figcaption>
    </figure>
  </div>

</div>

     
## <div class="tools-header">Open Infrastructure Map </div></h2>
<div class="tool-section">
  <div class="tool-content">
   Open Infrastructure Map can be used as a tool to map and find issues by utilising the nighttime lights feature and osmose issues.<br>
   <ol>
    <li> Go to the <a href="https://openinframap.org/#2/26/12">website</a> and set the background to nighttime lights. This can help see clear "holes" in a country's grid.</li><br>
    <li> In layers, activate the power validation feature. If you zoom in and find an unfinished power line, you can see the osmose issue affiliated to this line.</li>
   </ol>
  </div> 
  <div class="tool-images">
  <figure>
     <img src="../images/openinfranight.jpg" class="img-border" alt="Wikidata Comparison CSV Output">
      <figcaption class="image-caption">OpenInfraMap</figcaption>
      </figure>
     <img src="../images/openinfraosmose.jpg" class="img-border" alt="Wikidata Comparison GeoJSON Output">
  </div>
</div>

## <div class="tools-header">Find new lines that branch off from substations </div></h2>
<div class="tool-section">
  <div class="tool-content">
   A simple yet efficient strategy for mapping the transmission grid is to check every substation for new lines branching out from it. 
   As most national transmission grids are entirely connected, this strategy enables you to trace and therefore map the entire grid network. 
   One single unmapped power tower can sometimes trace to a missing interconnector to another country as shown in the image of a substation in Malawi.
   Can you see the power tower that's missing from the bottom Left corner?
  </div> 
  <div class="tool-images">
   <figure>
     <img src="../images/substation_malawi.jpg" class="img-border" alt="Substation in Malawi with unmapped interconnector in the left corner">
     <figcaption class="image-caption">A substation in Malawi with an unmapped interconnector in the left corner.</figcaption>
   </figure>
  </div>
</div>



## <div class="tools-header">Google Maps substations </div></h2>
<div class="tool-section">
  <div class="tool-content">
    <p>Google Maps would be the perfect additional data source for the locations and names of substations worldwide, but so far <strong>no official authorisation has been granted</strong> for using the location of substation within OpenStreetMap. Google Maps shows many transmission and distribution substations that are difficult to locate using current mapping strategies, particularly in remote areas of low- and middle-income countries.</p>
    <p>Knowing only the locations of these substations would greatly accelerate the progress of grid mapping and allow the discovery of smaller substations that are relevant for estimating distribution network coverage and rural electrification levels. Together with the OpenStreetMap community, the data can be integrated using officially authorised satellite images for OpenStreetMap contributors, <strong>if</strong> permission is granted!</p>
    <p>Google Maps has <strong>not</strong> yet granted official authorisation for the use of its data. Google would provide a significant boost to the sustainable energy transition, tackling climate change and bringing electricity to rural communities at the same time. Therefore, we are kindly requesting formal permission to access and utilize the coordinates of ‘electrical substations’ displayed on Google Maps, for the purpose of enriching OpenStreetMap and advancing global grid mapping initiatives. This task for request is currently in progress and can be found <a href="https://github.com/orgs/open-energy-transition/projects/25?pane=issue&itemId=102888888">here</a>.</p>
  </div>
  <div class="tool-images">
    <figure>
      <img src="../images/angolagoogle.jpg" class="img-border" alt="Google Maps Satellite view showing substations in Angola">
      <figcaption class="image-caption"> An Angola distribution substation missing in OpenStreetMap. Imagery ©2025 CNES/Airbus, Maxar Technologies. Map data ©2025 Google</figcaption>
    </figure>
  </div>
</div>

## <div class="tools-header">Online investigation 🔍</div>
<div class="tool-section">
  <div class="tool-content">

  <p>Looking for recent news articles, reports, academic studies, or datasets related to newly operational substations and transmission lines is a simple way to find information about larger infrastructure that just started construction or operation. Politicians and investors love to be photographed with such new infrastructure. That's why you find almost always news articles and reports about new substations, transmission lines and power plants.</p>
    
  <p>Local Large Language Models (LLMs) can help by conducting searches in the country’s official language. For example: “Please search for news articles, reports, academic studies, or datasets about transmission lines or substations opened in Country A in the last 5 years. Use the official language of the country A. Only include resources not already listed in the <a href='https://github.com/open-energy-transition/Awesome-Electric-Grid-Mapping'>Awesome Electric Grid Mapping</a> repository.”</p>

  <p>Please be aware of the licence and quality of the documents you are finding. If you cannot validate the information you find by different sources, you can at least use the names of substations, regions and towns to identify the locations of new substations or transmission lines, and verify their visibility in satellite images. The fastest way to search global power infrastructure like power plants, substations or country interconnector by name is by the search function of <a href="https://openinframap.org/#2/26/12">Open Infrastructure Map</a>.</p>

  </div>
  <div class="tool-images">
    <figure>
      <img src="../images/mapstrats.jpg" class="img-border" alt="A wind farm in Bangladesh displayed in OpenStreetMap">
      <figcaption class="image-caption">A wind farm in Bangladesh displayed in OpenStreetMap that has been discovered by offical documents.</figcaption>
    </figure>
  </div>
</div>

## <div class="tools-header">Using the mapcss to locate "holes"  in the grid〰️</div>
<div class="tool-section">
  <div class="tool-content">

  <p>Another fast and efficient way to locate transmission lines that are unfinished, is to simply use the mapcss and look for unfinished lines. A lack of lines in a large area, could also tell you that a line might be missing there. <br>
  <br>
  If you haven't yet added our mapcss to JOSM, you can find it <a href="https://github.com/open-energy-transition/grid-mapping-starter-kit/tree/main/josm-config">here.</a></p>

  </div>
  <div class="tool-images">
    <figure>
      <img src="../images/mapcss_tool.jpg" class="img-border" alt="Mapcss of Bosnia displayed in OpenStreetMap">
      <figcaption class="image-caption">Mapcss layer of the Bosnian transmission grid in JOSM.</figcaption>
    </figure>
  </div>
</div>

## <div class="tools-header">Downloading transmission data of an area near a border 📥</div>
<div class="tool-section">
  <div class="tool-content">
    <p>If you are mapping an interconnector between two countries and want to see what’s mapped on the “other” side of the border, you can either do a quick Download from OSM in a new layer or use the following Overpass query:</p>
    <ol>
      <li>Copy this <a href="https://github.com/open-energy-transition/grid-mapping-starter-kit/blob/main/scripts/Alternative_overpass.overpassql">query</a> and paste it into “Download from Overpass API” in JOSM.</li>
      <li>Draw a small bounding box in the slippy map, then run the query to download.</li>
    </ol>
    <p><strong>Explanation:</strong> The query finds nodes in your bounding box, detects their admin area (level 4 by default), and fetches all power infrastructure within it. You can adjust the “admin level” in the query (e.g. level 2 for national, level 6 for province) by editing the <code>admin_level</code> parameter in the download tab. A smaller bounding box is better (faster execution).</p>
  </div>
  <div class="tool-images">
    <img src="../images/alternative_query.png" class="img-border" alt="Overpass Query Example" style="width:100%; float:right; margin: 5px 0 30px 20px;">
  </div>
</div>

## <div class="tools-header">Bing attribution issue ⛔</div>
<div class="tool-section">
  <div class="tool-content">
    <p>At the moment, there seems to be an issue with Bing attribution in JOSM where it only loads in the mornings (CET). To work around this:</p>
    <ol>
      <li>On a day when Bing attribution is working, copy the <code>bing.attribution.xml</code> file from your JOSM folder to a safe place:
        <ul>
          <li><strong>Windows:</strong> <code>%APPDATA%\JOSM\bing.attribution.xml</code></li>
          <li><strong>Mac:</strong> <code>~/Library/Caches/JOSM/bing.attribution.xml</code></li>
          <li><strong>Linux:</strong> <code>~/.cache/JOSM/bing.attribution.xml</code></li>
        </ul>
      </li>
      <li>On a day when it isn’t working, replace the broken file with your saved copy, then restart or reload JOSM.</li>
    </ol>
  </div>
  <div class="tool-images">
    <figure>
      <img src="../images/bing_issue.png" class="img-border" width="300" alt="Bing Attribution in JOSM">
    </figure>
  </div>
</div>
