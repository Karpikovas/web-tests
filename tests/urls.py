from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_suite, name='test_suite'),
    path('register/', views.RegisterFormView.as_view(), name='register'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('<int:pk>/', views.QuestionDetailView.as_view(), name='questions'),

]