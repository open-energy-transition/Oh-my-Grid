# Start Mapping

Welcome to our interactive mapping tool! Click on a country below to start mapping power infrastructure directly in JOSM.

<div id="map" style="height: 600px;"></div>

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>

<script>
// Initialize map
const map = L.map('map').setView([20, 0], 2);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '© OpenStreetMap'
}).addTo(map);

// Overpass query template - keep line breaks for readability
function buildOverpassQuery(iso) {
    return `[out:xml][timeout:300];
relation["boundary"="administrative"]["admin_level"="2"]["ISO3166-1:alpha2"="${iso}"]->.admin_boundary;
.admin_boundary map_to_area ->.searchArea;

node["power"="tower"](area.searchArea) -> .towers;
node["power"="pole"](area.searchArea) -> .poles;
way["power"="line"](area.searchArea)(bn.towers) -> .lines_connected;
way["power"="line"]["voltage"](if:t["voltage"] >= 90000)(area.searchArea) -> .high_voltage_lines;
way["power"="cable"](area.searchArea) -> .cables;
node.poles(w.high_voltage_lines) -> .hv_poles;
nwr["power"="substation"](area.searchArea) -> .substation_nwr;
nwr["power"="plant"](area.searchArea) -> .plant_nwr;
nwr["power"="generator"](area.searchArea) -> .generator_nwr;
nwr["power"="transformer"](area.searchArea) -> .transformer_nwr;
node["power"="portal"](area.searchArea) -> .portal_nodes;

(
  .towers;
  .hv_poles;   // Only HV poles
  .cables;
  .lines_connected;
  .high_voltage_lines;
  .substation_nwr;
  .plant_nwr;
  .generator_nwr;
  .portal_nodes;
  .transformer_nwr;
  .admin_boundary;
);

out body;
>;
out skel qt;`
}

// JOSM integration function
function sendToJosm(iso) {
  // Build your Overpass query and encode only that part.
  const rawQuery = buildOverpassQuery(iso);
  const encodedQuery = encodeURIComponent(rawQuery);
  
  // Construct the Overpass URL by inserting the encoded query.
  const overpassUrl = "https://overpass-api.de/api/interpreter?data=" + encodedQuery;
  
  // IMPORTANT: Do not encode the overpassUrl again.
  // Build the final JOSM URL by concatenating the strings manually.
  const josmUrl = "http://localhost:8111/import?url=" + overpassUrl + "&new_layer=true";
  
  console.log("Final URL to Test:", josmUrl);
  
  // Testing by opening a temporary window.
  const testWindow = window.open(josmUrl, '_josm_test');
  setTimeout(() => testWindow.close(), 2000);

  // Also trying via an iframe.
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