const search = document.getElementById("search");
const matchList = document.getElementById("match-list");

// // search bus stops

const searchStops = async (searchText) => {
  const res = await fetch("/api/get_stops");

  const stops = await res.json();

  // Get matches

  let matches = stops.filter((stop) => {
    const regex = new RegExp(`${searchText}`, "gi");
    return stop.name.match(regex) || stop.address.match(regex);
  });

  if (search.value === "") {
    matches = [];
    matchList.innerHTML = "";
  }

  if (matches.length === 0) {
    matches = [];
    matchList.innerHTML = "";
  }

  renderHtml(matches);
};

apiEndPoint = `/stop/`;

function renderHtml(matches) {
  if (matches.length > 0) {
    const html = matches
      .map(
        (match) => `
        <div class="card text-center mb-1">
        <div class="card-header">
            <a href="${apiEndPoint}${match.code}">
            <h5>${
              match.name.split(" ")[0] == "Stop"
                ? match.name.split(" ").slice(1).join(" ")
                : match.name
            }</h5> </a>
        </div>
        <h6 class="mt-2" >${match.address}</h6>
        <small class="text-muted" >lat: ${parseFloat(match.lat).toFixed(
          4
        )} lon: ${parseFloat(match.lon).toFixed(4)}</small>
        </div>`
      )
      .join("");

    matchList.innerHTML = html;
  }
}

search.addEventListener("input", () => searchStops(search.value));
