# Start Mapping

Welcome to our interactive mapping tool! Click on a country below to start mapping power infrastructure directly in JOSM. :rocket:

:exclamation: Remember to allow remote control in Edit>Preferences>Remote Control

<div id="map" style="height: 600px;"></div>

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>

<script>
// Map
const map = L.map('map').setView([20, 0], 2);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '© <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener noreferrer">OpenStreetMap</a> contributors'
}).addTo(map);


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


// JOSM integration function
function sendToJosm(iso) {
  // Build your Overpass query and encode only that part.
  const rawQuery = buildOverpassQuery(iso);
  const encodedQuery = encodeURIComponent(rawQuery);
  
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


// Load GeoJSON and add interactivity
fetch('../data/countries.geojson')
    .then(response => response.json())
    .then(countries => {
        L.geoJSON(countries, {
            style: { color: '#3388ff', weight: 1 },
            onEachFeature: (feature, layer) => {
                const iso = feature.properties.ISO_A2;
                const name = feature.properties.NAME;
                
                layer.bindPopup(`<b>${name}</b><br>Click to load in JOSM`);
                layer.on('click', () => {
                    // Show loading feedback
                    layer.setStyle({ color: '#ff7800' });
                    layer.getPopup().setContent(`Loading ${name}...`).update();
                    
                    try {
                        sendToJosm(iso);
                    } catch (error) {
                        layer.getPopup().setContent(`Error: ${error.message}`).update();
                    }
                    
                    // Reset style after 2 seconds
                    setTimeout(() => {
                        layer.setStyle({ color: '#3388ff' });
                        layer.getPopup().setContent(`<b>${name}</b><br>Click to load in JOSM`).update();
                    }, 2000);
                });
            }
        }).addTo(map);
    })
    .catch(error => console.error('GeoJSON error:', error));
</script>