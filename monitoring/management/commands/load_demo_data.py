from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from monitoring.models import MonitoringStation, AirQualityReading

class Command(BaseCommand):
    help = "Load clearly labelled illustrative sample data for the AirAware prototype."

    def handle(self, *args, **options):
        # Approximate illustrative points around Coimbatore; not real station locations or actual readings.
        stations = [
            ("Demo Station A", "Central Coimbatore (illustrative)", 11.0168, 76.9558, [82, 96, 112, 128, 104]),
            ("Demo Station B", "Peelamedu area (illustrative)", 11.0280, 77.0260, [65, 74, 88, 91, 79]),
            ("Demo Station C", "Ukkadam area (illustrative)", 10.9925, 76.9614, [135, 158, 181, 169, 147]),
            ("Demo Station D", "Saibaba Colony area (illustrative)", 11.0260, 76.9440, [54, 61, 70, 66, 59]),
            ("Demo Station E", "Singanallur area (illustrative)", 11.0000, 77.0320, [105, 121, 139, 132, 118]),
        ]
        now = timezone.now()
        for name, loc, lat, lon, values in stations:
            station, _ = MonitoringStation.objects.update_or_create(name=name, defaults={
                "location_name": loc, "latitude": lat, "longitude": lon,
                "source": "Illustrative demo data — replace with validated source", "is_active": True,
            })
            for i, aqi in enumerate(values):
                AirQualityReading.objects.update_or_create(
                    station=station, recorded_at=now - timedelta(hours=(len(values)-i-1)*3),
                    defaults={
                        "aqi": aqi, "pm25": round(aqi * 0.42, 1),
                        "pm10": round(aqi * 0.78, 1), "is_demo": True,
                        "quality_note": "Illustrative value; not an official AQI calculation",
                    })
        self.stdout.write(self.style.SUCCESS("Demo data loaded. These are illustrative values, not live measurements."))
