# Generated by Django 4.0.5 on 2022-12-20 07:05

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_jinn_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stores',
            name='coordinates',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]