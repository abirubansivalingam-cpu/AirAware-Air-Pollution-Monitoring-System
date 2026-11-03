# AirAware — Air-Pollution Monitoring and Exposure Mapping

**Project code:** NECPS26375  
**Project type:** MCA full-stack web application prototype  
**Stack:** Python, Django 5.2, SQLite, Bootstrap, Leaflet, Chart.js

AirAware presents air-quality readings by monitoring station, shows station markers on a map, charts the latest AQI by station, accepts community observations, estimates a simple concentration-time index, and exports readings to CSV.

## Important scope and data notice

The bundled data is **illustrative demonstration data only**. The station coordinates and values are not official, current or verified measurements. The dashboard labels the data as demo data. The concentration × time result is an educational index, not a measured inhaled dose, medical assessment or health-risk prediction. For a real deployment, integrate a documented and permitted official data source or calibrated sensors, preserve source timestamps/units, validate data quality, and show provenance on every reading.

## Requirements

- Python 3.10 or newer (the project has been used with Django 5.2 in the supplied development setup)
- Internet connection for installing Django and loading Bootstrap/Leaflet/Chart.js and OpenStreetMap tiles
- No sensor, API key or PostgreSQL is needed for the demo; SQLite is configured by default

## Windows CMD: first-time setup

1. Extract the ZIP into a folder such as `C:\Users\YOUR_NAME\Downloads\AirAware`.
2. Open that folder in File Explorer, click the address bar, type `cmd`, and press Enter. Confirm `dir` shows `manage.py` and `requirements.txt` in the same folder.
3. Run these commands one at a time:

```cmd
py -m venv .venv
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe manage.py migrate
.venv\Scripts\python.exe manage.py load_demo_data
.venv\Scripts\python.exe manage.py createsuperuser
.venv\Scripts\python.exe manage.py test
.venv\Scripts\python.exe manage.py runserver 8080
```

Open the dashboard at `http://127.0.0.1:8080/`. Open the administration panel at `http://127.0.0.1:8080/admin/` and use the superuser credentials you created. Keep CMD open while the server is running. Press `CTRL+C` to stop it.

### If the virtual environment is already in a parent folder

If `manage.py` is in an inner folder but `.venv` is in its parent, run commands from the inner folder using `..\.venv\Scripts\python.exe` instead. Prefer extracting this clean ZIP into a new folder so `manage.py` and `.venv` are together.

## Main URLs

- `/` — dashboard, map, latest readings, community reports
- `/report/` — submit a community pollution observation
- `/exposure/` — concentration × time educational estimator
- `/readings.csv` — export stored readings as CSV
- `/admin/` — manage stations, readings and reports

## Database and demo data

The initial schema migration is included. `migrate` creates the required tables. `load_demo_data` can be run more than once; it updates the named demo stations and creates/updates illustrative readings. The database is stored in `db.sqlite3` beside `manage.py`.

## Project modules

1. Air-quality dashboard
2. Monitoring station registry
3. Air-quality reading registry
4. AQI display categories (simplified display bands)
5. Interactive map
6. Latest AQI chart
7. Community pollution report form
8. Coordinate input validation
9. Admin review of community reports
10. Exposure concentration-time calculator
11. Exposure input validation
12. CSV export
13. Data provenance/demo flags
14. SQLite persistence and migrations
15. Automated Django tests and documentation

## Testing

Run `.venv\Scripts\python.exe manage.py test`. Tests cover dashboard rendering, CSV export, report creation/coordinate validation, and exposure calculations/input limits.

## Before academic submission or public deployment

- Add a real, documented data source or calibrated sensor integration; do not describe demo values as live.
- Validate AQI categories and formulas against the chosen jurisdiction's official methodology.
- Add authentication, rate limiting, moderation/spam controls and privacy notice if reports become public.
- Use environment-managed secret keys, `DEBUG=False`, a production server, HTTPS, secure cookies, backups and a security review before deployment.
- Conduct a documented evaluation using source-grounded data, test cases, usability feedback and limitations.
