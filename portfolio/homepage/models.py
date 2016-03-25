from django.db import models




class Photo(models.Model):
    title       = models.CharField(max_length=100, null=True, blank=True)
    file        = models.ImageField(upload_to="static/images", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created  = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated  = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title


class Message(models.Model):
    name    = models.CharField(max_length=65, null=True, blank=True)
    email   = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.email