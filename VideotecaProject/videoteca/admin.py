from django.contrib import admin
from videoteca.models import Movie, MovieType

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'type']
    list_filter = ['type']

admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieType)
