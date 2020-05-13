let xval = document.getElementById('x_value');
let yval = document.getElementById('y_value');
let zval = document.getElementById('z_value');

$(document).ready(() => {
  try {
    if (window.Accelerometer) {
      document.getElementById("div-error").innerHTML = 'This stuff seems to work';
    } else {
      console.log({ error: "Generic API Accelerometer not available" });
      document.getElementById("div-error").innerHTML = 'NOT WORKING';
    }
  } catch (error) {
    console.log({ error: error });
    document.getElementById("div-error").innerHTML = 'Errrrrrr';

  }
});
