const cityData = JSON.parse(document.getElementById('city-data').textContent);
const cityMap = Object.fromEntries(cityData.map((city) => [city.slug, city]));
const form = document.getElementById('trip-form');
const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const costsEl = document.getElementById('costs');
const itineraryEl = document.getElementById('itinerary-list');
const weatherEl = document.getElementById('weather-list');
const routeSummaryEl = document.getElementById('route-summary');
const splitOutputEl = document.getElementById('split-output');
const expenseListEl = document.getElementById('expense-list');
const poiResultsEl = document.getElementById('poi-results');
const expenses = [];
let latestPlan = null;
let map;
let routeLayer;

function iconRefresh() {
  if (window.lucide) {
    window.lucide.createIcons();
  }
}

function rupee(value) {
  return new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR', maximumFractionDigits: 0 }).format(value);
}

function showPanel(name) {
  document.querySelectorAll('.view-panel').forEach((panel) => {
    panel.classList.toggle('is-active', panel.dataset.panel === name);
  });
  window.scrollTo({ top: 0, behavior: 'smooth' });
  if (name === 'map' && map) {
    setTimeout(() => {
      map.invalidateSize();
      const routeCities = latestPlan ? latestPlan.route : [cityMap.bangalore, cityMap.goa];
      drawRoute(routeCities);
    }, 120);
  }
  iconRefresh();
}

function initMap() {
  if (!window.L) {
    setTimeout(initMap, 250);
    return;
  }
  map = L.map('map', { scrollWheelZoom: false }).setView([20.5937, 78.9629], 5);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '&copy; OpenStreetMap contributors',
  }).addTo(map);
  drawRoute([cityMap.bangalore, cityMap.goa]);
}

async function drawRoute(routeCities) {
  if (!map || !routeCities.length) return;
  if (routeLayer) routeLayer.remove();
  const points = routeCities.map((city) => [city.lat, city.lon]);
  routeLayer = L.layerGroup().addTo(map);
  const coordinates = routeCities.map((city) => `${city.lon},${city.lat}`).join(';');
  try {
    const response = await fetch(`https://router.project-osrm.org/route/v1/driving/${coordinates}?overview=full&geometries=geojson`);
    const route = await response.json();
    const geometry = route.routes?.[0]?.geometry?.coordinates;
    if (!geometry) throw new Error('No route geometry');
    L.geoJSON({ type: 'LineString', coordinates: geometry }, {
      style: { color: '#24f5ff', weight: 5, opacity: 0.92 },
    }).addTo(routeLayer);
  } catch (error) {
    L.polyline(points, { color: '#24f5ff', weight: 5, opacity: 0.9, dashArray: '8 8' }).addTo(routeLayer);
  }
  routeCities.forEach((city, index) => {
    const label = index === 0 ? 'Start' : index === routeCities.length - 1 ? 'Finish' : `Night ${index}`;
    L.marker([city.lat, city.lon]).addTo(routeLayer).bindPopup(`${label}: ${city.name}`);
  });
  map.fitBounds(points, { padding: [40, 40] });
}

function renderCosts(costs) {
  const items = [
    ['Fuel', costs.fuel],
    ['Tolls', costs.tolls],
    ['Hotels', costs.hotels],
    ['Food', costs.food],
    ['Total', costs.total],
    ['Per person', costs.per_person],
  ];
  costsEl.innerHTML = items.map(([label, value]) => `
    <div class="metric">
      <span>${label}</span>
      <strong>${rupee(value)}</strong>
    </div>
  `).join('');
}

function renderItinerary(plan) {
  itineraryEl.innerHTML = plan.itinerary.map((day) => `
    <article class="day-card">
      <span>Day ${day.day} - ${day.date} - ${day.city}, ${day.state}</span>
      <h3>${day.title}</h3>
      <div class="drive-timeline">
        ${day.drive_blocks.map((block) => `
          <div class="drive-step">
            <span>${block.label} - ${block.distance}</span>
            <p>${block.text}</p>
          </div>
        `).join('')}
      </div>
      <div class="day-grid">
        <div><span>Local stop</span>${day.morning}</div>
        <div><span>Scenic/place option</span>${day.afternoon}</div>
        <div><span>Evening</span>${day.evening}</div>
      </div>
      <p><strong>Stay:</strong> ${day.hotel}. <strong>Food:</strong> ${day.restaurant}. <strong>Road note:</strong> ${day.drive_note}</p>
    </article>
  `).join('');
}

