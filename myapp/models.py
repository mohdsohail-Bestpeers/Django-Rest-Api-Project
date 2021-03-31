from django.db import models

class React(models.Model):
    Name = models.CharField(max_length = 20)
    Detail = models.CharField(max_length = 150)     