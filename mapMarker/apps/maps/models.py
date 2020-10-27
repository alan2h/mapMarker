from django.db import models


class Mark(models.Model):

    name = models.CharField(max_length=300, null=True, blank=True)
    estado = models.BooleanField(default=True)
    latitud = models.CharField(max_length=9000, null=False, blank=False)
    longitud = models.CharField(max_length=9000, null=False, blank=False)