let mapInitialised = false;

document.getElementById('toggle-map').addEventListener('click', function() {
  const heatmap = document.getElementById('heatmap-container');
  const leaflet = document.getElementById('leaflet-container');

  if (heatmap.classList.contains('hidden')) {
    heatmap.classList.remove('hidden');
    leaflet.classList.add('hidden');
    this.textContent = 'Show Interactive Map';
  } else {
    heatmap.classList.add('hidden');
    leaflet.classList.remove('hidden');
    this.textContent = 'Show Heatmap';

    if (!mapInitialised) {
      initMap();
      mapInitialised = true;
    } else {
      map.invalidateSize(); 
    }
  }
});