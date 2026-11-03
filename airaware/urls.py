from django.contrib import admin
from django.urls import path
from monitoring import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.dashboard, name="dashboard"),
    path("report/", views.submit_report, name="submit_report"),
    path("exposure/", views.exposure, name="exposure"),
    path("readings.csv", views.export_csv, name="export_csv"),
]
