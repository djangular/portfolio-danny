from django.contrib import admin
from models import Photo


class PhotoAdmin(admin.ModelAdmin):

    class Meta:
        model=Photo


admin.site.register(Photo, PhotoAdmin)
