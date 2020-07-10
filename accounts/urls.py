from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('candidates/',views.candidates,name="candidates"),
    path('politicians/<str:pk>/',views.politicians,name="politicians"),
    
]