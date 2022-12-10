from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title
     
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})