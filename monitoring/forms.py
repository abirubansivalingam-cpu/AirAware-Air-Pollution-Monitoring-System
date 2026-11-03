from django import forms
from .models import PollutionReport


class PollutionReportForm(forms.ModelForm):
    class Meta:
        model = PollutionReport
        fields = ["title", "report_type", "description", "location_name", "latitude", "longitude"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "latitude": forms.NumberInput(attrs={"step": "any", "placeholder": "Optional latitude"}),
            "longitude": forms.NumberInput(attrs={"step": "any", "placeholder": "Optional longitude"}),
        }

    def clean(self):
        cleaned = super().clean()
        lat = cleaned.get("latitude")
        lon = cleaned.get("longitude")
        if (lat is None) != (lon is None):
            raise forms.ValidationError("Enter both latitude and longitude, or leave both blank.")
        if lat is not None and not -90 <= lat <= 90:
            self.add_error("latitude", "Latitude must be between -90 and 90.")
        if lon is not None and not -180 <= lon <= 180:
            self.add_error("longitude", "Longitude must be between -180 and 180.")
        return cleaned


class ExposureForm(forms.Form):
    concentration = forms.FloatField(
        min_value=0, max_value=2000,
        label="PM2.5 concentration (µg/m³)",
        help_text="Enter a measured or assumed concentration between 0 and 2000 µg/m³.",
    )
    hours = forms.FloatField(min_value=0, max_value=24, label="Hours exposed (0–24)")
