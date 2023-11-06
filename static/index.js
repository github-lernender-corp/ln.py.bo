const TIMEOUT_SECONDS = 5000; // 5 Seconds
//
// render() Data via DOM API
//
function render(data) {
  console.log('Render data')
}

//
// reload()
//
function reload() {
  var id = null;
  var url = `/api/sensor?id=${id}`;
  fetch(url)
    .then((response) => response.json())
    .then((json) => {
      render(json);
    });
}
//
// continual loop
//
(function loop() {
  setTimeout(() => {
    reload();
    loop();
  }, TIMEOUT_SECONDS);
})();