async function loadWeather(routeCities, days) {
  weatherEl.textContent = 'Loading live weather from Open-Meteo...';
  const forecasts = await Promise.all(routeCities.map((city) => (
    fetch(`/api/weather/${city.slug}/?days=${Math.min(days, 7)}`).then((response) => response.json())
  )));
  weatherEl.innerHTML = forecasts.map((report) => {
    if (report.error) {
      return `<div class="weather-day"><strong>${report.city}</strong><span>Weather unavailable</span>${report.error}</div>`;
    }
    const first = report.forecast[0];
    return `<div class="weather-day">
      <span>${report.city}</span>
      <strong>${first.min_c}C - ${first.max_c}C</strong>
      Rain chance ${first.rain_pct ?? 0}% today
    </div>`;
  }).join('');
}

function renderSplit() {
  if (!latestPlan) return;
  const extra = expenses.reduce((sum, item) => sum + item.amount, 0);
  const total = latestPlan.costs.total + extra;
  splitOutputEl.innerHTML = `
    <div class="metric">
      <span>Total with extras</span>
      <strong>${rupee(total)}</strong>
    </div>
    <div class="metric">
      <span>Each traveller pays</span>
      <strong>${rupee(Math.round(total / latestPlan.travelers))}</strong>
    </div>
  `;
  expenseListEl.innerHTML = expenses.map((item) => `<li>${item.name}: <strong>${rupee(item.amount)}</strong></li>`).join('');
}

function updateSos(plan) {
  const contact = document.getElementById('emergency-contact').value.trim();
  const callTarget = contact || plan.emergency.primary;
  document.getElementById('sos-call').href = `tel:${callTarget}`;
}

async function planTrip() {
  const data = new FormData(form);
  const payload = {
    origin: data.get('origin'),
    destination: data.get('destination'),
    start_date: data.get('start_date'),
    end_date: data.get('end_date'),
    travelers: data.get('travelers'),
    mileage: data.get('mileage'),
    interests: data.getAll('interests'),
  };
  costsEl.innerHTML = '<div class="metric"><span>Status</span><strong>Planning...</strong></div>';
  const response = await fetch('/api/plan/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrfToken },
    body: JSON.stringify(payload),
  });
  const plan = await response.json();
  if (!response.ok) {
    costsEl.innerHTML = `<div class="metric"><span>Error</span><strong>${plan.error}</strong></div>`;
    itineraryEl.innerHTML = `<div class="empty-state">${plan.error}</div>`;
    weatherEl.innerHTML = '<div class="empty-state">Weather loads after a valid trip plan.</div>';
    splitOutputEl.innerHTML = '<div class="empty-state">Group split appears after a valid trip plan.</div>';
    latestPlan = null;
    return;
  }
  latestPlan = plan;
  routeSummaryEl.textContent = `${plan.origin} to ${plan.destination} - ${plan.days} days`;
  drawRoute(plan.route);
  renderCosts(plan.costs);
  renderItinerary(plan);
  renderSplit();
  updateSos(plan);
  await loadWeather(plan.route, plan.days);
  iconRefresh();
}

async function loadPois() {
  const city = document.getElementById('poi-city').value;
  const category = document.getElementById('poi-category').value;
  poiResultsEl.textContent = 'Searching OpenStreetMap...';
  const report = await fetch(`/api/pois/?city=${city}&category=${category}`).then((response) => response.json());
  if (!report.pois.length) {
    poiResultsEl.innerHTML = `<div class="poi-item"><strong>No live results found</strong><span>${report.city}</span>Try another category or city.</div>`;
    return;
  }
  poiResultsEl.innerHTML = report.pois.map((poi) => `
    <div class="poi-item">
      <strong>${poi.name}</strong>
      <span>${report.city} - ${report.category}</span>
    </div>
  `).join('');
}

form.addEventListener('submit', (event) => {
  event.preventDefault();
  planTrip();
});

document.querySelectorAll('[data-view]').forEach((button) => {
  button.addEventListener('click', () => showPanel(button.dataset.view));
});
document.getElementById('load-pois').addEventListener('click', loadPois);
document.getElementById('add-expense').addEventListener('click', () => {
  const nameInput = document.getElementById('expense-name');
  const amountInput = document.getElementById('expense-amount');
  const amount = Number(amountInput.value || 0);
  if (!amount || amount < 0) return;
  expenses.push({ name: nameInput.value.trim() || 'Shared expense', amount });
  nameInput.value = '';
  amountInput.value = '';
  renderSplit();
});
document.getElementById('emergency-contact').addEventListener('input', () => {
  if (latestPlan) updateSos(latestPlan);
});

document.addEventListener('DOMContentLoaded', () => {
  initMap();
  iconRefresh();
});
