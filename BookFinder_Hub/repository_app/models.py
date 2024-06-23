from django.db import models

# Create your models here.

class Repository(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='pdfs/')
