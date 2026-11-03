import csv
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import PollutionReportForm, ExposureForm
from .models import AirQualityReading, MonitoringStation, PollutionReport

def dashboard(request):
    latest = []
    for station in MonitoringStation.objects.filter(is_active=True):
        reading = station.readings.first()
        if reading:
            latest.append({
                "station": station, "reading": reading, "category": reading.category(),
                "level": "high" if reading.aqi > 200 else ("medium" if reading.aqi > 100 else "low"),
            })
    latest.sort(key=lambda item: item["reading"].aqi, reverse=True)
    readings = list(AirQualityReading.objects.select_related("station").order_by("-recorded_at")[:40])
    # Chart shows the latest reading per station; avoids pretending sparse demo readings form a continuous time series.
    chart_labels = [x["station"].name for x in latest]
    chart_aqi = [x["reading"].aqi for x in latest]
    map_points = [{
        "name": x["station"].name, "location": x["station"].location_name,
        "lat": x["station"].latitude, "lon": x["station"].longitude,
        "aqi": x["reading"].aqi, "category": x["category"],
    } for x in latest]
    context = {
        "latest": latest, "stations_count": MonitoringStation.objects.filter(is_active=True).count(),
        "reports_count": PollutionReport.objects.filter(reviewed=False).count(),
        "high_count": sum(1 for x in latest if x["reading"].aqi > 200),
        "map_points_json": __import__("json").dumps(map_points),
        "chart_labels_json": __import__("json").dumps(chart_labels),
        "chart_aqi_json": __import__("json").dumps(chart_aqi),
        "recent_reports": PollutionReport.objects.all()[:5],
        "updated": timezone.localtime(),
    }
    return render(request, "monitoring/dashboard.html", context)

def submit_report(request):
    if request.method == "POST":
        form = PollutionReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Report submitted for review. Thank you for contributing.")
            return redirect("dashboard")
    else:
        form = PollutionReportForm()
    return render(request, "monitoring/report.html", {"form": form})

def exposure(request):
    result = None
    if request.method == "POST":
        form = ExposureForm(request.POST)
        if form.is_valid():
            c = form.cleaned_data["concentration"]
            h = form.cleaned_data["hours"]
            result = {"dose": round(c * h, 2), "concentration": c, "hours": h}
    else:
        form = ExposureForm()
    return render(request, "monitoring/exposure.html", {"form": form, "result": result})

def export_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="airaware_readings.csv"'
    writer = csv.writer(response)
    writer.writerow(["station", "location", "recorded_at", "AQI", "PM2.5_ug_m3", "PM10_ug_m3", "is_demo", "quality_note"])
    for r in AirQualityReading.objects.select_related("station").order_by("-recorded_at"):
        writer.writerow([r.station.name, r.station.location_name, r.recorded_at.isoformat(), r.aqi, r.pm25, r.pm10, r.is_demo, r.quality_note])
    return response
