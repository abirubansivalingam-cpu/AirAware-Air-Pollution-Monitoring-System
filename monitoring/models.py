from django.db import models
from django.utils import timezone

class MonitoringStation(models.Model):
    name = models.CharField(max_length=120)
    location_name = models.CharField(max_length=180)
    latitude = models.FloatField()
    longitude = models.FloatField()
    source = models.CharField(max_length=120, default="Illustrative demo data")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} — {self.location_name}"

class AirQualityReading(models.Model):
    station = models.ForeignKey(MonitoringStation, on_delete=models.CASCADE, related_name="readings")
    recorded_at = models.DateTimeField(default=timezone.now)
    aqi = models.PositiveIntegerField()
    pm25 = models.FloatField(null=True, blank=True, help_text="PM2.5 concentration in µg/m³")
    pm10 = models.FloatField(null=True, blank=True, help_text="PM10 concentration in µg/m³")
    is_demo = models.BooleanField(default=True)
    quality_note = models.CharField(max_length=180, blank=True)

    class Meta:
        ordering = ["-recorded_at"]

    def category(self):
        # Simplified display bands for prototype only; official AQI calculation is pollutant- and jurisdiction-specific.
        if self.aqi <= 50: return "Good"
        if self.aqi <= 100: return "Satisfactory / Moderate"
        if self.aqi <= 200: return "Moderate"
        if self.aqi <= 300: return "Poor"
        if self.aqi <= 400: return "Very Poor"
        return "Severe"

    def __str__(self):
        return f"{self.station.name}: AQI {self.aqi} ({self.recorded_at:%Y-%m-%d %H:%M})"

class PollutionReport(models.Model):
    REPORT_TYPES = [
        ("smoke", "Smoke / burning"), ("dust", "Construction or road dust"),
        ("traffic", "Heavy traffic emissions"), ("odor", "Strong chemical or unusual odour"),
        ("other", "Other"),
    ]
    title = models.CharField(max_length=120)
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    description = models.TextField(max_length=1500)
    location_name = models.CharField(max_length=180)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    reviewed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
