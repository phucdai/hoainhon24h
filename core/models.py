from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    (1, 'Bản nháp'),
    (1, 'Công bố')
)


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True, default="")
    slug = models.SlugField(max_length=255, unique=True, default="")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    hits = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', default="")
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='images/')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
