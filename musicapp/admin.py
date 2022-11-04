from django.contrib import admin
from .models import Song, Artiste, lyric

# Register your models here.
admin.site.register(Song)
admin.site.register(Artiste)
admin.site.register(lyric)
