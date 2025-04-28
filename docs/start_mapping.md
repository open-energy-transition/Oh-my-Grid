<div class="page-headers">
<h1>Start Mapping </h1>
</div>
Welcome to our interactive mapping tool! Click on a country below to start mapping power infrastructure directly in JOSM. :rocket:

<p>
  When you make an edit, please use the <span class="big-font">#ohmygrid</span> in the changeset to help the initiative!
</p>


:exclamation: Remember to allow remote control in _Edit>Preferences>Remote Control_ and to disable all ad blocker.<br>
:exclamation: Please read the common mistakes section in the starter-kit!

<style>
#map {
    position: relative;
    z-index: 1;
    width: 100%;
    height: 600px;
    margin: 20px 0;
    border-radius: 8px;
    border: 1px solid #ddd;
}

@media (max-width: 768px) {
    #map {
        height: 400px;
    }
}
</style>

<div id="map"></div>

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>

<script>
// Map
const map = L.map('map').setView([20, 0], 2);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '© <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener noreferrer">OpenStreetMap</a> contributors'
}).addTo(map);

// Define large countries that should use regional boundaries when zoomed in
const largeCountries = ['BR', 'US', 'CA', 'IN', 'MX', 'AU', 'CN'];
const zoomThreshold = 5; // Zoom level at which to show regions instead of countries

// Layers for countries and regions
const countriesLayer = L.geoJSON(null, {
    style: { color: '#3388ff', weight: 1 }
}).addTo(map);

const regionsLayer = L.geoJSON(null, {
    style: { color: '#3388ff', weight: 1 }
});

// Overpass query 
function buildOverpassQuery(iso) {
  return `[out:xml][timeout:300];
  
  // Get the complete administrative boundary relation and its members
  relation["boundary"="administrative"]["admin_level"="2"]["ISO3166-1:alpha2"="${iso}"]->.admin_boundary;
  (.admin_boundary; >;);
  // Convert the full relation into an area, which we use for the subsequent search
  .admin_boundary map_to_area ->.searchArea;
  
  // Get towers, poles, lines, cables, etc.
  node["power"="tower"](area.searchArea) -> .towers;
  node["power"="pole"](area.searchArea) -> .poles;
  way["power"="line"](area.searchArea) -> .lines_connected;
  way["power"="line"]["voltage"](if:t["voltage"] >= 90000)(area.searchArea) -> .high_voltage_lines;
  way["power"="cable"](area.searchArea) -> .cables;
  node.poles(w.high_voltage_lines) -> .hv_poles;
  
  // Get substations explicitly as nodes, ways, and relations
  node["power"="substation"](area.searchArea) -> .substation_nodes;
  way["power"="substation"](area.searchArea) -> .substation_ways;
  relation["power"="substation"](area.searchArea) -> .substation_relations;
  
  // And similarly for power plants, generators, and transformers
  node["power"="plant"](area.searchArea) -> .plant_nodes;
  way["power"="plant"](area.searchArea) -> .plant_ways;
  relation["power"="plant"](area.searchArea) -> .plant_relations;
  
  node["power"="generator"](area.searchArea) -> .generator_nodes;
  way["power"="generator"](area.searchArea) -> .generator_ways;
  relation["power"="generator"](area.searchArea) -> .generator_relations;
  
  node["power"="transformer"](area.searchArea) -> .transformer_nodes;
  way["power"="transformer"](area.searchArea) -> .transformer_ways;
  relation["power"="transformer"](area.searchArea) -> .transformer_relations;
  
  node["power"="portal"](area.searchArea) -> .portal_nodes;
  
  // Union all elements – note that we also include the original admin boundary
  (
    .towers;
    .hv_poles;
    .cables;
    .lines_connected;
    .high_voltage_lines;
    .substation_nodes;
    .substation_ways;
    .substation_relations;
    .plant_nodes;
    .plant_ways;
    .plant_relations;
    .generator_nodes;
    .generator_ways;
    .generator_relations;
    .portal_nodes;
    .transformer_nodes;
    .transformer_ways;
    .transformer_relations;
    .admin_boundary;
  );
  
  // First output: all elements with metadata
  out meta;
  // Second recursion: fetch all members of multipolygon relations, etc.
  >;
  // Output the full geometry (again with meta) so JOSM receives complete data
  out meta;
  `;
}

