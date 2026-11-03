from django.contrib import admin
from .models import MonitoringStation, AirQualityReading, PollutionReport

@admin.register(MonitoringStation)
class StationAdmin(admin.ModelAdmin):
    list_display = ("name", "location_name", "latitude", "longitude", "is_active")
    search_fields = ("name", "location_name")

@admin.register(AirQualityReading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ("station", "recorded_at", "aqi", "pm25", "pm10", "is_demo")
    list_filter = ("is_demo", "recorded_at")
    date_hierarchy = "recorded_at"

@admin.register(PollutionReport)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("title", "report_type", "location_name", "created_at", "reviewed")
    list_filter = ("report_type", "reviewed")
    search_fields = ("title", "location_name", "description")
