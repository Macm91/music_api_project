from django.http.response import Http404
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

class SongDetail (APIView):
    def get_objects(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        song= self.get_objects(pk)
        serializer = songSerializer(song)
        return Response (serializer.data)

    def put (self, request, pk):
        song = self.get_objects(pk)
        serializer = songSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete (self, request, pk):
        song = self.get_objects(pk)
        song.delete()
        return Response (status= status.HTTP_204_NO_CONTENT)

