from django.db import models
from datetime import date

# Create your models here.
def about_image_upload(instanse, filename):
    imagename, extension = filename.split('.')
    return 'Abouts/%s.%s' % (instanse.id, extension)

def team_image_upload(instanse, filename):
    imagename, extension = filename.split('.')
    return 'teams/%s.%s' % (instanse.id, extension)

def testimonials_image_upload(instanse, filename):
    imagename, extension = filename.split('.')
    return 'testimonials/%s.%s' % (instanse.id, extension)

class About(models.Model):
    img1 = models.ImageField(upload_to=about_image_upload,null=True)
    img2 = models.ImageField(upload_to=about_image_upload,null=True)
    title = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100)
    description = models.TextField()
    description_ar = models.TextField()
    @property
    def years_of_experience(self):
        return date.today().year - 2019
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
class About_list_item(models.Model):
    title = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100)
    about = models.ForeignKey("About", on_delete=models.CASCADE, related_name='list')
    
    def __str__(self):
        return self.title
    
class Fact(models.Model):
    @property
    def years_of_experience(self):
        return date.today().year - 2019
    team_members = models.IntegerField(default=0)
    happy_clients = models.IntegerField(default=0)
    
    def __str__(self):
        return 'Fact '+str(self.id)
    
class Team_member(models.Model):
    img = models.ImageField(upload_to=team_image_upload)
    name = models.CharField(max_length=50)
    name_ar = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    position_ar = models.CharField(max_length=50)
    facebook = models.CharField(max_length=100,null=True)
    twitter = models.CharField(max_length=100,null=True)
    instagram = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.name
    
class Feature(models.Model):
    title = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100)
    description = models.TextField()
    description_ar = models.TextField()
    
    def __str__(self):
        return self.title

class Feature_list_item(models.Model):
    title = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100)
    description = models.TextField()
    description_ar = models.TextField()
    feature = models.ForeignKey("Feature", on_delete=models.CASCADE, related_name='list')
    
    def __str__(self):
        return self.title

class Tesimonial(models.Model):
    img = models.ImageField(upload_to=testimonials_image_upload)
    name = models.CharField(max_length=50)    
    name_ar = models.CharField(max_length=50)    
    profession = models.CharField(max_length=100)
    profession_ar = models.CharField(max_length=100)
    comment = models.TextField()
    comment_ar = models.TextField()
    
    def __str__(self):
        return self.name