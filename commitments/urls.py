from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.commitment_list, name='commitment_list'),
]