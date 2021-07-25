from django.urls import path     
from . import views
urlpatterns = [
    path('first_route/', views.first_route),
    path('second_route/', views.second_route),
]
