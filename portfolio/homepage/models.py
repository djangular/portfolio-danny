from django.db import models
from django.utils.encoding import smart_unicode


class Photo(models.Model):
    title       = models.CharField(max_length=100, null=True, blank=True)
    thumbnail   = models.ImageField(upload_to='static/images/', null=True, blank=True)
    overlay     = models.ImageField(upload_to='static/images/', null=True, blank=True)
    created     = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated     = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title
