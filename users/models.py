from django.db import models
from django.contrib.auth.models import User
from PIL import Image                                                               #for image compression we use pillow library

# Create your models here.

class Profile(models.Model):                                                        #inherenting the Model class from models
    user = models.OneToOneField(User, on_delete=models.CASCADE)                     #creating a one to one relationship bewtween user and profile, cascadehere means if the user is deleted delete the profile but if the profile is deleted the user wont get deleted, it's only a one way thing
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')      #we need to work with images inn python-django

    def __str__(self):
        return f'{self.user.username} Profile'                                      #so that the query result is more specific while quering the database

    def save(self):
        super().save()                                                              #super is used to run the save method os the parent class(Profile)

        img= Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
