from django.db.models.signals import post_save
from django.contrib.auth.models import User             #sender
from django.dispatch import receiver
from .models import Profile

#we are doing this so that every time a new user is made the userprofile is automatically made for it

@receiver(post_save, sender=User)                                       #this function means whenever a user is created(new user made), then send the signal(post_save) which is then recieved by the reciever which here is create_profile which has all the arguments which the signal post_save passes to it
def create_profile(sender, instance, created, **kwargs):                #this function runs every time a user is created, sender is the one sending signal(User), instance has the new user thats is created, created contains true if new user is created
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)                                       #this function means whenever a user is saved, then send the signal(post_save) which is then recieved by the reciever which here is save_profile which has all the arguments which the signal post_save passes to it
def save_profile(sender, instance, **kwargs):                           #this function runs every time a user is saved, sender is the one sending signal(User), instance has the new user thats is created
    instance.profile.save()                                             #savin the saved instance(User) to profile