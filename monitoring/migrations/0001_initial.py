# Generated for AirAware initial database schema.
import django.utils.timezone
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='MonitoringStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('location_name', models.CharField(max_length=180)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('source', models.CharField(default='Illustrative demo data', max_length=120)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PollutionReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('report_type', models.CharField(choices=[('smoke', 'Smoke / burning'), ('dust', 'Construction or road dust'), ('traffic', 'Heavy traffic emissions'), ('odor', 'Strong chemical or unusual odour'), ('other', 'Other')], max_length=20)),
                ('description', models.TextField(max_length=1500)),
                ('location_name', models.CharField(max_length=180)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('reviewed', models.BooleanField(default=False)),
            ],
            options={'ordering': ['-created_at']},
        ),
        migrations.CreateModel(
            name='AirQualityReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recorded_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('aqi', models.PositiveIntegerField()),
                ('pm25', models.FloatField(blank=True, help_text='PM2.5 concentration in µg/m³', null=True)),
                ('pm10', models.FloatField(blank=True, help_text='PM10 concentration in µg/m³', null=True)),
                ('is_demo', models.BooleanField(default=True)),
                ('quality_note', models.CharField(blank=True, max_length=180)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='readings', to='monitoring.monitoringstation')),
            ],
            options={'ordering': ['-recorded_at']},
        ),
    ]
