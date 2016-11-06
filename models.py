from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.models import ContentType

class SuModel(models.Model):
    model = models.ForeignKey(ContentType, models.CASCADE)

    def __unicode__(self):
        return self.model.model
