
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile


#@receiver(sender=Profile, signal=post_save)
def createProfile(sender, instance, created, **kwargs):
   if created:
        Profile.objects.create(
            user = instance,
            username = instance.username,
            name = instance.first_name,
            email = instance.email,
        )

def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created== False:
        user.username = profile.username
        user.email = profile.email
        user.first_name = profile.name
        user.save


def deleteUser(sender,instance,**kwargs):
    user = instance.user
    user.delete()


post_save.connect(createProfile,User)
post_save.connect(updateUser,Profile)
post_delete.connect(deleteUser,Profile)

