# Generated by Django 4.0.1 on 2022-02-16 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_add_service_time_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='dependencies',
            field=models.ManyToManyField(blank=True, related_name='dependants', to='services.Service'),
        ),
    ]
