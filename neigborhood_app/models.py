from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class Neigborhood(models.Model):
    
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    occupants = models.PositiveIntegerField()
    
    
class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    neigborhood = models.ForeignKey(Neigborhood,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='images/')
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    
    
    def __str__(self):
        return self.name


@receiver(post_save,sender=User)
def create_profile(sender, instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    
@receiver(post_save,sender=User)
def save_profile(sender, instance,**kwargs):
    instance.profile.save()
    
class Business(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey('User',on_delete=models.CASCADE)
    neigborhood = models.ForeignKey(Neigborhood, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    
    def create_business(self):
        self.save()
        
    def delete_business(self):
        self.delete()
        
    @classmethod
    def find_business(cls,id):
        search = cls.objects.get(id = id)
        return  search
    
    @classmethod   
    def update_business(cls,id,new_name):
        cls.objects.filter(pk = id).update(name=new_name)
        new_name_object = cls.objects.get(name = new_name)
        new_name = new_name_object.name
        return new_name
    
    def __str__(self):
        return self.name
    
    class Meta:
        
        order_by = ['name']
    
class Post(models.Model):
    
    title = models.CharField(max_length=100)
    post = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    def create_post(self):
        self.save()
        
    def delete_post(self):
        self.delete()
        
    @classmethod   
    def update_business(cls,id,post):
        cls.objects.filter(pk = id).update(post=post)
        new_post_object = cls.objects.filter(post__icontains = post)
        new_post = new_post_object.post
        return new_post
    
    @classmethod
    def get_single_post(cls,id):
        post = cls.objects.get(pk=id)
        return post