// Overpass query for regions
function buildRegionOverpassQuery(iso3166_2) {
  return `[out:xml][timeout:300];
  
  // Get the complete administrative boundary relation and its members
  relation["boundary"="administrative"]["admin_level"="4"]["ISO3166-2"="${iso3166_2}"]->.admin_boundary;
  (.admin_boundary; >;);
  // Convert the full relation into an area, which we use for the subsequent search
  .admin_boundary map_to_area ->.searchArea;
  
  // Get towers, poles, lines, cables, etc.
  node["power"="tower"](area.searchArea) -> .towers;
  node["power"="pole"](area.searchArea) -> .poles;
  way["power"="line"](area.searchArea) -> .lines_connected;
  way["power"="line"]["voltage"](if:t["voltage"] >= 90000)(area.searchArea) -> .high_voltage_lines;
  way["power"="cable"](area.searchArea) -> .cables;
  node.poles(w.high_voltage_lines) -> .hv_poles;
  
  // Get substations explicitly as nodes, ways, and relations
  node["power"="substation"](area.searchArea) -> .substation_nodes;
  way["power"="substation"](area.searchArea) -> .substation_ways;
  relation["power"="substation"](area.searchArea) -> .substation_relations;
  
  // And similarly for power plants, generators, and transformers
  node["power"="plant"](area.searchArea) -> .plant_nodes;
  way["power"="plant"](area.searchArea) -> .plant_ways;
  relation["power"="plant"](area.searchArea) -> .plant_relations;
  
  node["power"="generator"](area.searchArea) -> .generator_nodes;
  way["power"="generator"](area.searchArea) -> .generator_ways;
  relation["power"="generator"](area.searchArea) -> .generator_relations;
  
  node["power"="transformer"](area.searchArea) -> .transformer_nodes;
  way["power"="transformer"](area.searchArea) -> .transformer_ways;
  relation["power"="transformer"](area.searchArea) -> .transformer_relations;
  
  node["power"="portal"](area.searchArea) -> .portal_nodes;
  
  // Union all elements – note that we also include the original admin boundary
  (
    .towers;
    .hv_poles;
    .cables;
    .lines_connected;
    .high_voltage_lines;
    .substation_nodes;
    .substation_ways;
    .substation_relations;
    .plant_nodes;
    .plant_ways;
    .plant_relations;
    .generator_nodes;
    .generator_ways;
    .generator_relations;
    .portal_nodes;
    .transformer_nodes;
    .transformer_ways;
    .transformer_relations;
    .admin_boundary;
  );
  
  // First output: all elements with metadata
  out meta;
  // Second recursion: fetch all members of multipolygon relations, etc.
  >;
  // Output the full geometry (again with meta) so JOSM receives complete data
  out meta;
  `;
}

// JOSM integration function
function sendToJosm(query) {
  // Encode only the query part
  const encodedQuery = encodeURIComponent(query);
  
  // Construct the Overpass URL by inserting the encoded query.
  const overpassUrl = "https://overpass-api.de/api/interpreter?data=" + encodedQuery;
  
  // Build the final JOSM URL by concatenating the strings manually.
  const josmUrl = "http://localhost:8111/import?new_layer=true&url=" + overpassUrl;

  // Keep a log to see the actual URL
  console.log("URL ", josmUrl);
  
  const iframe = document.createElement('iframe');
  iframe.style.display = 'none';
  iframe.src = josmUrl;
  document.body.appendChild(iframe);
  setTimeout(() => document.body.removeChild(iframe), 1000);
}

// Handle zoom events to show/hide the appropriate layers
map.on('zoomend', function() {
    const currentZoom = map.getZoom();
    
    if (currentZoom >= zoomThreshold) {
        // When zoomed in enough, hide countries and show regions
        if (!map.hasLayer(regionsLayer)) {
            map.addLayer(regionsLayer);
        }
    } else {
        // When zoomed out, hide regions
        if (map.hasLayer(regionsLayer)) {
            map.removeLayer(regionsLayer);
        }
    }
});

// Load country GeoJSON and add interactivity
fetch('../data/countries.geojson')
    .then(response => response.json())
    .then(countries => {
        countriesLayer.addData(countries);
        
        countriesLayer.eachLayer(layer => {
            const iso = layer.feature.properties.ISO_A2;
            const name = layer.feature.properties.NAME;
            
            layer.bindPopup(`<b>${name}</b><br>Click to load in JOSM`);
            layer.on('click', () => {
                // Don't allow clicks on large countries when zoomed in enough
                if (largeCountries.includes(iso) && map.getZoom() >= zoomThreshold) {
                    layer.getPopup().setContent(`<b>${name}</b><br>Please click on a specific region`).update();
                    return;
                }
                
                // Show loading feedback
                layer.setStyle({ color: '#ff7800' });
                layer.getPopup().setContent(`Loading ${name}...`).update();
                
                try {
                    const query = buildOverpassQuery(iso);
                    sendToJosm(query);
                } catch (error) {
                    layer.getPopup().setContent(`Error: ${error.message}`).update();
                }
                
                // Reset style after 2 seconds
                setTimeout(() => {
                    layer.setStyle({ color: '#3388ff' });
                    layer.getPopup().setContent(`<b>${name}</b><br>Click to load in JOSM`).update();
                }, 2000);
            });
        });
    })
    .catch(error => console.error('Countries GeoJSON error:', error));

// Load regions GeoJSON and add interactivity
fetch('../data/regions.geojson')
    .then(response => response.json())
    .then(regions => {
        regionsLayer.addData(regions);
        
        regionsLayer.eachLayer(layer => {
            const iso3166_2 = layer.feature.properties.ISO_1;
            const name = layer.feature.properties.NAME;
            
            layer.bindPopup(`<b>${name}</b><br>Click to load in JOSM`);
            layer.on('click', () => {
                // Show loading feedback
                layer.setStyle({ color: '#ff7800' });
                layer.getPopup().setContent(`Loading ${name}...`).update();
                
                try {
                    const query = buildRegionOverpassQuery(iso3166_2);
                    sendToJosm(query);
                } catch (error) {
                    layer.getPopup().setContent(`Error: ${error.message}`).update();
                }
                
                // Reset style after 2 seconds
                setTimeout(() => {
                    layer.setStyle({ color: '#3388ff' });
                    layer.getPopup().setContent(`<b>${name}</b><br>Click to load in JOSM`).update();
                }, 2000);
            });
        });
    })
    .catch(error => console.error('Regions GeoJSON error:', error));
</script>
