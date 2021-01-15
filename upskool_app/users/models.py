from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from django.utils import timezone

PROFILE_TYPES = (
    (u'Gov', 'Government'),
    (u'NGO', 'NGO'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    type = models.CharField(choices=PROFILE_TYPES, max_length=16)

    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self,*args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

# class GovUser(models.Model):
#     profile = models.ForeignKey(Profile,  on_delete=models.CASCADE)
#     # Corporate fields here

#     class Meta:
#         db_table = 'gov_user'


# class NgoUser(models.Model):
#     profile = models.ForeignKey(Profile,  on_delete=models.CASCADE)
#     # Corporate fields here

#     class Meta:
#         db_table = 'ngo_user'



class Requirement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('req-detail', kwargs={'pk': self.pk})


