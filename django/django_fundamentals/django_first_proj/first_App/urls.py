from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<int:number>',views.num_display),
    path('<int:number>/delete',views.destroy),
]