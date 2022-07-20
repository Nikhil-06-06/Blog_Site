from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User                    #gets the author user table from database

# Create your models here.
class Post(models.Model):                                      #The code for this class froms a table named post in the backend of our application containing the following fields, after making this table you have to aplly migration commands in your cmd, for the table to be created, a file will be created in the mogrations folder
    title = models.CharField(max_length=100) 
    content= models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)   #auto_now=True sets the date time as current date time whenever the post is updated, auto_now_add sets the date time as current whenever a new post is added   
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):                                #redirects the user to the post currently made after creation
        return reverse('post-detail', kwargs={'pk': self.pk})