from django.db import models

# Create your models here.
class Article(models.Model):
    slug = models.SlugField(null=False, blank=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    body = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True)
    createdAt = models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now_add = True)
    favourited = models.BooleanField()
    favoriteCount = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name