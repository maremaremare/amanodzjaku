from django import template
from photologue.models import Gallery, Photo


register = template.Library()

@register.inclusion_tag('portfolio.html')
def portfolio():
    '''
    Inclusion tag sample
    '''
    all_photos = Photo.objects.all()
    all_galleries = Gallery.objects.all()
    return {'all_photos':all_photos, 'all_galleries':all_galleries}

@register.filter(name='colorLastWord')
def colorLastWord(value):
    value_list = value.split(' ')
    print value_list
    if len(value_list)>1:
        
        value_list[-1] = '<span>'+ value_list[-1] + '</span>'
    result = ''
    for x in value_list:
        result+=x
    return result 
