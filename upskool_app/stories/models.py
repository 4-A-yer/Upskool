from django.db import models
from PIL import Image
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Stories(models.Model):
    story_title = models.CharField(max_length=100)
    story_content = models.TextField()
    story_date_posted = models.DateTimeField(default=timezone.now)
    story_author = models.ForeignKey(User, on_delete=models.CASCADE)
    story_image = models.ImageField(default='default1.jpg', upload_to='success_stories')

    def __str__(self):
        return self.story_title

    def get_absolute_url(self):
        return reverse('story-detail', kwargs={'pk': self.pk})

