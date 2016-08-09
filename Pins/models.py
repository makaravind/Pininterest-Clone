from __future__ import unicode_literals

from django.db import models

class Pin(models.Model):

    tagline = models.CharField(max_length=25)
    interest = models.FileField(null=True, blank=True)
    created_on = models.DateField(auto_now_add=True, auto_now=False)
    updated_on = models.DateField(auto_now_add=False, auto_now=True)
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        # return self.tagline[:20] + '...'
        return self.tagline