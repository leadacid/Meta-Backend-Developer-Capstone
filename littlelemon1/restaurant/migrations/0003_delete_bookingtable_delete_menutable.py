# Generated by Django 4.2.5 on 2023-09-21 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_menuitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookingTable',
        ),
        migrations.DeleteModel(
            name='MenuTable',
        ),
    ]