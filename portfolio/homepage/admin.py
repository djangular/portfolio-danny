from django.contrib import admin
from .models import Photo

class photoAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']


    class Meta:
        model = Photo


admin.site.register(Photo, photoAdmin)
