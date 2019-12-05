from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('rock', views.rock, name='rock'),
    path('scissor', views.scissor, name='scissor'),
    path('paper', views.paper, name='paper'),
]
