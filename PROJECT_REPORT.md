# AirAware: Air-Pollution Monitoring and Exposure Mapping

## Abstract
AirAware is a web-based prototype intended to make air-quality information easier to inspect in a spatial context. It provides a dashboard of station readings, an interactive map, a comparison chart, a community observation form, a simple concentration-time estimator, and CSV export. The application is built with Django and SQLite, with Bootstrap for the interface, Leaflet for map rendering, and Chart.js for visualisation. The supplied readings are synthetic demonstration data; the prototype does not claim to provide real-time or officially validated pollution measurements. The project establishes a modular foundation for later integration with a permitted official data feed or calibrated sensors.

## 1. Problem statement
Air-quality values can be difficult for students and community members to interpret when they are separated from location, timestamp, source and context. A small web application can consolidate readings and observations into a single interface, while making the limitations and provenance of data visible.

## 2. Aim
To design and implement a web-based prototype for visualising air-quality readings by location and collecting community pollution observations.

## 3. Objectives
- Display the latest stored reading for each active monitoring station.
- Present station coordinates on an interactive map.
- Compare latest station AQI values in a chart.
- Allow a user to submit a pollution observation with optional coordinates.
- Validate user-entered coordinates and exposure calculator inputs.
- Calculate a simple concentration × duration index with explanatory limitations.
- Export stored readings in CSV format.
- Provide an administration interface for managing stations, readings and reports.
- Test core routes and workflows with Django's test framework.

## 4. Scope and limitations
The current implementation is a student prototype using synthetic demo values and illustrative locations. It does not ingest live sensor data, calculate an official AQI from raw pollutant concentrations, predict pollution, identify individual health risk, or calculate inhaled dose. The map, Bootstrap, Chart.js and Leaflet resources use external CDNs and OpenStreetMap tiles, so those visual resources need an internet connection. The app should not be used for medical, emergency or regulatory decisions.

## 5. Technology stack
- Python and Django: server-side logic, routing, forms, ORM and administration.
- SQLite: local relational database for the prototype.
- HTML/CSS and Bootstrap: responsive user interface.
- Leaflet and OpenStreetMap tiles: map visualisation.
- Chart.js: chart of latest station AQI values.
- Django TestCase: automated application tests.

## 6. System architecture
1. Presentation layer: dashboard and forms rendered by Django templates.
2. Application layer: views validate requests, prepare dashboard summaries, calculate the concentration-time index and export CSV.
3. Data layer: Django models persist monitoring stations, air-quality readings and pollution reports in SQLite.
4. Administration layer: Django admin lets an authorised administrator maintain station/reading records and review reports.
5. Visualisation layer: Leaflet renders map markers and Chart.js renders a station comparison chart in the browser.

## 7. Database design

### MonitoringStation
Stores station name, location label, latitude, longitude, source description and active status. One station can have many readings.

### AirQualityReading
Stores station reference, timestamp, AQI value, optional PM2.5 and PM10 values, demo-data flag and a quality note. Each reading belongs to one station.

### PollutionReport
Stores title, report type, description, location label, optional coordinates, submission timestamp and reviewed status. Reports are displayed as unverified observations until reviewed.

## 8. Main modules
1. Dashboard and summary counts.
2. Monitoring station and reading display.
3. Simplified AQI category labels.
4. Interactive map.
5. Latest AQI comparison chart.
6. Community pollution report submission.
7. Coordinate validation.
8. Report review through Django admin.
9. Exposure concentration-time estimator.
10. Exposure input validation.
11. CSV export.
12. Demo-data loader.
13. Database migrations.
14. Django admin management.
15. Automated tests and project documentation.

## 9. Methodology
The prototype follows an iterative development process: requirements definition, data-model design, implementation of routes and forms, integration of visualisations, test writing, and review of limitations. Synthetic records are used to verify the user interface and data flow without implying access to a live monitoring network. Future evaluation should use a clearly documented and authorised dataset, compare displayed values with source records, measure input-validation outcomes, and collect usability feedback under an approved process.

## 10. Test plan
Run `python manage.py test` after installing dependencies and applying migrations. Included automated tests verify dashboard response and station rendering, CSV response, exposure page loading and calculation, rejection of out-of-range exposure duration, report submission, and invalid coordinate rejection. Record the actual test output in the final submission rather than claiming a result without running it.

## 11. Future enhancements
- Integrate a documented official data API or calibrated sensors.
- Record source URL/provider, units, observation time, ingestion time and data-quality flags for each imported reading.
- Implement scheduled ingestion with retries and stale-data warnings.
- Add authentication and moderation workflows for community reports.
- Add time-series filtering and downloadable reports.
- Validate the AQI calculation against the selected country's official methodology.
- Deploy with production security controls and conduct a user evaluation.

## 12. Conclusion
AirAware demonstrates how a full-stack web application can combine stored air-quality readings, a map, a chart, community observations and CSV export. Its current value is as a functional educational prototype. Reliable real-world use depends on integrating verified data, implementing jurisdiction-specific AQI methods, and conducting systematic validation and security review.
