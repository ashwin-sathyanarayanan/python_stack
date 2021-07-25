from django.urls import path, include           # import include
urlpatterns = [
    path('', include('time_display.urls')),
]