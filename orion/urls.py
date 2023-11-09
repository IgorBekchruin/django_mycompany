from django.urls import path
from django.views.generic import TemplateView
from .views import *


urlpatterns = [
    path('', TemplateView.as_view(template_name='orion/index.html'), name='index'),
    path('about/', TemplateView.as_view(template_name='orion/about.html'), name='about'),
    path('contact/', contact_view, name='contact'),
    path('products/', TemplateView.as_view(template_name='orion/products.html'), name='products'),

]
