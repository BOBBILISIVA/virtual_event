from django.contrib import admin
from .models import Event, Note

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'venue', 'created_by')
    search_fields = ('name', 'venue', 'created_by__username')
    list_filter = ('date', 'venue')

from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created_at', 'updated_at')  # Make sure these fields exist

admin.site.register(Note, NoteAdmin)
