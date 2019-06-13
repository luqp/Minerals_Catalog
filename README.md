# Minerals Catalog
This project use Django to build a website that displays information about various minerals (AKA rocks).
The home page redirect you to a site that contains a list of all of the minerals in a database.
Clicking on a mineral’s name opens a page that displays information about the mineral.

## To use
You need create a new virtual Python environment:
```
python3 -m venv env
```
### Activate your new virtual Python environment
```
source ./env/bin/activate
```
If using Windows:
```
.\env\Scripts\activate
```
## Requirements
This project use some requirements located on requirements.txt file:
```
pip3 install -r requirements.txt
```

## Run app
To run the app you need to enter in catalog folder and run the server like following:
```
(env) ...\Minerals_Catalog> cd .\catalog\
(env) ...\Minerals_Catalog\catalog> python manage.py runserver
```
To see the webpage you have to make `ctrl + click` in `http://127.0.0.1:8000/`this open a new window in your brouser
```
...
Django version 2.2.2, using settings 'catalog.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

# Catalog
This project contains 874 items with one image each.
<p align="center">
  <img src="https://github.com/windyludev/Minerals_Catalog/blob/master/catalog/assets/img/list-preview.png">
</p>
