from music_api_project.music_app.models import Song
from django.contrib import admin
from .models import Song

# Register your models here.
admin.site.register(Song)