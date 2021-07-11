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












   