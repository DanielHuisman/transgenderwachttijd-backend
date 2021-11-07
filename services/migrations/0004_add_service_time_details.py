# Generated by Django 3.2.9 on 2021-11-07 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_add_service_medical_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetime',
            name='has_stop',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicetime',
            name='is_individual',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicetime',
            name='days',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
