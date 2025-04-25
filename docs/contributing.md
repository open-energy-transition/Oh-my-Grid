<div class="page-headers">
<h1>Contribute and map with us! </h1>
</div>

Our initiative wants to build a community of mappers from all around the world, so that power infrastructure is continuously added and improved in the future.
You can join this [discord](https://discord.gg/a5znpdFWfD) server to learn more, and chat about OSM grid mapping with us.

If you want to join our community, join our OSM [team](https://mapping.team/teams/1570/invitations/eec8b5f8-b212-4013-8707-96245f300fa1), and use our hashtag **#ohmygrid**!
<br>

Here are some [heatmaps](https://yosmhm.neis-one.org/) of the mapping work some of our team has done (more than 40k towers placed!):
<div style="display: flex; justify-content: space-between; gap: 20px; margin: 20px 0;">
  <img src="../images/heatmapahd.png" class="img-border" width="300">
  <img src="../images/heatmapmwi.png" class="img-border" width="300">
  <img src="../images/heatmapTA.png" class="img-border" width="300">
</div>

<!-- Progress Bars Section -->
<div class="progress-section">
  <h2>Community Progress</h2>
   
   <button id="refresh-btn" style="margin-bottom:1rem;">
     🔄 Refresh stats
   </button>

  <div class="progress-item">
    <label>Changesets tagged <code>#ohmygrid</code>:</label>
    <div class="progress">
      <div class="progress-bar" id="cs-bar"></div>
    </div>
    <span id="cs-count">Loading…</span>
  </div>

  <div class="progress-item">
    <label>Towers mapped by some of our team:</label>
    <div class="progress">
      <div class="progress-bar" id="tower-bar"></div>
    </div>
    <span id="tower-count">Loading…</span>
  </div>
</div>

<script>
async function fetchAndUpdate() {
  // 1) Changesets
  const csResp = await fetch('https://osmcha.org/api/v1/changesets/?hashtags=ohmygrid&page_size=1');
  const csCount = (await csResp.json()).count;

  // 2) Towers
  const towerQuery = `
    [out:json][timeout:100];
    (
      node["power"="tower"](user:"Andreas Hernandez");
      node["power"="tower"](user:"Tobias Augspurger");
      node["power"="tower"](user:"Mwiche");
      node["power"="tower"](user:"davidtt92");
      node["power"="tower"](user:"relaxxe");
    );
    out count;
  `;
  const towerResp = await fetch('https://overpass-api.de/api/interpreter', {
    method: 'POST',
    body: towerQuery.trim()
  });
  const towerCount = (await towerResp.json()).elements[0].count || 0;

  // 3) DOM updates
  document.getElementById('cs-count').textContent    = csCount.toLocaleString();
  document.getElementById('tower-count').textContent = towerCount.toLocaleString();

  const csGoal = 500, towerGoal = 10000;
  document.getElementById('cs-bar').style.width    = Math.min(100, csCount/csGoal*100) + '%';
  document.getElementById('tower-bar').style.width = Math.min(100, towerCount/towerGoal*100) + '%';

  // 4) Cache in localStorage
  const data = { csCount, towerCount, timestamp: Date.now() };
  localStorage.setItem('ohmygridStats', JSON.stringify(data));
}

async function updateProgress() {
  // Try to load from cache
  const cached = JSON.parse(localStorage.getItem('ohmygridStats') || 'null');
  if (cached && Date.now() - cached.timestamp < 24*60*60*1000) {
    // use cached
    document.getElementById('cs-count').textContent    = cached.csCount.toLocaleString();
    document.getElementById('tower-count').textContent = cached.towerCount.toLocaleString();
    document.getElementById('cs-bar').style.width    = Math.min(100, cached.csCount/500*100) + '%';
    document.getElementById('tower-bar').style.width = Math.min(100, cached.towerCount/10000*100) + '%';
  } else {
    // fetch fresh
    await fetchAndUpdate();
  }
}

// Wire up on load + button
updateProgress();
document.getElementById('refresh-btn')
        .addEventListener('click', () => fetchAndUpdate());
</script>

##**Want to track and see your personal mapping progress (KPI)? :white_check_mark:** <br>
This [repository](https://github.com/open-energy-transition/KPI-OSM/tree/main) has a few different scripts (Overpass and Python) to measure your KPI's, as well as a [web-interface](https://open-energy-transition.github.io/KPI-OSM/). You can see how many towers you have placed and the respective line voltage, the power line length you have edited in km, the amount of MW capacity you added as a % of the country's mapped capacity, and a distribution table by voltage of substations you have added. <br>
<div style="display: flex; justify-content: left; gap: 40px; margin: 20px auto; max-width: 1200px;">
  <img src="../images/kp3.png" class="img-border" width="400">
  <img src="../images/kp4.png" class="img-border" width="400">
</div>
