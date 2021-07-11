from django.test import TestCase
from .models import Image, Profile

# Create your tests here.
class ImageTestclass(TestCase):
    #setup method
    def setUp(self):
        self.myimage=Image(image='image',name='Fai',caption='Nice',likes=0,comments='great')

     #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.myimage,Image))
    
    #save method
    def test_save_images(self):
        self.myimage.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)

    #delete method
    def test_delete_images(self):
        self.myimage.save_image()
        images_record=Image.objects.all()
        self.myimage.delete_image()
        self.assertTrue(len(images_record)==0)

    def test_update_caption(self):
        new_caption=Image.update_caption()
        expected_caption=f'{new_caption}'
        self.assertTrue(expected_caption,'new_image')


class ProfileTestclass(TestCase):
    #setup method
    def setUp(self):
        self.myprofile=Profile(profile_pic='image',bio='Hardworking')

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.myprofile,Profile))

    #save method
    def test_save_profile(self):
        self.myprofile.save_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)>0)

    def test_delete_profile(self):
        self.myprofile.save_profile()
        profile_record=Profile.objects.all()
        self.myprofile.delete_profile()
        self.assertTrue(len(profile_record)==0)

    def test_update_profile(self):
        new_profile=Profile.update_profile()
        expected_profile=f'{new_profile}'
        self.assertTrue(expected_profile,'new_image')
    






   