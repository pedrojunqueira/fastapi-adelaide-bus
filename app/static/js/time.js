"strict mode";

function getTime() {
  const clock = new Date();
  const hour = clock.getHours();
  const min = String(clock.getMinutes());
  const displayTime = `${hour}:${min.padStart(2, "0")}`;
  return displayTime;
}

const timeDOM = document.querySelector("#time");

timeDOM.textContent = getTime();

setInterval(function () {
  timeDOM.textContent = getTime();
}, 10000);
