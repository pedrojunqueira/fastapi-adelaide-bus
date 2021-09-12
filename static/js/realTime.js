const stop = JSON.parse(document.getElementById("stop").dataset.code);

const stopCode = stop.code;

const getRealTime = async () => {
  const res = await fetch(`/api/real_time/${stopCode}`);
  const nextServices = await res.json();

  console.log(nextServices);

  nextServices.forEach((service) => {
    const tripId = service.trip_id;

    const arriveInEl = document.getElementById(tripId);
    const iconElement = document.getElementById(`icon-${tripId}`);

    if (arriveInEl) {
      arriveInEl.textContent = service.arrives_in;
      iconElement.classList.remove("hide-icon");
    }
  });
};

getRealTime();

setInterval(function () {
  location.reload();
}, 100000);
