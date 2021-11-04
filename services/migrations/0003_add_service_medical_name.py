# Generated by Django 3.2.6 on 2021-11-04 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_fix_service_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='medical_name',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='service',
            name='medical_name_en',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='service',
            name='medical_name_nl',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
