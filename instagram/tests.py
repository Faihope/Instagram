from django.test import TestCase
from .models import Image

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











   