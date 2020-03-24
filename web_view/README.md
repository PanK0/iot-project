# Web-based Dashboard
Using your favorite programming language and web development libraries develop a web site that provides the following functionality:

- Display the latest values received from all the sensors of a specified environmental station.
- Display the values received during the last hour from all environmental station of a specified sensor. 

Refs @ http://ichatz.me/Site/InternetOfThings2020-Assignment1

## How To
### If you're running this on your local machine:
- Open the settings.py file at web_view/settings.py
- Comment the first DEBUG variable and uncomment the seconde one

```
# DEBUG = (os.environ.get('DEBUG_VALUE') == 'True')
DEBUG = True
```
- Run the server 

```
python manage.py runserver
```
### If you want to go in the web app:
Go @ https://iotwebapp.herokuapp.com/
