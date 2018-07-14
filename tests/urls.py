from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.test_suite, name='test_suite'),
]