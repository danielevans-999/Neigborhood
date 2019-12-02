from django.test import TestCase
from .models import *
from django.utils import timezone

class NeigborhoodTestClass(TestCase):
    
    def setUp(self):
        self.neigborhood = Neigborhood(name='kenya',pic='images/dan.jpeg',location='nairobi',occupants=40,health_info=854,police_contact=986523,admin_id=3)


    def test_instance(self):
        self.assertTrue(isinstance(self.neigborhood,Neigborhood))
        
    def test_save_method(self):
        self.neigborhood.create_neigborhood()
        neigborhoods = Neigborhood.objects.all()
        self.assertTrue(len(neigborhoods)>0)
    
    def test_delete_method(self):
        self.neigborhood.create_neigborhood()
        self.neigborhood.delete_neigborhood()
        neigborhood = Neigborhood.objects.all()
        self.assertTrue(len(neigborhood) is 0)
        
    def test_update_neigborhood_method(self):
        self.neigborhood.create_neigborhood()
        new_name = 'Ruaraka' 
        update = self.neigborhood.update_neigborhood(self.neigborhood.id,new_name)
        self.assertEqual(update,new_name)
        
    def test_update_occupants_method(self):
        self.neigborhood.create_neigborhood()
        new_occpants = 400
        update = self.neigborhood.update_occupants(self.neigborhood.id,new_occpants)
        self.assertEqual(update,new_occpants)
        
        
    def tearDown(self):
        Neigborhood.objects.all().delete() 
        
        
        
        
        
class BusinessTestClass(TestCase):
    
    def setUp(self):
        self.business = Business(name='danteshop',user_id=3,neigborhood_id=1,email='daniel@gmail.com')


    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))
        
    def test_save_method(self):
        self.business.create_business()
        business = Business.objects.all()
        self.assertTrue(len(business)>0)
    
    def test_delete_method(self):
        self.business.create_business()
        self.business.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business) is 0)
        
    def test_update_bussiness_method(self):
        self.business.create_business()
        new_name = 'otibostores' 
        update = self.business.update_business(self.business.id,new_name)
        self.assertEqual(update,new_name)
        
    def test_find_method(self):
        self.business.create_business()
        bussiness = self.business.find_business(self.business.id)
        self.assertEquals(bussiness.name,'danteshop')
        
        
        
    def tearDown(self):
        Business.objects.all().delete() 
        
        
        
        
class PostTestClass(TestCase):
    
    def setUp(self):
        self.post = Post(title='home',post='home is thebest', date_posted=timezone.now(),user_id=3,neigborhood_id=1)


    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))
        
    def test_save_method(self):
        self.post.create_post()
        post = Post.objects.all()
        self.assertTrue(len(post)>0)
    
    def test_delete_method(self):
        self.post.create_post()
        self.post.delete_post()
        post = Post.objects.all()
        self.assertTrue(len(post) is 0)
        
    def test_update_bussiness_method(self):
        self.post.create_post()
        new_title = 'i think otherwise' 
        update = self.post.update_post(self.post.id,new_title)
        self.assertEqual(update,new_title)
        
    def test_find_method(self):
        self.post.create_post()
        post = self.post.get_single_post(self.post.id)
        self.assertEquals(post.title,'home')
        
        
        
    def tearDown(self):
        Post.objects.all().delete() 