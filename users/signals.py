
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Profile
from django.conf import settings


#@receiver(sender=Profile, signal=post_save)
def createProfile(sender, instance, created, **kwargs):
   if created:
        profile = Profile.objects.create(
            user = instance,
            username = instance.username,
            name = instance.first_name,
            email = instance.email,
        )

        # body = 'We are excited to have you here. Start using our application and send your valuable feedback'
        # subject = 'Welcome to Devsearch'
        # send_mail(
        # subject,
        # body,
        # settings.EMAIL_HOST,
        # [profile.email],
        # fail_silently=False,
        # )

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

