# Generated by Django 5.1.4 on 2024-12-07 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_eventregistration'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EventRegistration',
        ),
    ]