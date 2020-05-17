// Getting values from document
let xval = document.getElementById('x_value');
let yval = document.getElementById('y_value');
let zval = document.getElementById('z_value');
let derr = document.getElementById('div-error');
let dact = document.getElementById('div-activity');

let acc = new Accelerometer({ frequency : 1 });

// global vars
let mag = 0;
let pippo = 0;

// Thingsboard stuffs
const ACCESS_TOKEN_G = '6WTHnnVbJdlrX8QcOSWj';
const TOPIC = 'https://demo.thingsboard.io/api/v1/' + ACCESS_TOKEN_G +'/telemetry';
const PORT = 1883;
let http = new XMLHttpRequest();

let vals = {
  'x' : xval.innerHTML,
  'y' : yval.innerHTML,
  'z' : zval.innerHTML
};

let activity = {
  'moving' : 0
};

let telemetry = JSON.stringify(activity);

// Load the code when the page is ready
$(document).ready(() => {
  try {
    if (window.Accelerometer) {
      this.getAccelerometerValues();
    } else {
      derr.innerHTML = 'Accelerometer not available';
    }
  } catch (error) {
    derr.innerHTML = error;
  }
});

// Gets data from the accelerometer with an update frequency of 1 Hz and
// puts the data into the corresponding field of the html page.
function getAccelerometerValues() {
  acc.onreading = () => {
    // Data must be sent on reading!
    this.sendValues();
  }
  acc.start();
}

// Send values to thingsboard
function sendValues() {
  http = new XMLHttpRequest();
  http.open("POST", TOPIC);
  mag = getTotalAcceleration();
  pippo = Math.abs(mag - 9.81);
  if (pippo > 0.12) {
    activity.moving = 1;
    telemetry = JSON.stringify(activity);
    http.send(telemetry);
    dact.style.background = 'green';
    dact.innerHTML = "<b> Moving </b>" + pippo.toFixed(3);
  } else {
    activity.moving = 0;
    telemetry = JSON.stringify(activity);
    http.send(telemetry);
    dact.style.background = 'blue';
    dact.innerHTML = "<b> Stopped </b>" + pippo.toFixed(3);
  }
}

function getTotalAcceleration() {
  vals.x = acc.x.toFixed(3);
  vals.y = acc.y.toFixed(3);
  vals.z = acc.z.toFixed(3);
  return Math.sqrt( (vals.x * vals.x) + (vals.y * vals.y) + (vals.z * vals.z) );
}
