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
  let acc = new Accelerometer({ frequency : 1 });
  acc.onreading = () => {
    xval.innerHTML = acc.x.toFixed(3);
    yval.innerHTML = acc.y.toFixed(3);
    zval.innerHTML = acc.z.toFixed(3);
  }
  acc.start();
}
