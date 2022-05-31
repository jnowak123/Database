function getWeather(){

  var key = '14a24dee3920387f8b0cfd6295374d0c'
  var name = document.getElementById('nameField').value  
  var place = document.getElementById('placeField').value

  fetch(`https://api.openweathermap.org/data/2.5/weather?q=${place}&appid=${key}&units=metric`)
    .then(response => response.json())
    .then(data => {

      var temp = data.main.temp
      console.log(typeof(name))
      if (typeof(name) == String){
        temp = name + ', ciepło się ubierz, jest ' + temp + ' stopni'}
      else {temp = 'Ciepło się ubierz, jest ' + temp + ' stopni'}

      document.getElementById('resp').innerHTML = temp
      document.getElementById('resp').style.display ='block'

      var coord = data.coord
      window.initMap(coord.lat, coord.lon) = initMap;
    })
    .catch(error => {
    console.error(error);
    document.getElementById('placeField').value = ''
    document.getElementById('placeField').placeholder = 'Input valid city name'
    document.getElementById('placeField').style.backgroundColor = '#880808'
    });
  document.cookie = `name=${name}`;
}

function getCookie(cname) {
  //Funkcja skopiowana z internetu, wyłuskująca z ciasteczka właściwość o wskazanej w parametrze nazwie.
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
}


function loadSite(){
  let x = getCookie("name")
  document.getElementById('nameField').value = x
}

function initMap(lat, lng) {
  const place = { lat: lat, lng: lng};
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 4,
    center: place,
  });
  const marker = new google.maps.Marker({
    position: place,
    map: map,
  });
}

function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
  