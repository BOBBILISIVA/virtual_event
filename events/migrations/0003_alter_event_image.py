# Generated by Django 5.1.4 on 2024-12-07 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_rename_attendees_event_registered_users_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, default='event_images/download.jpeg', null=True, upload_to='event_images/'),
        ),
    ]
