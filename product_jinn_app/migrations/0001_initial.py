# Generated by Django 4.0.5 on 2022-12-17 11:17

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import product_jinn_app.models



class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField(default=0)),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_category', to='product_jinn_app.categories')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_store', to='product_jinn_app.stores')),
            ],
        ),
        migrations.CreateModel(
            name='Prod_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.ImageField(blank=True, null=True, upload_to=product_jinn_app.models.upload_to)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='product_jinn_app.products')),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contact', to='product_jinn_app.stores')),
            ],
        ),
    ]
