# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver





class Profile(models.Model):
    photo=models.ImageField(upload_to='images/',default='images/avatar.jpg')
    bio=models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    projectsposted = models.ForeignKey(Project,null=True)

    
    def save_profile(self):
        self.save()
    def delete_profile(self):
       self.delete()

    def update_bio(self,bio):
         self.bio=bio
         self.save()
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



class Post(models.Model):
    user = models.OneToOneField(User)
    post = models.ForeignKey(Project)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    link = models.CharField(max_length=1000)
    landingpic = models.ImageField(upload_to='images')
    username= models.CharField(max_length=20)
    user = models.OneToOneField(User)

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()