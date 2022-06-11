from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,ondelete="CASCADE",null=True,blank=True)
    profile_photo = models.ImageField(default='default.png',upload_to='profiles/')
    bio = models.HtmlField(max_length=500,default='Tell me Something about yourself')
    phone_number = models.CharField(max_length=10,default='12345678')

class Projects(models.Model):
    profile = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=20,blank=True)
    design = models.IntegerField(default=0)
    content= models.IntegerField(default=0)
    image_landing = models.ImageField()(upload_to ='landing/')
    description = models.HtmlField(max_length=200, blank=True)
    link=URLOrRelativeField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

class Rates(models.Model):
    design = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    content = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)]) 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.IntegerField(default=0) 
    