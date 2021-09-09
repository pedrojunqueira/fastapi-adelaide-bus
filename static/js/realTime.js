const stop = JSON.parse(document.getElementById("stop").dataset.code);

const stopCode = stop.code;

const getRealTime = async () => {
  const res = await fetch(`/api/next_services/${stopCode}`);
  const nextServices = await res.json();

  console.log(nextServices);

  const elIds = nextServices.map((el) => `${el.route}-${el.destination}`);

  elIds.forEach((element) => {
    let el = document.getElementById("190-City");

    el.textContent = "Now";
  });
};

// setInterval(function () {
//   getRealTime();
// }, 3000);
