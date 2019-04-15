from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from .forms import NewsLetterForm

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 30)

    def save_category(self):
        """
        This is the function that we will use to save the instance of this class
        """
        self.save()

    def delete(self):
        """
        This is the method to delete the instance
        """
        Category.objects.get(id = self.id).delete()

    

    def __str__(self):
        return self.name


    @classmethod
    def delete_category(cls,name):
        cls.objects.filter(name = name).delete()

class Bus(models.Model):
    bus_name = models.CharField(max_length = 30)
    bus_category = models.ForeignKey(Category,on_delete = models.CASCADE)

    def save_bus(self):
        self.save()

    @classmethod
    def search_by_category(cls,search_term):
        buses = cls.objects.filter(bus_category__name__contains = search_term)
        return buses

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.CharField(default="Hi!", max_length = 30)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    
    @classmethod
    def search_user(cls,name):
        return User.objects.filter(username__icontains = name)


