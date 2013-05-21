from django.db import models
from django.forms import ModelForm


class Project(models.Model):
    name = models.CharField(max_length=50,
            help_text="This is not very important. It's just used to name the project on this page, so you remember which one it is.",
            )
    slug = models.CharField(max_length=30,
            help_text="""only lowercase letters or numbers or dashes, no spaces. This will be used to create the URL link to your project."""
            )
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    text = models.TextField()
    snapshot = models.ImageField(
            upload_to='images/portfolio',
            help_text="Add a preview image for your project. This will be used on the project index page.",
            )

    def __unicode__(self):
        return self.name

class Item(models.Model):
    MEDIA_TYPES = (
            ('image','image'),
            ('iframe','iframe'),
    )

    order_key = models.IntegerField( default=4 )
    title = models.CharField(max_length=50)
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

class Download(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True )
    file = models.FileField(
            upload_to='files/downloads',
            )
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title


