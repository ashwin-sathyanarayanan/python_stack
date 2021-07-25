from django.urls import path, include           # import include

urlpatterns = [
    path('', include('first_App.urls')),
]