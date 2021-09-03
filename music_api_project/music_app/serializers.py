from django.db.models import fields
from rest_framework import serializers
from .models import Song


class songSerializer (serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'release_date']


