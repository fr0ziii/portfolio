from tokenize import blank_re
from django.db import models
from django.forms import ImageField

# Create your models here.

class Tag (models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images", default="placeholder.png")
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, null=True)


    def __str__(self):
        return self.headline
