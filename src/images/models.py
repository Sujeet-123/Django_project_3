from django.db import models

# Create your models here.
class Image(models.Model):
    picture = models.ImageField()
    classfied = models.CharField(max_length=200,blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Image classfied at {}".format(self.uploaded.strftime('%y-%m-%y %H:%M'))

    def save(self, *args, **kwargs):
        try:
            print('success')
        except:
            print('classification failded')

        super().save(*args, **kwargs)