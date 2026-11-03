from django.test import TestCase
from django.urls import reverse
from monitoring.models import MonitoringStation, AirQualityReading, PollutionReport


class AirAwareSmokeTests(TestCase):
    def setUp(self):
        self.station = MonitoringStation.objects.create(
            name="Test station", location_name="Test location",
            latitude=11.0, longitude=76.9,
        )
        AirQualityReading.objects.create(
            station=self.station, aqi=75, pm25=22, pm10=40,
            is_demo=True, quality_note="Test reading",
        )

    def test_dashboard_loads(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Know the air around you")
        self.assertContains(response, "Test station")

    def test_csv_export(self):
        response = self.client.get(reverse("export_csv"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/csv", response["Content-Type"])
        self.assertContains(response, "Test station")

    def test_exposure_page_loads(self):
        response = self.client.get(reverse("exposure"))
        self.assertEqual(response.status_code, 200)

    def test_exposure_calculation(self):
        response = self.client.post(reverse("exposure"), {"concentration": "20", "hours": "3"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "60.0")

    def test_exposure_rejects_more_than_24_hours(self):
        response = self.client.post(reverse("exposure"), {"concentration": "20", "hours": "25"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ensure this value is less than or equal to 24")

    def test_report_page_loads(self):
        response = self.client.get(reverse("submit_report"))
        self.assertEqual(response.status_code, 200)

    def test_report_submission(self):
        response = self.client.post(reverse("submit_report"), {
            "title": "Smoke near road", "report_type": "smoke",
            "description": "Observed smoke for several minutes.",
            "location_name": "Test road", "latitude": "11.0", "longitude": "76.9",
        })
        self.assertRedirects(response, reverse("dashboard"))
        self.assertEqual(PollutionReport.objects.count(), 1)

    def test_report_rejects_invalid_coordinates(self):
        response = self.client.post(reverse("submit_report"), {
            "title": "Invalid location", "report_type": "dust",
            "description": "Dust observed.", "location_name": "Test road",
            "latitude": "111", "longitude": "76.9",
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(PollutionReport.objects.count(), 0)
