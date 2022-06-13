from django.db import models
class chunha(models.Model):
        tenhoap = models.CharField(max_length=300)
        congdung = models.CharField(max_length=600)