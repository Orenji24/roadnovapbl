# RoadNova India

RoadNova is a Django road-trip planner for India with city-to-city itinerary generation, OpenStreetMap maps, Open-Meteo weather, fuel/toll/cost estimates, SOS tools, and group expense splitting.

## Run it

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe backend\manage.py migrate
.\.venv\Scripts\python.exe backend\manage.py seed_roadnova
.\.venv\Scripts\python.exe backend\manage.py runserver
```

Open http://127.0.0.1:8000/.

## Deploy

This project includes `render.yaml`, `Procfile`, `runtime.txt`, WhiteNoise static file support, and Gunicorn so it can run as a deployed Django web app. GitHub by itself only hosts the code; connect the GitHub repo to Render or another Python web host to get a live app URL.

## Useful commands

```powershell
.\.venv\Scripts\python.exe backend\manage.py test trips
.\.venv\Scripts\python.exe backend\manage.py createsuperuser
```
