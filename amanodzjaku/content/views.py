# coding: utf-8
# Create your views here.
from content.models import  Section, Accordeon, Slider, Link 
from photologue.models import Category
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.shortcuts import render
from django import forms
from django.http import HttpResponse, Http404
from django.shortcuts import *
from django.template import RequestContext


class ExampleForm(forms.Form):
    name = forms.CharField(label=u'Имя')
    email = forms.EmailField(label=u'Email')
    subject = forms.CharField(label=u'Тема')
    message = forms.CharField(label=u'Сообщение', widget=forms.Textarea(attrs={'rows':2, 'cols':15}))

def hello(request):
    print ExampleForm()
    if request.method == "POST":
        form = ExampleForm(request.POST)
        message = 'Сообщение отправлено. Большое спасибо.'
        if form.is_valid():
            email = form.cleaned_data['email']
            messag = form.cleaned_data['message']
            from django.core.mail import send_mail
            send_mail('Сообщение от посетителя сайта dzjaku.ru', messag+u'\n\nОбратный адрес: '+email, 'visa.italia.ru@gmail.com', ('ksawie@gmail.com',))
        else:
            message = 'произошла ошибка'

        return HttpResponse(message)       

    return render(request, 'base.html', {'form':ExampleForm(), 'section_list': Section.objects.all(), 
    					'accordeon_list': Accordeon.objects.all(), 'category_list': Category.objects.all(), 
                         'slider_list': Slider.objects.all(), 'link_list': Link.objects.all()    })
###
#class BaseView(TemplateView):
#    template_name = "base.html"

 #   def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context

  #      context = super(BaseView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        #context['sidebar_title'] = define_root_Cat(request) 
   #     context['section_list'] = Section.objects.all()
    #    context['accordeon_list'] = Accordeon.objects.all()  
     #   context['category_list'] = Category.objects.all()
      #  context['slider_list'] = Slider.objects.all()  
       # context['link_list'] = Link.objects.all()          

        #return context