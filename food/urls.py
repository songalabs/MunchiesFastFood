from django.conf.urls import url
from django.views.generic import ListView, DetailView
from . import views
#from food.models import .
#from order.models import .

urlpatterns=[
	url(r'^$', views.index, name="index")]