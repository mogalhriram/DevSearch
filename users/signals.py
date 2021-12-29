
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
        )

def deleteUser(sender,instance,**kwargs):
    user = instance.user
    user.delete()


post_save.connect(createProfile,User)

post_delete.connect(deleteUser,Profile)

