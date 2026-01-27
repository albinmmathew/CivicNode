from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

#To autocreate profiles(admin, registration, shell, etc)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance,created, **kwargs):
	if created:	#if user exists(profile edited):doesn't create duplicate 
		Profile.objects.create(user=instance)