from django.db import models
from photologue.models import Photo


# Create your models here.


class Section(models.Model):

    special_types = (
        ('portfolio', 'Portfolio'),
        ('accordeon', 'Accordeon'),
        ('form', 'Contact form'),
        ('text', 'Text/Html'),

    )
    order = models.SmallIntegerField(unique=False, blank=True)
    title = models.CharField(max_length=30)
    slug = models.CharField(max_length=15)
    header = models.TextField()
    special = models.CharField(max_length=10, choices=special_types)
    content = models.TextField(blank=True)
    image = models.ForeignKey(Photo, blank=True)
    image_text = models.TextField()

    class Meta:
        verbose_name = ('Section')
        verbose_name_plural = ('Sections')
        ordering = ['order']

    def __unicode__(self):
        return self.title


class Accordeon(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

    class Meta:
        verbose_name = ('Accordeon item')
        verbose_name_plural = ('Accordeon items')

    def __unicode__(self):
        return self.title


class Link(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=250, blank=True)
    url = models.URLField()
    image = models.ForeignKey(Photo)

    def __unicode__(self):
        return self.title


class Number(models.Model):
    number = models.CharField(max_length=10)
    text = models.CharField(max_length=300)

    def __unicode__(self):
        return self.title


class Slider(models.Model):
    order = models.SmallIntegerField(unique=False, blank=True)
    header = models.CharField(max_length=100)
    image = models.ForeignKey(Photo)
    def __unicode__(self):
        return self.header
    class Meta:
        verbose_name = ('Slider item')
        verbose_name_plural = ('Slider items')
