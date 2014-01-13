# coding: utf-8

from django.contrib import admin
from content.models import Section, Accordeon, Number, Link, Slider 



# class TestModelAdmin(OrderedModelAdmin):
#   pass

admin.site.register(Section)
admin.site.register(Accordeon)
admin.site.register(Number)
admin.site.register(Link)
admin.site.register(Slider)