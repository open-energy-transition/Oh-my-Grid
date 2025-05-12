<div class="page-headers">
<h1>Contribute and map with us! </h1>
</div>

Our initiative wants to build a community of mappers from all around the world, so that power infrastructure is continuously added and improved in the future.
You can join this [discord](https://discord.gg/a5znpdFWfD) server to learn more, and chat about OSM grid mapping with us.

If you want to join our community, join our OSM [team](https://mapping.team/teams/1570/invitations/eec8b5f8-b212-4013-8707-96245f300fa1), and use our hashtag **#ohmygrid**!
<br>

Here are some [heatmaps](https://yosmhm.neis-one.org/) of the mapping work some of our team has done (more than 92k towers placed!):
<div style="display: flex; justify-content: space-between; gap: 20px; margin: 20px 0;">
  <img src="../images/heatmapahd.png" class="img-border" width="300">
  <img src="../images/heatmapmwi.png" class="img-border" width="300">
  <img src="../images/heatmapTA.png" class="img-border" width="300">
</div>

<!-- Progress Bars Section -->
## **<div class="tools-header">Community progress :rocket:</div>**

<div class="progress-section"> 
   <button id="refresh-btn" style="margin-bottom:1rem;">
     🔄 Refresh stats (only click if the bars are not "loading...")
   </button>

  <div class="progress-item">
    <label>Changesets tagged <code>#ohmygrid</code>:</label>
    <div class="progress">
      <div class="progress-bar" id="cs-bar"></div>
    </div>
    <span id="cs-count">Loading…</span>
  </div>

  <div class="progress-item">
    <label>Towers mapped by our team: (will currently take 3 minutes to load)</label>
    <div class="progress">
      <div class="progress-bar" id="tower-bar"></div>
    </div>
    <span id="tower-count">Loading…</span>
  </div>
</div>

<script>
  // Function to fetch data and update the DOM/cache - ONLY TOWER COUNT
async function fetchAndUpdate() {
  console.log("Fetching fresh stats (Towers only)..."); // Debug log
  // Show loading state ONLY for towers
  // document.getElementById('cs-count').textContent = 'Loading...'; // Comment out or remove CS elements later
  document.getElementById('tower-count').textContent = 'Loading...';
  // document.getElementById('cs-bar').style.width = '0%'; // Comment out or remove CS elements later
  document.getElementById('tower-bar').style.width = '0%';

  try {
    // 1) Changesets -- COMMENTED OUT / REMOVED
    /*
    const csResp = await fetch('https://osmcha.org/api/v1/changesets/?hashtags=ohmygrid&page_size=1');
    if (!csResp.ok) throw new Error(`OSMCha fetch failed: ${csResp.statusText}`);
    const csData = await csResp.json();
    const csCount = csData.count || 0;
    */
    const csCount = 0; // Set a default value if needed, or remove cs elements entirely

    // 2) Towers
    const towerQuery = `
      [out:json][timeout:300];
      (
        node["power"="tower"](user:"Andreas Hernandez");
        node["power"="tower"](user:"Tobias Augspurger");
        node["power"="tower"](user:"Mwiche");
        node["power"="tower"](user:"davidtt92");
        node["power"="tower"](user:"relaxxe");
        node["power"="tower"](user: "Russ")(newer:"2025-03-01T00:00:00Z");
        node["power"="tower"](user: "map-dynartio")(newer:"2025-03-01T00:00:00Z");
        node["power"="tower"](user: "overflorian")(newer:"2025-03-01T00:00:00Z");
        node["power"="tower"](user: "nlehuby")(newer:"2025-03-01T00:00:00Z");
        node["power"="tower"](user: "ben10dynartio")(newer:"2025-03-01T00:00:00Z");
        node["power"="tower"](user: "InfosReseaux")(newer:"2025-03-01T00:00:00Z");


      );
      out count;
    `;
    console.log("Sending Overpass query..."); // Debug log
    const towerResp = await fetch('https://overpass-api.de/api/interpreter', {
      method: 'POST',
      // Sending the query raw in the body is usually fine for Overpass POST
      body: towerQuery.trim()
    });
    console.log("Overpass response received:", towerResp.status, towerResp.statusText); // Debug log
    if (!towerResp.ok) throw new Error(`Overpass fetch failed: ${towerResp.statusText}`);
    const towerData = await towerResp.json();
    console.log("Overpass JSON data:", towerData); // Debug log

    const towerCount = parseInt(towerData.elements[0]?.tags?.nodes?.total || towerData.elements[0]?.tags?.total || '0', 10);

    console.log("Counts fetched:", { csCount, towerCount }); // Debug log

    // 3) DOM updates (Only for towers now)
    // document.getElementById('cs-count').textContent    = csCount.toLocaleString(); // Comment out
    document.getElementById('tower-count').textContent = towerCount.toLocaleString();

    const towerGoal = 10000; // Consider making these configurable
    // document.getElementById('cs-bar').style.width    = Math.min(100, (csCount / csGoal) * 100) + '%'; // Comment out
    document.getElementById('tower-bar').style.width = Math.min(100, (towerCount / towerGoal) * 100) + '%';

    // 4) Cache in localStorage (Only tower count now)
    // Adapt the cache structure if you remove csCount permanently
    const dataToCache = { csCount: null, towerCount, timestamp: Date.now() }; // Set csCount to null or remove
    localStorage.setItem('ohmygridStats', JSON.stringify(dataToCache));
    console.log("Stats updated and cached."); // Debug log

  } catch (error) {
    console.error("Error fetching or updating stats:", error);
    // Display error message to the user
    // document.getElementById('cs-count').textContent = 'N/A'; // Update CS display
    document.getElementById('tower-count').textContent = 'Error';
  }
}

// *** IMPORTANT: Update updateProgressDisplay too ***
// You'll need to adjust the `updateProgressDisplay` function similarly
// to only handle the tower count from the cache or remove the csCount logic.

// Example adjusted updateProgressDisplay
async function updateProgressDisplay() {
  console.log("Updating progress display...");
  const cached = JSON.parse(localStorage.getItem('ohmygridStats') || 'null');
  const cacheExpiry = 60 * 60 * 1000; // 1 hour

  if (cached && cached.towerCount !== null && (Date.now() - cached.timestamp < cacheExpiry)) {
    console.log("Using cached stats for towers.");
    document.getElementById('tower-count').textContent = cached.towerCount.toLocaleString();
    const towerGoal = 10000;
    document.getElementById('tower-bar').style.width = Math.min(100, (cached.towerCount / towerGoal) * 100) + '%';
    // Handle CS display if you keep the elements
    // document.getElementById('cs-count').textContent = cached.csCount !== null ? cached.csCount.toLocaleString() : 'N/A';
    // document.getElementById('cs-bar').style.width = cached.csCount !== null ? Math.min(100, (cached.csCount / 500) * 100) + '%' : '0%';

  } else {
    console.log("Cache expired or missing, fetching fresh data.");
    await fetchAndUpdate();
  }
   // If you completely remove the CS HTML elements, you don't need to handle them here.
   // Otherwise, set a default state for CS count/bar:
   if (!cached || cached.csCount === null) {
       document.getElementById('cs-count').textContent = 'N/A';
       document.getElementById('cs-bar').style.width = '0%';
   }
}


// Keep the DOMContentLoaded wrapper and button listener as they were
document.addEventListener('DOMContentLoaded', function() {
  console.log("DOM fully loaded and parsed.");

  // Initial load
  updateProgressDisplay();

  // Wire up the refresh button
  const refreshButton = document.getElementById('refresh-btn');
  if (refreshButton) {
     refreshButton.addEventListener('click', () => {
         console.log("Refresh button clicked.");
         localStorage.removeItem('ohmygridStats'); // Clear cache on manual refresh
         fetchAndUpdate(); // Fetch and update immediately
     });
     console.log("Refresh button listener attached.");
  } else {
     console.error("Refresh button not found!");
  }
});

</script>

##**Want to track and see your personal mapping progress (KPI)? :white_check_mark:** <br>
This [repository](https://github.com/open-energy-transition/KPI-OSM/tree/main) has a few different scripts (Overpass and Python) to measure your KPI's, as well as a [web-interface](https://open-energy-transition.github.io/KPI-OSM/). You can see how many towers you have placed and the respective line voltage, the power line length you have edited in km, the amount of MW capacity you added as a % of the country's mapped capacity, and a distribution table by voltage of substations you have added. <br>
<div style="display: flex; justify-content: left; gap: 40px; margin: 20px auto; max-width: 1200px;">
  <img src="../images/kp3.png" class="img-border" width="400">
  <img src="../images/kp4.png" class="img-border" width="400">
</div>

## <div class="tools-header">Join the Community </div>
We welcome everyone to join our community calls and tutorials, to learn more about the mapping process and the initiative.
<iframe src="https://calendar.google.com/calendar/embed?height=600&wkst=1&ctz=Europe%2FBerlin&showPrint=0&title=Community%20live%20sessions&src=Y182ODE3NjE1MGIzMjY4MGRkZmUzMGM1ZTE1MDU0YTc5MTVhMzY2NmY1OGY5NjkxOGVjOTZhNDJjZWQwODQ2ZGVmQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23AD1457" style="border:solid 1px #777" width="800" height="600" frameborder="0" scrolling="no"></iframe>