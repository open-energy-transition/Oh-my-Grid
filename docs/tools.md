<div class="page-headers">
<h1>Useful Grid Mapping tools for OSM </h1>
</div>
<br>
<div class="tool-section">
  <div class="tool-content">
    <h2><div class="tools-header">Osmose per country</div></h2>
    <p><a href="https://open-energy-transition.github.io/osmose_per_country/">Osmose per country</a> - This is a front end interface that allows fetching data on gaps in the OSM data through the OSMOSE API on a country level.</p>

    <h3>What is Osmose?</h3>
    <p>"<a href="https://osmose.openstreetmap.fr/en/map/">Osmose-QA</a> is a quality assurance tool that detects issues in OpenStreetMap data"</p>

    <h3>How to use the Osmose per country tool</h3>
    <ol>
      <li>Go to the tool <a href="https://open-energy-transition.github.io/osmose_per_country/">website</a> or the repository to find it.</li>
      <li>Type the name of the country you want to find osmose issues for.</li>
      <li>Press Fetch Data. This will download a geojson file you can use as a hint layer in JOSM.</li>
    </ol>
    <p>Tip: Certain countries have different names associated, so to fetch the data for the entire country use an asterisk (wildcard) like: <code>France*</code></p>
  </div>
  <div class="tool-images">
    <img src="../images/osmoseapi.png" class="img-border" alt="Osmose API Tool Interface">
    <img src="../images/osmosenamib.png" class="img-border" alt="Osmose example">
  </div>
</div>


<div class="tool-section">
  <div class="tool-content">
    <h2><div class="tools-header">OSM and Global Energy Monitor comparison tool</div></h2>
    <p><a href="https://open-energy-transition.github.io/gem_per_country/">GEM per Country Power Tracker web application</a> - The tool allows users to preview and download GeoJSON data for global power plants in the Global Energy Monitor database filtered by country and power plant status.</p>

    <h3>How to use the GEM power plants per country tool</h3>
    <ol>
      <li>Go to the <a href="https://open-energy-transition.github.io/gem_per_country/">website</a>.</li>
      <li>Type the name of the country you want data for. Press preview, and download the geojson file.</li>
      <li>You can open this geojson file in JOSM, where you will be able to see all power plants from the GEM database.</li>
    </ol>
  </div>
  <div class="tool-images">
    <img src="../images/gemtracker.png" class="img-border" alt="GEM Tracker Interface">
    <img src="../images/gem_angola.png" class="img-border" alt="GEM Angola Data Example in JOSM">
  </div>
</div>


<div class="tool-section">
  <div class="tool-content">
    <h2><div class="tools-header">OSM and Wikidata comparison tool</div></h2>
    <p>This <a href="https://github.com/open-energy-transition/osm-wikidata-comparison/tree/main">repository</a> contains a Python script compares power plant data between OpenStreetMap (OSM) and Wikidata. It fetches data from both sources using APIs, performs comparisons based on geographic proximity and name, and identifies missing power plants or coordinate mismatches.<br> The comparison results are saved in CSV and GeoJSON formats.</p>

    <h3>How to use the OSM-Wikidata comparison tool</h3>
    <ol>
      <li>Paste the <a href="https://github.com/open-energy-transition/osm-wikidata-comparison/blob/main/requirements.txt">requirements.txt</a> file in your current directory/folder.</li>
      <li>Install dependencies needed:
        <pre><code class="language-bash">pip install -r requirements.txt</code></pre>
      </li>
      <li>Choose the country you want in the code by changing the name and Wikidata code. Run the script:
        <pre><code class="language-py"># ---------------------- CONFIGURATION ---------------------- #
# Specify the country you want to analyze. Adjust the 'COUNTRY_NAME' and 'country_code' accordingly.
COUNTRY_NAME = "Kenya" # Example: "Germany", "Brazil", "France"
#country_code = "Q1033"   # Country code according to Wikidata
max_distance_km = 0.7  #max_distance_km (float): The maximum distance to consider a match (in kilometers).
mismatch_threshold_km = 0.5 #mismatch_threshold_km (float): The threshold distance beyond which the coordinates are considered mismatched.
</code></pre>
      </li>
    </ol>
  </div>
  <div class="tool-images">
     <img src="../images/wikicsv.png" class="img-border" alt="Wikidata Comparison CSV Output">
     <img src="../images/wikigeo.png" class="img-border" alt="Wikidata Comparison GeoJSON Output">
  </div>
</div>


<div class="tool-section">
  <div class="tool-content">
    <h2><div class="tools-header">Google Maps Substations </div></h2>
    <p>Google Maps would be the perfect additional data source for the locations and names of substations worldwide, but so far <strong>no official authorisation has been granted</strong> for using the location of substation within OpenStreetMap. Google Maps shows many transmission and distribution substations that are difficult to locate using current mapping strategies, particularly in remote areas of low- and middle-income countries.</p>
    <p>Knowing only the locations of these substations would greatly accelerate the progress of grid mapping and allow the discovery of smaller substations that are relevant for estimating distribution network coverage and rural electrification levels. Together with the OpenStreetMap community, the data can be integrated using officially authorised satellite images for OpenStreetMap contributors, <strong>if</strong> permission is granted!</p>
    <p>Google Maps has <strong>not</strong> yet granted official authorisation for the use of its data. Google would provide a significant boost to the sustainable energy transition, tackling climate change and bringing electricity to rural communities at the same time. Therefore, we are kindly requesting formal permission to access and utilize the coordinates of ‘electrical substations’ displayed on Google Maps, for the purpose of enriching OpenStreetMap and advancing global grid mapping initiatives. This task for request is currently in progress and can be found <a href="https://github.com/orgs/open-energy-transition/projects/25?pane=issue&itemId=102888888">here</a>.</p>
  </div>
  <div class="tool-images">
    <figure>
      <img src="../images/angolagoogle.png" class="img-border" alt="Google Maps Satellite view showing substations in Angola">
      <figcaption class="image-caption">Imagery ©2025 CNES/Airbus, Maxar Technologies. Map data ©2025 Google</figcaption>
    </figure>
  </div>
</div>