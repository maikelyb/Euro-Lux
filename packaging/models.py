from django.db import models

# Create your models here.

def image_upload(instanse, filename):
    imagename, extension = filename.split('.')
    return 'Packs/%s.%s' % (instanse.id, extension)

class Pack(models.Model):
    img = models.ImageField(upload_to=image_upload,null=True)
    title = models.CharField(max_length=50, blank=True)
    title_ar = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    description_ar = models.TextField(blank=True)
    
    def __str__(self):
        return self.title