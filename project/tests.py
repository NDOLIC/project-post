# -*- coding: utf-8 -*-
from django.test import TestCase
from .models import Image,Profile

class ImageTestClass(TestCase):
       def setUp(self):
          
          self.profile=Profile(id=1,photo='Rwanda',bio='Kigali')
          self.image=Image(id=1,image='@heroo',name='koko',caption="koko koko koko okruuuuuu",likes=2,profile=self.profile)
          self.comment=Comment(id=1,comment='food',image=self.image)

       def tearDown(self):
           Profile.objects.all().delete()
           Image.objects.all().delete()
           Comment.objects.all().delete()

       def test_save_image(self):
         self.image.save_image()
         images = Image.objects.all()
         self.assertTrue(len(images) > 0)   

       def test_delete_image(self):
           self.image.save_image()
           self.image.delete_image()
           images = Image.objects.all()
           self.assertTrue(len(images) == 0) 

       def test_update_caption(self):
           self.image.save_image()
           caption='kiki'
           self.image.update_caption(caption)
           self.assertTrue( self.image.caption == caption) 
# Create your tests here.
class ProfileTestClass(TestCase):
       def setUp(self):
          
          self.profile=Profile(id=1234,photo='Rwanda',bio='Kigali')
          self.image=Image(id=1222,image='@heroo',name='koko',caption="koko koko koko okruuuuuu",likes=2,profile=self.profile)
          self.comment=Comment(id=2134,comment='food',image=self.image)
        
       def tearDown(self):
           Profile.objects.all().delete()
           Image.objects.all().delete()
           Comment.objects.all().delete()
       
       def test_save_profile(self):
         self.profile.save_profile()
         profiles = Profile.objects.all()
         self.assertTrue(len(profiles) > 0) 

        
       def test_delete_profile(self):
           self.profile.save_profile()
           self.profile.delete_profile()
           profiles = Profile.objects.all()
           self.assertTrue(len(profiles) == 0)  

       def test_update_caption(self):
           self.profile.save_profile()
           bio='kiki'
           self.profile.update_bio(bio)
           self.assertTrue( self.profile.bio == bio) 


