# Crowd_Sensing
In this assignment we will build a mobile application to provide a crowd-sensing extension to our application.

You need to develop an HTML5 application using the [Generic Sensor API](https://www.w3.org/TR/generic-sensor/) that collects data form the [accelerator sensor of the mobile phone](https://intel.github.io/generic-sensor-demos/).

Refs @ http://ichatz.me/Site/InternetOfThings2020-Assignment4

## Repository Structure

The repo is structured into five main files:

- index.html : [view](https://pank0.github.io/iot-project/Crowd_Sensing/index.html) for the cloud-based deployment. 
- cloud.js : javascript code that gets the values from the accelerometer and sends them to the cloud.
- edge.html : [view](https://pank0.github.io/iot-project/Crowd_Sensing/edge.html) for the edge-based deployment. Also provides a status section for the state of the user.
- edge.js : javascript code that gets the values from the accelerometer, computes the user status and sends it to the cloud.
- styles.css : css for the beautiful yellow web page.


## Requirements

- Device with accelerometer sensor
- Chrome 63 or later
- Use of [GitHub Pages](https://pages.github.com/)

## From page to Thingsboard
Differently from previous systems, now data are sent to [Thingsboard](https://demo.thingsboard.io/home) using HTTP protocol. 

So now we have to do a POST request to the dedicated URL.
Note that here I have called it `TOPIC` to maintain a sort of simmetry with what I did in the previous assignments, to have a conceptually identical structure.

The URL also contains the Access Token of the Thingsboard device: if you want to reproduce your own project you have to modify this token with yours.

[![http.png](https://i.postimg.cc/26MQzbSH/http.png)](https://postimg.cc/ft7tCbXX)

Data are sent when they are extracted.

The sampling of the values comes at a frequence of 1Hz: this means that one time per second data are taken and then they are elaborated (if needed) and sent.


## Cloud-based Deployment

The activity recognition model is performed into the cloud. The web page for this part of the project is available [here](https://pank0.github.io/iot-project/Crowd_Sensing/).

Through the `cloud.js` script the accelerometer values are extracted and then they are sent to [Thingsboard](https://demo.thingsboard.io/home) using HTTP protocol.

Data are taken using the [Generic Sensor API](https://www.w3.org/TR/generic-sensor/) that collects data form the [accelerator sensor of the mobile phone](https://intel.github.io/generic-sensor-demos/). 

When the script gets the data simply puts them into the html page and then send them to Thingsboard.

To perform a cloud model recognition on Thingsboard it's important to operate on the **rule chains**.

| Modified Root Rule Chain  | Interceptor Script |
| ------------- | ------------- |
|[![rulechain1.png](https://i.postimg.cc/VNzz5DVT/rulechain1.png)](https://postimg.cc/PCVgRzhz)  | [![rulechain2.png](https://i.postimg.cc/Mp7WWhdV/rulechain2.png)](https://postimg.cc/YvScRycC) |

In my implementation I have simply modified the **root rulechain** adding a script called **"Interceptor"** that is charged of recognizing if the data are coming from the wanted device. 


In our case the device that is accepting accelerometer raw data is the one named "**Crowd Sensing G**".

[![rulechain3.png](https://i.postimg.cc/C59F103H/rulechain3.png)](https://postimg.cc/H84GZqsV)

If the Interceptor script recognizes the device it forwards the message to a **new rule chain** named **"Cloud Computation RC"**. Here the black magic happens: the message passes to a new script named **"Model"** where it is computed so that in the device message will be added a new field, the `moving` one that tells us if the user is moving or not.

| New Rule Chain  | Model Script |
| ------------- | ------------- |
|[![rulechain4.png](https://i.postimg.cc/rFtVHd4h/rulechain4.png)](https://postimg.cc/QHhZ9d05)  | [![rulechain5.png](https://i.postimg.cc/DfNf5QSJ/rulechain5.png)](https://postimg.cc/0rpqywdP)  |

In this way it will become possible to take this new information and display it on a dashboard.

**NB** : in the dashboard it's possible to change the realtime display as you prefer.

[![AccCloud.jpg](https://i.postimg.cc/WzMyM7Bq/AccCloud.jpg)](https://postimg.cc/V0k4wXLz)


## Edge-based Deployment

The activity recognition model is performed locally. The web page for this part of the project is available [here](https://pank0.github.io/iot-project/Crowd_Sensing/edge.html).

Through the `edge.js` script the accelerometer values are extracted, they are computed and then they are sent to [Thingsboard](https://demo.thingsboard.io/home) using HTTP protocol.

Data are taken using the [Generic Sensor API](https://www.w3.org/TR/generic-sensor/) that collects data form the [accelerator sensor of the mobile phone](https://intel.github.io/generic-sensor-demos/). 

When the script gets the data it simply puts them into the html page and then send them to Thingsboard.

Differently from above, here it's all happening locally and what is sent is only the parameter **"moving"** with the computed response that can be 0 or 1.

[![moving.png](https://i.postimg.cc/TwWnkVVR/moving.png)](https://postimg.cc/ygsJxSp5)

In the [web view](https://pank0.github.io/iot-project/Crowd_Sensing/edge.html), as you can see, there's a dedicated area that is blue when the user is steady and becomes green as he starts moving.

| Steady User  | Moving User |
| ------------- | ------------- |
|[![Acc-Edge-Stopped.jpg](https://i.postimg.cc/ZRv2qmjc/Acc-Edge-Stopped.jpg)](https://postimg.cc/ftZBH6Gt)  | [![Acc-Edge-Moving.jpg](https://i.postimg.cc/T18SLs4X/Acc-Edge-Moving.jpg)](https://postimg.cc/S2rVHg4Z)|


## User Activity Recognition

To recognize user's activity I have calculated the magnitude of the 3D vector of acceleration data.

The magnitude of a 3D vector can be calculated with:

[![magsqrt.png](https://i.postimg.cc/kG3JJfN2/magsqrt.png)](https://postimg.cc/34159jch)

In this simple calculus, due to empirical experiences, I have set that when the magnitude exceeds a certain value the user's activity is recognized as moving.


## Tutorial
Hackster tutorial [here](https://www.hackster.io/panicik/iot-assignment-4-f9083e)!
Youtube video [here](https://youtu.be/bMXfNftw-ao)!
