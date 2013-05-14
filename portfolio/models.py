from django.db import models
from django.forms import ModelForm


class Project(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=30)
    title = models.CharField(max_length=50, blank=True, null=True)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField( blank=True, null=True )
    snapshot = models.ImageField(
            upload_to='images/portfolio',
            blank=True,
            null=True,
            )

    def __unicode__(self):
        return self.name

class Item(models.Model):
    MEDIA_TYPES = (
            ('image','image'),
            ('iframe','iframe'),
    )

    order_key = models.IntegerField( default=4 )
    title = models.CharField(max_length=50, blank=True, null=True )
    image = models.ImageField(
            # this could be a function instead of a string
            upload_to='images/portfolio',
            height_field = 'height',
            width_field = 'width',
            )
    media_type = models.CharField(max_length=50, default='image',
            choices = MEDIA_TYPES)
    embed_field = models.TextField( blank=True, null=True )
    text = models.TextField( blank=True, null=True )
    width = models.IntegerField()
    height = models.IntegerField()
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.title

