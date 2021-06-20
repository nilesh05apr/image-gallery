from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField(blank = False, null = False, upload_to = "media/")
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.pk)