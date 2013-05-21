from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=300)
    title = models.CharField(max_length=300, blank=True, null=True)
    bio = models.TextField( blank=True, null=True)
    image = models.ImageField(
            upload_to='images/people',
            )
    def __unicode__(self):
        return self.name




