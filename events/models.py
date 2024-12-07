from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True, default='event_images/download.jpeg')
    registered_users = models.ManyToManyField(User, related_name='registered_events', blank=True)


    def __str__(self):
        return self.name

from django.db import models

from django.db import models

class Note(models.Model):
    # Assuming you want to associate a user with the note
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Example of a user field
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Adding the updated_at field

    def __str__(self):
        return self.title


