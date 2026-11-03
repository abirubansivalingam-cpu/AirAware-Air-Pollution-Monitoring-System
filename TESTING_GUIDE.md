# AirAware testing guide (Windows CMD)

Open CMD in the folder containing `manage.py`.

## Check configuration
```cmd
.venv\Scripts\python.exe manage.py check
```
Expected: `System check identified no issues`.

## Apply database schema
```cmd
.venv\Scripts\python.exe manage.py migrate
```
The project includes `monitoring/migrations/0001_initial.py`, so Django creates the station, reading and report tables without requiring you to generate a migration manually.

## Load sample data
```cmd
.venv\Scripts\python.exe manage.py load_demo_data
```
The command should state that illustrative demo values were loaded. It is safe to rerun.

## Run automated tests
```cmd
.venv\Scripts\python.exe manage.py test
```
Review the test summary. If a test fails, copy the full error to your developer/support notes and fix it before presenting the project.

## Start and stop
```cmd
.venv\Scripts\python.exe manage.py runserver 8080
```
Open `http://127.0.0.1:8080/`. Stop the server with `CTRL+C` in that CMD window.

## Manual feature checklist
- [ ] Dashboard shows station rows and sample data warning.
- [ ] Map markers open popups.
- [ ] Chart shows one latest value per station.
- [ ] CSV download opens and contains station/readings columns.
- [ ] Report form accepts a valid report and shows it on the dashboard.
- [ ] Report form rejects invalid coordinates or only one coordinate.
- [ ] Exposure form calculates concentration × hours.
- [ ] Exposure form rejects negative values and more than 24 hours.
- [ ] Admin login can edit stations/readings and mark reports reviewed.
