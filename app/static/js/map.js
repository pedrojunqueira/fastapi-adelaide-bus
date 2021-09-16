const stop = JSON.parse(document.getElementById("stop").dataset.stop);
const vehicle = JSON.parse(document.getElementById("vehicle").dataset.vehicle);

const stopLocation = stop.coords;

const vehicleLocation = vehicle.coords;

const markers = [];

markers.push(stopLocation);

if (vehicleLocation.length > 0) {
  markers.push(vehicleLocation);
}

[stopLon, stopLat] = stopLocation;

let maxLon = stopLon;
let maxLat = stopLat;
let minLon = stopLon;
let minLat = stopLat;

markers.forEach((m) => {
  [lon, lat] = m;

  maxLon = maxLon > lon ? maxLon : lon;
  maxLat = maxLat > lat ? maxLat : lat;
  minLon = minLon < lon ? minLon : lon;
  minLat = minLat < lat ? minLat : lat;
});

const sw = displace_coords_meters(200, [minLon, minLat], -1);
const ne = displace_coords_meters(200, [maxLon, maxLat], 1);

mapboxgl.accessToken =
  "pk.eyJ1IjoicGVkcm9qdW5xdWVpcmEiLCJhIjoiY2t0aHBlZTZtMHR5ZzJ2bmwwbzJodGF3MiJ9.yB4PYtsgyI80Nk8L3aniKQ";

var map = new mapboxgl.Map({
  container: "map",
  style: "mapbox://styles/mapbox/streets-v11",
  center: stopLocation,
  zoom: 15,
});

// create bounds object

const bounds = new mapboxgl.LngLatBounds(sw, ne);

// include stop location on bounds
bounds.extend(stopLocation);

stopMarker = document.createElement("div");

stopMarker.className = "marker";

// marker bus stop
new mapboxgl.Marker({
  element: stopMarker,
  anchor: "bottom",
})
  .setLngLat(stopLocation)
  .addTo(map);

if (vehicleLocation.length > 0) {
  // marker bus

  busMarker = document.createElement("div");
  busMarker.className = "bus-marker";

  new mapboxgl.Marker({
    element: busMarker,
    anchor: "bottom",
  })
    .setLngLat(vehicleLocation)
    .addTo(map);

  // Add popup to bus

  new mapboxgl.Popup({
    offset: 24,
  })
    .setLngLat(vehicleLocation)
    .setHTML(`<p>${vehicle.route} - ${vehicle.destination} </p>`)
    .addTo(map);
}

// fit bounds to map

map.fitBounds(bounds);

function displace_coords_meters(m, coords, direction) {
  [lon, lat] = coords;
  const dir = direction;
  const metersShift = m;
  const ratio = 1 / 111111;
  const LatShifted = lat + metersShift * dir * ratio;
  const LonShifted =
    lon + (metersShift * dir * ratio) / Math.cos(lat * (Math.PI / 180));
  return [LonShifted, LatShifted];
}
