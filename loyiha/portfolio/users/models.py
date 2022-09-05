from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=False, null=False)
    profile_image = models.ImageField(upload_to='portfolio')
    social_github = models.CharField(max_length=100, blank=True, null=True)
    social_telegram = models.CharField(max_length=100, blank=True, null=False)
    social_instagram = models.CharField(max_length=100, default="instagram")
    social_youtube = models.CharField(max_length=100, blank=True, null=True)
    social_website = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name}"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        Profile.objects.create(
            user=user
        )


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()