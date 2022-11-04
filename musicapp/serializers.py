from rest_framework import serializers

from .models import Song, Artiste

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'artiste_id', 
            'title',
            'likes',
            'date_released',
        )
        model = Song

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
       
        fields = (
            'id',
            'first_name',
            'last_name',
            'age',
        )
        model = Artiste
