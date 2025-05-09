<div class="page-headers">
<h1>Start Mapping </h1>
</div>
Welcome to our interactive mapping tool! Click on a country below to start mapping power infrastructure directly in JOSM. :rocket:

If this is your first time mapping, please go through the [starter-kit tutorial](https://ohmygrid.org/starter-kit/).

<p>
  When you make an edit, please use the <span class="big-font">#ohmygrid</span> in the changeset to help the initiative!
</p>


:exclamation: Remember to allow remote control in _Edit>Preferences>Remote Control_ and to disable all ad blocker.<br>
:exclamation: Please read the common mistakes section in the starter-kit! <br>
:exclamation: Certain big countries should not be clicked on at a national level (eg. Brasil, USA, India), but you can zoom in to click on regions/states.

You can select what power infrastructure you want by clicking on the different choices. The **Default** pulls all power infrastructure and should be used when mapping generally. The repository with all the overpass queries can be found [here](https://github.com/open-energy-transition/osm-grid-definition).
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

// 2) Dynamic query‑mode discovery via GitHub Contents API
const GITHUB_API_QUERIES =
  'https://api.github.com/repos/open-energy-transition/osm-grid-definition/contents/queries';

/** Base URL for raw file fetches (OverpassQL and version.txt) */
const RAW_BASE =
  'https://raw.githubusercontent.com/open-energy-transition/osm-grid-definition/main/queries';

let currentMode = null;

// 2a) discover all folders under /queries
async function loadModes() {
  const res = await fetch(GITHUB_API_QUERIES);
  if (!res.ok) throw new Error('Cannot load query modes from GitHub API');
  const items = await res.json();
  // keep only directory entries
  const modes = items.filter(i => i.type === 'dir').map(i => i.name);
  if (modes.length === 0) throw new Error('No query folders found');
  return modes;
}

// 2.1a) fetch the version.txt for the given mode
async function fetchVersion(mode) {
  const url = `${RAW_BASE}/${mode}/version.txt`;
  const r   = await fetch(url);
  if (!r.ok) throw new Error('version not found');
  return (await r.text()).trim();
}

// 2b) render one button per folder name
async function initQueryUI() {
  const modes = await loadModes();

  // sort so “default” is first
  modes.sort((a, b) => {
    if (a === 'Default') return -1;
    if (b === 'Default') return 1;
    return a.localeCompare(b);
  });

  currentMode = modes.includes('Default') ? 'Default' : modes[0];

  // create container
  const container = document.createElement('div');
  container.id = 'query-buttons';

  // insert *before* the map div, so it's right above the map
  const mapEl = document.getElementById('map');
  mapEl.parentNode.insertBefore(container, mapEl);

  // now add one button per mode
  modes.forEach(async mode => {
  // — your existing button code —
    const btn = document.createElement('button');
    btn.textContent = mode.replace(/_/g, ' ');
    btn.classList.add('query-btn');
    if (mode === currentMode) btn.classList.add('active');
    btn.onclick = () => {
      currentMode = mode;
      document.querySelectorAll('.query-btn').forEach(b =>
       b.classList.toggle('active', b === btn)
    );
  };
 
// 2) version label
    const ver = document.createElement('div');
    ver.classList.add('query-version');
    ver.textContent = '…';  // placeholder

    // 3) wrap them in a group
    const group = document.createElement('div');
    group.classList.add('query-group');
    group.appendChild(btn);
    group.appendChild(ver);

    // 4) append the group
    container.appendChild(group);

  try {
    const v = await fetchVersion(mode);
    ver.textContent = `v${v}`;
  } catch {
    ver.textContent = 'v?';
  }
});

}


// 2c) fetch the correct OverpassQL file on demand
async function fetchQuery(mode, adminLevel) {
  const rawUrl =
    `https://raw.githubusercontent.com/open-energy-transition/osm-grid-definition/` +
    `main/queries/${mode}/admin${adminLevel}.overpassql`;
  const r = await fetch(rawUrl);
  if (!r.ok) throw new Error(`Query file not found: ${mode}/admin${adminLevel}`);
  return r.text();
}

// 2d) unified click handler for country (level 2) & region (level 4)
async function handleAreaClick(iso, level, layer) {
  const name = layer.feature.properties.NAME;
  layer.setStyle({ color: '#ff7800' });
  layer.getPopup().setContent(`Loading ${name}…`).update();

  try {
    let tpl = await fetchQuery(currentMode, level);
    tpl = tpl.replace(/\$\{iso\}/g, iso);
    sendToJosm(tpl);
  } catch (err) {
    layer.getPopup().setContent(`Error: ${err.message}`).update();
  }

  setTimeout(() => {
    layer.setStyle({ color: '#3388ff' });
    layer
      .getPopup()
      .setContent(`<b>${name}</b><br>Click to load in JOSM`)
      .update();
  }, 2000);
}

// initialize the UI immediately
initQueryUI().catch(console.error);


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
      const iso  = layer.feature.properties.ISO_A2;
      const name = layer.feature.properties.NAME;

      layer.bindPopup(`<b>${name}</b><br>Click to load in JOSM`);
      layer.on('click', () => {
        // large countries should be clicked at region level when zoomed in
        if (largeCountries.includes(iso) && map.getZoom() >= zoomThreshold) {
          layer
            .getPopup()
            .setContent(`<b>${name}</b><br>Please click on a specific region`)
            .update();
          return;
        }
        handleAreaClick(iso, 2, layer);
      });
    });
  })
  .catch(error => console.error('Countries GeoJSON error:', error));

// Load region GeoJSON and add interactivity
fetch('../data/regions.geojson')
  .then(response => response.json())
  .then(regions => {
    regionsLayer.addData(regions);

    regionsLayer.eachLayer(layer => {
      const iso3166_2 = layer.feature.properties.ISO_1;
      const name      = layer.feature.properties.NAME;

      layer.bindPopup(`<b>${name}</b><br>Click to load in JOSM`);
      layer.on('click', () => {
        handleAreaClick(iso3166_2, 4, layer);
      });
    });
  })
  .catch(error => console.error('Regions GeoJSON error:', error));
</script>
