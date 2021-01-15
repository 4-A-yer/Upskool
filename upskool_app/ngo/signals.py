from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import NgoProfile


@receiver(post_save, sender=User)
def create_ngoprofile(sender, instance, created, **kwargs):
    if created:
        NgoProfile.objects.create(ngouser=instance)


@receiver(post_save, sender=User)
def save_ngoprofile(sender, instance, **kwargs):
    instance.ngoprofile.save()