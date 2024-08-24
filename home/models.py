from django.db import models

# Create your models here.
def image_upload(instanse, filename):
    imagename, extension = filename.split('.')
    return 'carousels/%s.%s' % (instanse.id, extension)


class Carousel(models.Model):
    title_sm = models.CharField(max_length=100)
    title_sm_ar = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100)
    img = models.ImageField(upload_to=image_upload)

    def __str__(self):
        return 'carousel '+str(self.id)