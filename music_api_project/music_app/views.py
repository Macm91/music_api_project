from django.shortcuts import render
from .models import Song
from .serializers import songSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status


# Create your views here.

class SongList (APIView):
    
    def get(self, request):
        song = Song.objects.all()
        serializers = songSerializer(song, many = True)
        return Response(serializers.data)

    def post(self, request):
        serializers=songSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response (serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)