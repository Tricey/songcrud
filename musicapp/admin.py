from django.contrib import admin
from .models import song, Artiste, lyric

# Register your models here.
admin.site.register(song)
admin.site.register(Artiste)
admin.site.register(lyric)
