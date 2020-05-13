let xval = document.getElementById('x_value');
let yval = document.getElementById('y_value');
let zval = document.getElementById('z_value');
let derr = document.getElementById('div-error');

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

function getAccelerometerValues() {
  let acc = new Accelerometer({ frequency : 10 });
  acc.onreading = () => {
    xval.innerHTML = acc.x;
    yval.innerHTML = acc.y;
    zval.innerHTML = acc.z;
  }
  acc.start();
}
