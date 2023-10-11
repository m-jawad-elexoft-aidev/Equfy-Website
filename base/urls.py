from django.urls import path
from . import views
urlpatterns = [
path('faq1',views.faq1, name = 'faq1'),
path('contact_us', views.contact_us, name = 'contact_us')
]