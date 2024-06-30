# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('password_generator/', views.password_generator, name='password_generator'),
    path('password_strength/', views.password_strength, name='password_strength'),
    path('download_strength_report/', views.download_strength_report, name='download_strength_report'),
    path('download_generated_password/', views.download_generated_password, name='download_generated_password'),
    path('check_generated_password_strength/', views.check_generated_password_strength, name='check_generated_password_strength'),
    path('password_tips/', views.password_tips, name='password_tips'),  
]
